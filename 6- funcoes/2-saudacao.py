import os 
os.system('cls')

def mostrar_saudacao(nome, idade):
    print(f'nome {nome} tem {idade} anos')
nome = input("digite seu nome: ")

idade = input('Digite sua idade: ')

print('\n= exibindo dados =')
mostrar_saudacao(nome, idade)