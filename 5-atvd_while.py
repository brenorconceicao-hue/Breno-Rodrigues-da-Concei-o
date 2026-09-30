import os

os.system('cls')

usuario_correto = "senai"
senha_correta = "1234"

while True:
    usuario = input("Digite o seu login: ")
    senha = input("Digite a sua senha: ")

    if usuario == usuario_correto and senha == senha_correta:
        print("Login realizado com sucesso! Bem-vindo.")
        break
    else:
        input('pressione uma tecla para continuar...')
    os.system ('cls')
        