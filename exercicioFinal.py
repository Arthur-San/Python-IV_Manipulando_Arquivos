## Agenda de Contatos

# Desenvolva uma agenda de contatos persistindo as informações em arquivo. O programa deve seguir as especificidades:

# 1. Criar o arquivo Agenda contendo quatro métodos:
#     1. Um método para adicionar contato.
#     2. Um método para listar contatos.
#     3. Um método para remover contatos.
# 2. Criar um arquivo principal para a aplicação que importar o módulo de agenda e chamar cada um dos métodos desenvolvidos de acordo com a opção escolhida.
from Agenda import add_contato, list_contatos,limpar_console

choice = 0

class Main:
    while choice != 5:
        print('------AGENDA------')
        print('1 - Adicionar contato')
        print('2 - Listar contatos')
        print('3 - Remover contato')
        print('4 - Limpar console')
        print('5 - SAIR')

        choice = int(input('O que deseja fazer?\n->'))

        if choice == 1:
            nome = input('Digite o nome: ')
            numero = int(input('Digite o numero: '))
            contato = add_contato(nome, numero)
        elif choice == 2:
                list_contatos()
        #elif choice == 3:
        elif choice == 4:
            limpar_console()
            
        elif choice == 5:
             print('Programa encerrado!')
             break
            
        

        

        