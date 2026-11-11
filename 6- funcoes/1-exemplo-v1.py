import os
os.system("cls")

def cabecalho():
    print("\n")
    print('='*15)
    print('       SENAI')
    print('='*15)

    cabecalho()
    nome = input('digite seu nome: ')

    cabecalho()
    idade = input(int("digite sua idade"))
    cabecalho()
    print(f'nome: {nome}')
    print(f'idade: {idade}')