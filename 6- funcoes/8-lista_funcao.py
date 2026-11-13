import os 
os.system('cls')

def verificar_impar_par():
    if numero % 2 == 0 :
        resultado = "o numero é par"
    else:
        resultado = 'o numero é impar'
    return resultado

numero = int(input("digite um numero:"))

impar_par = verificar_impar_par()

print(f"{impar_par}")