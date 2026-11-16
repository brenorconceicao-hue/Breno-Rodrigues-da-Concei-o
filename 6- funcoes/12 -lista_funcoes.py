import os
os.system("cls")

def inflacionar_preco(preco):
    if preco >= 100:
        return preco * 1.10
    else:
        return preco * 1.20


while True:
    print("\n=== Menu ===")
    print("1 - Calcular preço com inflação")
    print("2 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        preco = float(input("Digite o preço do produto: R$ "))
        novo_preco = inflacionar_preco(preco)
        print(f"Preço com inflação: R$ {novo_preco:.2f}")
    elif opcao == "2":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida. Tente novamente.")