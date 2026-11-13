import os
os.system("cls")

def verificar_numero(numero):
    if numero < 0:
        print("O número é negativo.")
    elif numero > 0:
        print("O número é positivo.")
    else:
        print("O número é neutro.")

numero = int(input("Digite um número: "))
verificar_numero(numero)