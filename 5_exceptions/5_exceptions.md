##  Exceptions

A pasta **`exceptions`** contém as exceções personalizadas utilizadas pelo Sistema de Gerenciamento de Biblioteca. Essas exceções são responsáveis por identificar e tratar situações que violam as regras de negócio da aplicação, permitindo um controle mais seguro dos erros e fornecendo mensagens claras ao usuário.

A utilização de exceções personalizadas torna o código mais organizado, facilita a manutenção e evita o uso excessivo de verificações condicionais ao longo da aplicação.

### Arquivos do projeto

* **biblioteca_exception.py:** define a classe `BibliotecaException`, utilizada para representar erros específicos do sistema, como a tentativa de emprestar um item que já se encontra indisponível.

### Responsabilidades

A camada de exceções é responsável por:

* Definir exceções específicas para o sistema;
* Identificar violações das regras de negócio;
* Permitir o tratamento centralizado de erros;
* Fornecer mensagens de erro claras e compreensíveis ao usuário;
* Aumentar a robustez e a confiabilidade da aplicação.

A utilização de exceções personalizadas contribui para uma melhor organização do código, tornando o sistema mais seguro, legível e de fácil manutenção.
