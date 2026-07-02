from models.item_biblioteca import ItemBiblioteca

class Livro(ItemBiblioteca):

    def __init__(self, titulo, isbn, autor, disponivel=True):
        super().__init__(titulo, isbn, disponivel)
        self.autor = autor

    def descrever(self):
        return f"Livro: {self.titulo} - Autor: {self.autor}"
