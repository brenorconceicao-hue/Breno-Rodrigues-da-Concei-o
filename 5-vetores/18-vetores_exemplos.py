
import os
os.system('cls')

lista_nome = []
lista_sobrenome = []

while True:
    os.system('cls')

    print('''==== HOSPITAL DENDEZEIROS ====
            1- Cadastrar paciente
            2- Listar paciente
            3- Atualizar paciente
            4- Remover paciente
            0- Sair
            ''')

    opcao = input('Escolha uma opção: ')

    match opcao:

        case '1':
            os.system('cls')
            print('==== CADASTRAR PACIENTE ====')

            nome = input('Digite o nome do paciente: ').upper()
            sobrenome = input('Digite o sobrenome do paciente: ').upper()

            if nome == '' or sobrenome == '':
                print('O nome e o sobrenome devem ser inseridos!')
            else:
                lista_nome.append(nome)
                lista_sobrenome.append(sobrenome)
                print('Paciente cadastrado!')

            input('Pressione ENTER para continuar...')

        case '2':
            os.system('cls')
            print('==== LISTA DE PACIENTES ====')

            if len(lista_nome) == 0:
                print('Não existem pacientes cadastrados!')
            else:
                for posicao, nome in enumerate(lista_nome):
                    print(f'{posicao + 1} - {nome} {lista_sobrenome[posicao]}')

            input('Pressione ENTER para continuar...')

        case '3':
            os.system('cls')
            print('==== ATUALIZAR PACIENTE ====')

            if len(lista_nome) == 0:
                print('Não existem pacientes cadastrados!')
            else:
                for posicao, nome in enumerate(lista_nome):
                    print(f'{posicao + 1} - {nome} {lista_sobrenome[posicao]}')

                numero = input('Digite o número do paciente: ')

                if numero.isdigit():
                    numero = int(numero)

                    if numero >= 1 and numero <= len(lista_nome):
                        nome = input('Digite o novo nome: ').upper()
                        sobrenome = input('Digite o novo sobrenome: ').upper()

                        if nome == '' or sobrenome == '':
                            print('O nome e o sobrenome devem ser inseridos!')
                        else:
                            lista_nome[numero - 1] = nome
                            lista_sobrenome[numero - 1] = sobrenome
                            print('Paciente atualizado!')
                    else:
                        print('Paciente não encontrado!')
                else:
                    print('Digite um número válido!')

            input('Pressione ENTER para continuar...')

        case '4':
            os.system('cls')
            print('==== REMOVER PACIENTE ====')

            if len(lista_nome) == 0:
                print('Não existem pacientes cadastrados!')
            else:
                for posicao, nome in enumerate(lista_nome):
                    print(f'{posicao + 1} - {nome} {lista_sobrenome[posicao]}')

                numero = input('Digite o número do paciente: ')

            if numero == '1' or numero == '2' or numero == '3':
             numero = int(numero)
else:
    print('Digite um número válido!')():
    numero = int(numero)

    if numero >= 1 and numero <= len(lista_nome):

                        nova_lista_nome = []
                        nova_lista_sobrenome = []

                        for posicao in range(len(lista_nome)):
                            if posicao != numero - 1:
                                nova_lista_nome.append(lista_nome[posicao])
                                nova_lista_sobrenome.append(lista_sobrenome[posicao])

                        lista_nome = nova_lista_nome
                        lista_sobrenome = nova_lista_sobrenome

                        print('Paciente removido com sucesso!')

    else:
                        print('Paciente não encontrado!')
            else:
                    print('Digite um número válido!')

            input('Pressione ENTER para continuar...')

        case '0':
            print('Saindo do sistema...')
            break

        case _:
            print('Opção inválida!')
            input('Pressione ENTER para continuar...')
