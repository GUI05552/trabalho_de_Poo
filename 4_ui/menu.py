"""
menu.py

Responsável pela interface em modo texto do Sistema de Gerenciamento de
Biblioteca. Este módulo exibe o menu principal e recebe a opção escolhida
pelo usuário.
"""

def menu():

    print(" SISTEMA DE GERENCIAMENTO DE BIBLIOTECA")
    print("1 - Cadastrar Livro")
    print("2 - Cadastrar Revista")
    print("3 - Listar Itens")
    print("4 - Buscar Item")
    print("5 - Atualizar Item")
    print("6 - Excluir Item")
    print("7 - Realizar Empréstimo")
    print("0 - Sair")
    print("========================================")

    return input("Escolha uma opção: ")
