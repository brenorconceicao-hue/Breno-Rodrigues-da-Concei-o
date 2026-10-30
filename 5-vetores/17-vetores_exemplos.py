
import os
os.system('cls')

lista_produtos = []


while True:
    os.system('cls')
    print('''
        ==== MERCADINHO DENDEZEIROS ====
        1- cadastrar produto
        2- listar todos os produtos
        3- atualizar produto
        4- remover produto
        5- buscar produto
        0 - Sair
        ''')
    opcao = int(input('Escolha uma opção: '))
    
    match opcao:

        case 1:
            #CREATE (INSERIR)
            print('=== CADASTRAR PRODUTO ===')
            nome_produto = input('Nome do produto: ').strip().upper

            if nome_produto in lista_produtos:
                print('Produto já cadastrado.')
            else:
                lista_produtos.append(nome_produto)
                print('Produto cadastrado com sucesso!')

        case 2:
            #READ (LER / BUSCAR / CONSULTAR)
            print('== PRODUTOS NO ESTOQUE ===')

            for posicao, produto in enumerate(lista_produtos):
                print(f'{posicao + 1} - {produto}')
                

            print(f'Total: {len(lista_produtos)}')

        case 3:
            # UPDATE (ATUALIZAR)
            print(' == ATUALIZAR PRODUTO == ')
            nome = input("Qual produto deseja atualizar?: ")

            if nome in lista_produtos:
                posicao = lista_produtos.index(nome)
                novo = input('Novo nome: ')
                lista_produtos[posicao] = novo
                print('Produto alterado com sucesso!')
            else:
                print('Produto não encontrado.')

        case 4:
            # DELETE (REMOVER)
            print(' == REMOVER PRODUTO == ')
            nome = input("Qual produto deseja remover?: ")

            if nome in lista_produtos:
                lista_produtos.remove(nome)
                print('Produto removido com sucesso!')
            else:
                print('Produto não encontrado.')

        case 5:
            #READ ( LER / CONSULTAR / BUSCAR)
            print(' == BUSCAR PRODUTO == ')
            nome = input("Qual produto deseja buscar?: ")

            if nome in lista_produtos:
                print(f'Produto encontrado: {nome}')
            else:
                print('Produto não encontrado.')

        case 0:
            print("Saindo do programa!")
            break

        case _:
            print("Opção inválida! \n Tente novamente mais tarde...")

    input('Pressione uma tecla para continuar')
