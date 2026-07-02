from exceptions.biblioteca_exception import BibliotecaException

class Emprestimo:

    def __init__(self, usuario, item, banco):

        self.usuario = usuario
        self.item = item

        if not item._disponivel:
            raise BibliotecaException(
                f"O item '{item.titulo}' já está emprestado."
            )

        item._disponivel = False

        banco.registrar_emprestimo_no_banco(
            usuario.id_usuario,
            item.isbn
        )

    def __str__(self):
        return f"{self.item.titulo} emprestado para {self.usuario.nome}"
