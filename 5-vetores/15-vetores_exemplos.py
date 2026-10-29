import os
os.system('cls')
lista_produtos = []

while True:
  os.system('cls')
  print("=== MERCADINHO DENDEZEIROS ===")
  print("1 - Cadastrar produto")
  print("2 - Listar produtos")
  print("0 - Sair")
  opcao = int(input("Escolha uma opção: "))


  match opcao:
    case 1:
      print("=== CADASTRO DE PRODUTO ===")
      nome = input("Digite o nome do produto: ").strip().upper()
      if nome == "":
        print("Nome do produto não pode ser vazio.")
      elif nome in lista_produtos:
        print(f"Produto {nome} já cadastrado.")
      else:
        lista_produtos.append(nome)
        print(f"Produto {nome} cadastrado com sucesso")
        input("\nPressione Enter para continuar...")
    case 2:
      print("=== LISTA DE PRODUTOS ===")
      if len(lista_produtos) == 0:
        print("Nenhum produto cadastrado.")
      else:
        for i, produto in enumerate(lista_produtos):
          print(f"{i + 1} {produto}")
      input("\nPressione Enter para continuar...")
    case 0:
      print("Saindo do programa...")
      break  
    case _:
      print("Opção inválida. Tente novamente.")
      input("\nPressione Enter para continuar...")