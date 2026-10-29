import os
import time
os.system('cls') 
print('Faça seu cadastro')
nome = input('Digite seu nome: ')
senha = input('Digite a sua senha: ')

while True:
    print('login')
    nome_login = input('Digite seu nome: ')
    senha_login = input('Digite a sua senha: ')
    if nome_login == nome and senha_login == senha:
        print('Login realizado com sucesso!')
        break
    else:
        print('Login ou senha incorretos. Tente novamente.')
        time.sleep(2)
        os.system('cls')