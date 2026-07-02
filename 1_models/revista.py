from models.item_biblioteca import ItemBiblioteca

class Revista(ItemBiblioteca):

    def __init__(self, titulo, isbn, edicao, disponivel=True):
        super().__init__(titulo, isbn, disponivel)
        self.edicao = edicao

    def descrever(self):
        return f"Revista: {self.titulo} - Edição {self.edicao}"
