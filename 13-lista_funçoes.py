import os
from datetime import date

os.system("cls")  

def idade():
    ano_de_nascimento = int(input("Insira seu ano de nascimento: "))
    ano_atual = date.today().year

    idade_calculada = ano_atual - ano_de_nascimento
    return idade_calculada

resultado = idade()
print(f"Sua idade aproximada é {resultado} anos.")