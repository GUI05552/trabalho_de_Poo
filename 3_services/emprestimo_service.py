"""
emprestimo_service.py

Contém as regras de negócio relacionadas aos empréstimos.
"""

from models.emprestimo import Emprestimo


class EmprestimoService:

    def realizar_emprestimo(self, usuario, item, banco):
        return Emprestimo(usuario, item, banco)