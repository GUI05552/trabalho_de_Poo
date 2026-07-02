# Explicação dos Diagramas — Sistema de Biblioteca

> Documentação baseada nos arquivos `bib.py` e `sistema_de_biblioteca.py`.

---

## 1. Diagrama de Casos de Uso

O diagrama de casos de uso descreve **o que o sistema faz** do ponto de vista dos atores externos, sem entrar em detalhes de implementação.

### Atores

| Ator | Descrição |
|------|-----------|
| **Usuário** | Leitor que interage com o sistema para consultar itens e realizar empréstimos. |
| **PostgreSQL** | Sistema de banco de dados externo, presente somente em `bib.py`. |

### Casos de uso

| Caso de uso | Descrição |
|-------------|-----------|
| Listar e descrever itens | Chama `descrever()` polimorficamente em `Livro` e `Revista`, exibindo informações de cada item. |
| Realizar empréstimo | Instancia a classe `Emprestimo`, ligando um `Usuario` a um `ItemBiblioteca`. |
| Verificar disponibilidade | Checagem interna do atributo `_disponivel`, sempre acionada ao realizar um empréstimo (`«include»`). |
| Lançar exceção | Dispara `BibliotecaException` caso o item já esteja emprestado — acionado condicionalmente (`«extend»`). |
| Registrar no banco | Persiste o empréstimo no PostgreSQL via `BancoDeDados` — presente somente em `bib.py` (`«include»`). |

### Estereótipos UML utilizados

- `«include»` — o caso de uso base **sempre** aciona o incluído, obrigatoriamente.
- `«extend»` — o caso incluído só é acionado **condicionalmente**, quando o item já está indisponível.

---

## 2. Diagrama de Classes

O diagrama de classes mostra a **estrutura estática** do sistema: classes, atributos, métodos e os relacionamentos entre elas.

### Classes

| Classe | Tipo | Presente em |
|--------|------|-------------|
| `ItemBiblioteca` | Abstrata (ABC) | ambos os arquivos |
| `Livro` | Concreta, herda `ItemBiblioteca` | ambos os arquivos |
| `Revista` | Concreta, herda `ItemBiblioteca` | ambos os arquivos |
| `Usuario` | Classe de domínio | ambos os arquivos |
| `Emprestimo` | Classe de domínio | ambos os arquivos |
| `BibliotecaException` | Exceção customizada | ambos os arquivos |
| `BancoDeDados` | Infraestrutura / persistência | somente `bib.py` |

### Atributos e métodos principais

**ItemBiblioteca (abstrata)**
- `titulo: str`, `isbn: str`, `_disponivel: bool` (encapsulado)
- `descrever()` — método abstrato implementado pelas subclasses
- `__str__()` — retorna o status e o título do item

**Livro**
- Herda tudo de `ItemBiblioteca` e adiciona `autor: str`
- Implementa `descrever()` com o nome do autor

**Revista**
- Herda tudo de `ItemBiblioteca` e adiciona `edicao: int`
- Implementa `descrever()` com o número da edição

**Usuario**
- `nome: str`, `id_usuario: str`
- `__str__()` — exibe nome e ID

**Emprestimo**
- Associa um `Usuario` a um `ItemBiblioteca`
- No construtor: verifica `_disponivel`, seta para `False` e, em `bib.py`, aciona `BancoDeDados`
- Lança `BibliotecaException` se o item já estiver emprestado

**BancoDeDados** (somente `bib.py`)
- `conectar()` — abre conexão com o PostgreSQL via psycopg2
- `preparar_banco()` — cria as tabelas caso não existam
- `salvar_item_se_nao_existir(item)` — insere ou atualiza o item
- `registrar_emprestimo_no_banco(id_usuario, isbn)` — salva o empréstimo e marca o item como indisponível

### Relacionamentos

| Relacionamento | Entre | Tipo |
|----------------|-------|------|
| Herança | `Livro` → `ItemBiblioteca` | Generalização |
| Herança | `Revista` → `ItemBiblioteca` | Generalização |
| Associação | `Emprestimo` → `Usuario` | Dependência (usa) |
| Associação | `Emprestimo` → `ItemBiblioteca` | Dependência (usa) |
| Dependência | `Emprestimo` → `BancoDeDados` | Dependência (usa) — somente `bib.py` |
| Raises | `Emprestimo` → `BibliotecaException` | Lança exceção |

---

## 3. Diagrama de Sequência

O diagrama de sequência mostra o **fluxo de mensagens em tempo de execução** entre os objetos, dividido em três blocos.

### Bloco 1 — Setup dos objetos

1. `main` instancia `Livro("A Fantástica Fábrica...", "12345", "Tolkien")`.
2. `main` instancia `Usuario("Alice", "U001")`.
3. `main` chama `banco.preparar_banco()` → cria as tabelas no PostgreSQL se não existirem.
4. `main` chama `banco.salvar_item_se_nao_existir(livro)` → persiste o livro no banco.

