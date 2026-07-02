"""
livro_service.py

Contém as regras de negócio relacionadas aos livros.
"""

from database.banco_de_dados import BancoDeDados


class LivroService:

    def __init__(self):
        self.banco = BancoDeDados()
    def cadastrar_livro(self, livro):
        self.banco.salvar_item(livro)

    def listar_livros(self):
        return self.banco.listar_itens()

    def buscar_livro(self, isbn):
        return self.banco.buscar_item(isbn)

    def atualizar_livro(self, isbn, novo_titulo):
        self.banco.atualizar_item(isbn, novo_titulo)

    def excluir_livro(self, isbn):
        self.banco.excluir_item(isbn)