## Models

A pasta **`models`** reúne as classes responsáveis por representar as entidades do domínio do Sistema de Gerenciamento de Biblioteca. Essas classes modelam os objetos utilizados pela aplicação e implementam os principais conceitos da Programação Orientada a Objetos (POO).

### Classes do projeto

* **ItemBiblioteca:** classe abstrata que define os atributos e comportamentos comuns aos itens da biblioteca.
* **Livro:** representa um livro cadastrado no sistema.
* **Revista:** representa uma revista cadastrada no sistema.
* **Usuario:** representa os usuários responsáveis pelos empréstimos.
* **Emprestimo:** representa o processo de empréstimo entre um usuário e um item da biblioteca, aplicando as regras de negócio relacionadas à disponibilidade dos itens.

### Conceitos de POO aplicados

Nesta pasta são implementados os seguintes conceitos:

* Classes e Objetos;
* Encapsulamento;
* Herança;
* Polimorfismo;
* Classe Abstrata (`ABC`);
* Métodos Abstratos (`@abstractmethod`);
* Sobrescrita do método `__str__`.

Essas classes servem como base para o funcionamento do sistema, permitindo que os dados sejam manipulados de forma organizada, reutilizável e de fácil manutenção.
