import os
os.system('cls')  

lista_series = []

while True:

    os.system('cls')
    print("=== LISTA DE SÉRIES ===")
    print("1 - Cadastrar série")
    print("2 - Listar séries")
    print("0 - Sair")
    opcao = int(input("Escolha uma opção: "))  

    match opcao:
        case 1:
            print("=== CADASTRO DE SÉRIE ===")
            nome = input("Digite o nome da série: ").strip().upper()
            if nome == "":
                print("Nome da série não pode ser vazio.")
            elif nome in lista_series:
                print(f"Série {nome} já cadastrada.")
            else:
                lista_series.append(nome)
                print(f"Série {nome} cadastrada com sucesso")
                input("\nPressione Enter para continuar...")
        case 2:
            print("=== LISTA DE SÉRIES ===")
            if len(lista_series) == 0:
                print("Nenhuma série cadastrada.")
            else:
                for i, serie in enumerate(lista_series):
                    print(f"{i + 1} {serie}")
            input("\nPressione Enter para continuar...")
        case 0:
            print("Saindo do programa...")  
            break
        case _:
            print("Opção inválida. Tente novamente.")
            input("\nPressione Enter para continuar...")