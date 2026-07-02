class Usuario:

    def __init__(self, nome, id_usuario):
        self.nome = nome
        self.id_usuario = id_usuario

    def __str__(self):
        return f"{self.nome} ({self.id_usuario})"
