import os
os.system("cls")

print('''\n=== CADASTRO ===
1-Cadastrar
2-listar
3-sair''')
os.system('cls')

def logo_senai ():
    os.system('cls')
    



def mostrar_dados (nome, email , telefone):
    print(f'nome {nome} email {email} telefone {telefone}')
    
print("= SOLICITANDO DADOS =")
logo_senai ()

logo_senai ()
nome = input("digite seu nome: ")

logo_senai ()
email = input("digite seu email: ")

logo_senai ()

telefone = input("digite seu telefone: ")

print('EXIBINDO DADOS')

mostrar_dados (nome, email , telefone)
print(f'nome {nome} email {email} telefone {telefone}')