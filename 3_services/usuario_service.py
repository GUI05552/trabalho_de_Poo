"""
usuario_service.py

Contém as regras de negócio relacionadas aos usuários.
"""

from models.usuario import Usuario


class UsuarioService:

    def criar_usuario(self, nome, id_usuario):
        return Usuario(nome, id_usuario)