from abc import ABC, abstractmethod

class ItemBiblioteca(ABC):

    def __init__(self, titulo, isbn, disponivel=True):
        self.titulo = titulo
        self.isbn = isbn
        self._disponivel = disponivel

    @abstractmethod
    def descrever(self):
        pass

    def __str__(self):
        status = "Disponível" if self._disponivel else "Emprestado"
        return f"{self.titulo} | ISBN: {self.isbn} | {status}"
