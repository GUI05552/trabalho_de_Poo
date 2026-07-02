#  Sistema de Gerenciamento de Biblioteca

Sistema desenvolvido em **Python** utilizando **Programação Orientada a Objetos (POO)** e **PostgreSQL** para gerenciamento de livros, revistas e empréstimos.

O projeto foi desenvolvido como trabalho prático da disciplina de **Engenharia de Software**, tendo como objetivo aplicar conceitos de orientação a objetos, persistência de dados e integração com banco de dados relacional.

---

#  Integrantes

* Nome do Integrante 1
* Nome do Integrante 2
* Nome do Integrante 3

---

# Sumário

1. Descrição do Sistema
2. Tecnologias Utilizadas
3. Conceitos de POO Aplicados
4. Funcionalidades
5. Estrutura do Projeto
6. Banco de Dados
7. Regras de Negócio
8. Como Executar

---

#  Descrição do Sistema

O Sistema de Gerenciamento de Biblioteca permite controlar o cadastro de livros e revistas, realizar empréstimos de itens e armazenar todas as informações em um banco de dados PostgreSQL.

O sistema foi desenvolvido utilizando os princípios da Programação Orientada a Objetos, garantindo organização, reutilização de código e facilidade de manutenção.

---

#  Tecnologias Utilizadas

* Python 3
* PostgreSQL
* psycopg2

---

#  Conceitos de Programação Orientada a Objetos

Durante o desenvolvimento foram aplicados os seguintes conceitos:

* Classes e Objetos
* Encapsulamento
* Herança
* Polimorfismo
* Classe Abstrata (`ABC`)
* Métodos Abstratos (`@abstractmethod`)
* Sobrescrita do método `__str__`
* Tratamento de Exceções Personalizadas

---

#  Funcionalidades

O sistema possui as seguintes funcionalidades:

* Cadastro de livros;
* Cadastro de revistas;
* Cadastro de usuários;
* Listagem de todos os itens cadastrados;
* Busca de itens por ISBN;
* Atualização dos dados dos itens;
* Exclusão de itens cadastrados;
* Registro de empréstimos;
* Controle automático da disponibilidade dos itens.

---

#  Estrutura do Projeto

```text
Biblioteca/
│
├── bib.py
├── README.md
└── requirements.txt
```

---

#  Banco de Dados

O sistema utiliza o **PostgreSQL** para persistência das informações.

## Tabelas

### tabela_itens

Responsável por armazenar todos os livros e revistas cadastrados.

Campos:

* ISBN (Chave Primária)
* Título
* Tipo
* Autor
* Edição
* Disponibilidade

### tabela_emprestimos

Responsável pelo registro dos empréstimos realizados.

Campos:

* ID
* ID do Usuário
* ISBN do Item

---

#  Regras de Negócio

| Código | Regra                                                    | Implementação                                                                                                      |
| ------ | -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| RN01   | Não permitir empréstimo de um item já emprestado.        | O sistema verifica o atributo `_disponivel`. Caso o item esteja indisponível, uma `BibliotecaException` é lançada. |
| RN02   | Após um empréstimo, o item torna-se indisponível.        | O atributo `_disponivel` é atualizado para `False`.                                                                |
| RN03   | Todo empréstimo deve ser registrado no banco de dados.   | O método `registrar_emprestimo_no_banco()` registra o empréstimo e atualiza a disponibilidade do item.             |
| RN04   | Cada item deve possuir um ISBN único.                    | O ISBN é definido como chave primária da tabela `tabela_itens`, evitando registros duplicados.                     |
| RN05   | As tabelas devem existir antes da utilização do sistema. | O método `preparar_banco()` cria automaticamente as tabelas utilizando `CREATE TABLE IF NOT EXISTS`.               |
| RN06   | Apenas objetos da biblioteca podem ser emprestados.      | O empréstimo aceita somente objetos derivados da classe abstrata `ItemBiblioteca`.                                 |
| RN07   | Apenas itens disponíveis podem ser emprestados.          | A disponibilidade é validada antes da realização do empréstimo, garantindo a consistência dos dados.               |

---

# ▶ Como Executar

## Pré-requisitos

Antes de executar o sistema é necessário possuir:

* Python 3 instalado;
* PostgreSQL instalado e em execução;
* Biblioteca `psycopg2`.

---

## Instalação

Instale a dependência utilizando o comando:

```bash
pip install psycopg2
```

Ou, caso utilize o arquivo de dependências:

```bash
pip install -r requirements.txt
```

---

## Configuração do Banco de Dados

No arquivo `bib.py`, configure os seguintes parâmetros de conexão:

* Host
* Database
* User
* Password
* Port

---

## Execução

Execute o programa com o comando:

```bash
python bib.py
```

Na primeira execução, o sistema criará automaticamente as tabelas necessárias no banco de dados, caso ainda não existam.

---
