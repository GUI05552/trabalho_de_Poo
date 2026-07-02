"""
biblioteca_exception.py

Define a exceção personalizada utilizada pelo Sistema de Gerenciamento de
Biblioteca. Essa exceção é lançada sempre que ocorre uma violação das regras
de negócio da aplicação, como a tentativa de emprestar um item que já está
emprestado.
"""

class BibliotecaException(Exception):
    """
    Classe base para exceções do sistema de biblioteca.
    """
    pass