### Bloco 2 — Empréstimo bem-sucedido (`emp1`)

1. `main` instancia `Emprestimo(usuario, livro, banco)`.
2. `Emprestimo` consulta `livro._disponivel` → retorna `True`.
3. `Emprestimo` seta `livro._disponivel = False`.
4. `Emprestimo` chama `banco.registrar_emprestimo_no_banco(id_usuario, isbn)`.
5. O banco salva o registro e atualiza o item para indisponível.
6. `emp1` é criado e retornado para `main`.

### Bloco 3 — Segundo empréstimo com exceção (`emp2`)

1. `main` tenta instanciar `Emprestimo(usuario, livro, banco)` novamente com o mesmo livro.
2. `Emprestimo` consulta `livro._disponivel` → retorna `False`.
3. `Emprestimo` lança `BibliotecaException("O item já está emprestado.")`.
4. O bloco `except BibliotecaException` em `main` captura o erro.
5. `main` imprime a mensagem de erro no terminal.

---

## 4. MER Conceitual (Notação Chen)

O MER Conceitual representa as **regras de negócio** em nível abstrato, usando a notação de Peter Chen: retângulos para entidades, losangos para relacionamentos e ovais para atributos.

### Entidades e seus atributos

| Entidade | Atributos |
|----------|-----------|
| **USUARIO** | ID (identificador único), Nome, CPF, Telefone, E-mail |
| **EMPRESTIMO** | ID (identificador único), Data_Emprestimo, Data_Dev_Prevista |
| **LIVRO** | ID (identificador único), Título, Autor, ISBN, Ano |

### Relacionamentos e cardinalidades

**USUARIO — realiza — EMPRESTIMO (1:N)**
Um usuário pode realizar vários empréstimos ao longo do tempo, mas cada empréstimo pertence a exatamente um usuário. Por isso a cardinalidade é 1 para N: do lado do usuário vale 1, do lado do empréstimo vale N.

**EMPRESTIMO — contém — LIVRO (N:M)**
Um empréstimo pode conter vários livros, e um mesmo livro pode aparecer em vários empréstimos diferentes ao longo do tempo (emprestado, devolvido, emprestado novamente). Por isso a cardinalidade é N para M, o que no modelo físico exigirá uma tabela de junção.

---

## 5. Modelo Lógico / Físico (Tabelas)

O modelo lógico/físico mapeia o MER Conceitual para **tabelas de banco de dados relacionais**, explicitando Chaves Primárias (PK) e Chaves Estrangeiras (FK). A relação N:M entre Empréstimos e Livros gera uma quarta tabela intermediária chamada `Itens_Emprestimo`.

### Tabela: Usuarios

| Campo | Tipo | Restrição |
|-------|------|-----------|
| id_usuario | INT | PK — identificador único do leitor |
| nome | VARCHAR | Nome completo |
| cpf | VARCHAR | CPF do leitor |
| email | VARCHAR | Endereço de e-mail |
| telefone | VARCHAR | Telefone de contato |

### Tabela: Livros

| Campo | Tipo | Restrição |
|-------|------|-----------|
| id_livro | INT | PK — identificador único da obra |
| titulo | VARCHAR | Título do livro |
| autor | VARCHAR | Nome do autor |
| isbn | VARCHAR | Código ISBN |
| qtd_disponivel | INT | Quantidade disponível no acervo |
| ano | INT | Ano de publicação |
| disponivel | BOOLEAN | Indica se há exemplar disponível |

### Tabela: Emprestimos

| Campo | Tipo | Restrição |
|-------|------|-----------|
| id_emprestimo | INT | PK — identificador único da transação |
| data_retirada | DATE | Data em que o livro foi retirado |
| data_dev_prevista | DATE | Data prevista para devolução |
| status | VARCHAR | Estado atual: "Pendente" ou "Devolvido" |
| id_usuario | INT | FK → Usuarios (quem realizou o empréstimo) |

### Tabela: Itens_Emprestimo *(tabela de junção)*

| Campo | Tipo | Restrição |
|-------|------|-----------|
| id_emprestimo | INT | PK + FK → Emprestimos |
| id_livro | INT | PK + FK → Livros |

`id_emprestimo` e `id_livro` juntos formam a **Chave Primária Composta** desta tabela. Ela existe para resolver a relação N:M entre Emprestimos e Livros: cada linha representa um livro específico dentro de um empréstimo específico.

### Cardinalidades entre as tabelas

| Tabela A | Cardinalidade | Tabela B | Via |
|----------|---------------|----------|-----|
| Usuarios | 1 — N | Emprestimos | FK `id_usuario` |
| Emprestimos | 1 — N | Itens_Emprestimo | FK `id_emprestimo` |
| Livros | 1 — N | Itens_Emprestimo | FK `id_livro` |

---

*Documentação gerada com base nos arquivos `bib.py` e `sistema_de_biblioteca.py`.*
