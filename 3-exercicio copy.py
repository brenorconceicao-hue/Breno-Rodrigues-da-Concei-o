import os 
os.system('cls')

def logo_senai():
    print("\n=== SENAI ===")

def mostrar_dados(nome, email, telefone):
    print(f"Nome: {nome}\nE-mail: {email}\nTelefone: {telefone}")

cadastros = []

while True:
    os.system('cls')
    print("""
=== CADASTRO ===
1 - Cadastrar
2 - Listar
0 - Sair
""")

    opcoes = input("Escolha uma opção: ")

    match opcoes:
        
        case "1":
            logo_senai()
            print("= SOLICITANDO DADOS =")
            nome = input("Digite seu nome: ")
            email = input("Digite seu e-mail: ")
            telefone = input("Digite seu telefone: ")

            cadastros.append((nome, email, telefone))
            print("Cadastro realizado!")
            input('Toque para continuar')
        case "2":
            logo_senai()

            if not cadastros:
                print("Ainda não há cadastros.")
            else:
                print("= CADASTROS =")
                for nome, email, telefone in cadastros:
                    mostrar_dados(nome, email, telefone)
                    print("---")
                input('Toque para continuar')

        case "0":
            print("Saindo do programa...")
            break

        case _:
            print("Opção inválida. Escolha 1, 2 ou 0.")