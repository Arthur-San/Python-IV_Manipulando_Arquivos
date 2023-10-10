# 1. Criar o arquivo Agenda contendo quatro métodos:
#     1. Um método para adicionar contato.
#     2. Um método para listar contatos.
#     3. Um método para remover contatos.

def add_contato(nome, numero):
    with open("dados/exercicioFinal.txt", "a", encoding="utf-8") as file:
        file.write(f"\n{nome}/{numero}")

