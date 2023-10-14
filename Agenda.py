# 1. Criar o arquivo Agenda contendo quatro métodos:
#     1. Um método para adicionar contato.
#     2. Um método para listar contatos.
#     3. Um método para remover contatos.

import os

def add_contato():
    name = input('Informe o nome: ')
    adress = input('Informe o endereço: ')
    phone = input('Informe o fone: ')

    contact = f"Nome: {name} \nEndereço: {adress} \nTelefone: {phone}"

    with open("dados/exercicioFinal.txt", "a", encoding="utf-8") as file:
        file.write(contact)


def list_contatos():
    if not os.path.exists("dados/exercicioFinal.txt"):
        print('A lista está vazia')
        return
    else:
        with open("dados/exercicioFinal.txt", "r", encoding="utf-8") as file:
            contacts = file.read()
    print("-------LISTA DE CONTATOS-------")
    print(f"{contacts}\n")


def remove_contato():
    if not os.path.exists("dados/exercicioFinal.txt"):
        print('A lista está vazia')
        return
    else:
        with open("dados/exercicioFinal.txt", "w", encoding="utf-8") as file:
            file.write("")
        

def limpar_console():
    import os
    os.system('cls')