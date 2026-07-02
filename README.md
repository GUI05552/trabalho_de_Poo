#  Sistema de Gerenciamento de Biblioteca

Sistema desenvolvido em **Python** utilizando **Programação Orientada a Objetos (POO)** e **PostgreSQL** para gerenciamento de livros, revistas e empréstimos.

O projeto foi desenvolvido como trabalho prático da disciplina de **Engenharia de Software**, tendo como objetivo aplicar conceitos de orientação a objetos, persistência de dados e integração com banco de dados relacional.

---

#  Integrantes

* GUILHERME MENDONÇA CASTRO
* JOANE DE ARAÚJO BATISTA 
* RAYSSA OLIVEIRA MARTINS DAS CHAGAS

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

## Descrição do Sistema

O Sistema de Gerenciamento de Biblioteca foi desenvolvido utilizando a linguagem Python e o banco de dados PostgreSQL, aplicando os principais conceitos de Programação Orientada a Objetos estudados na disciplina. O sistema permite o gerenciamento de livros e revistas, realizando o cadastro dos itens, o controle de empréstimos e o armazenamento das informações em um banco de dados relacional. Além disso, foram implementadas regras de negócio que garantem a integridade dos dados, impedindo, por exemplo, que um item indisponível seja emprestado novamente.

---

## Tecnologias Utilizadas

O projeto foi desenvolvido utilizando a linguagem Python como principal tecnologia para implementação da lógica do sistema. Para a persistência dos dados foi utilizado o PostgreSQL, sendo a conexão realizada por meio da biblioteca 'psycopg2', responsável pela comunicação entre a aplicação e o banco de dados.

---

## Conceitos de Programação Orientada a Objetos

O sistema aplica os seguintes conceitos de POO:

Durante o desenvolvimento do sistema foram aplicados diversos conceitos da Programação Orientada a Objetos. A classe abstrata 'ItemBiblioteca' foi utilizada para definir características comuns entre os itens da biblioteca. As classes Livro e Revista implementam herança ao estender essa classe abstrata, além de demonstrarem polimorfismo por meio da implementação do método 'descrever()'. O encapsulamento foi empregado utilizando o atributo '_disponivel', responsável por controlar a disponibilidade dos itens. Também foi criado um tratamento de exceções personalizado através da classe 'BibliotecaException', garantindo maior segurança durante a execução das operações.

---

## Funcionalidades

- Cadastro de livros
- Cadastro de revistas
- Cadastro de usuários
- Listagem de itens cadastrados
- Busca de itens por ISBN
- Atualização de informações dos itens
- Exclusão de itens
- Registro de empréstimos
- Controle de disponibilidade dos itens

---

## Estrutura do Projeto

text
biblioteca/
│
├── bib.py
├── README.md
└── requirements.txt


---

## Banco de Dados

O armazenamento das informações é realizado no PostgreSQL. Durante a primeira execução, o sistema cria automaticamente as tabelas necessárias caso elas ainda não existam. Atualmente são utilizadas as tabelas tabela_itens, responsável pelos livros e revistas cadastrados, e tabela_emprestimos, destinada ao registro dos empréstimos realizados.

### Tabelas

- tabela_itens
- tabela_emprestimos

---


## Regras de Negócio

| Código | Regra de Negócio | Implementação |
|:------:|------------------|---------------|
| RN01 | Não permitir que um item já emprestado seja emprestado novamente. | O sistema verifica o atributo _disponivel. Caso o item esteja indisponível, uma BibliotecaException é lançada. |
| RN02 | Após a realização de um empréstimo, o item torna-se indisponível. | O atributo _disponivel é alterado para False, indicando que o item está emprestado. |
| RN03 | Todo empréstimo deve ser registrado no banco de dados. | O método registrar_emprestimo_no_banco() registra o empréstimo e atualiza o status do item no PostgreSQL. |
| RN04 | Cada item da biblioteca deve possuir um ISBN único. | O banco utiliza o ISBN como chave primária. Caso o ISBN já exista, a cláusula ON CONFLICT (isbn) evita a duplicação do registro. |
| RN05 | As tabelas do banco de dados devem existir antes da utilização do sistema. | O método preparar_banco() cria automaticamente as tabelas utilizando CREATE TABLE IF NOT EXISTS. |
| RN06 | Apenas itens da biblioteca podem ser emprestados. | O empréstimo recebe objetos derivados da classe abstrata ItemBiblioteca, como Livro e Revista. |
| RN07 | Apenas itens disponíveis podem ter seu status alterado para emprestado. | A disponibilidade do item é alterada somente após a validação do empréstimo, garantindo a consistência das informações. |

---

## Como Executar

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
