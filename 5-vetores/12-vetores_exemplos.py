import os 
os.system('cls')

print('INSERINDO NUMEROS')
quantidades_negativos= 0
vetor_numeros = []
soma_positivos = 0

for i in range(5):
    numero = float(input(f'digite o {i+1}º numero:'))
    vetor_numeros.append(numero)
    os.system('cls')
    for num in vetor_numeros:
        if numero < 0:
            quantidades_negativos += 1
        elif numero > 0 :
            soma_positivos += numero
            os.system('cls')
            print('EXIBINDO NUMEROS')
            print(f'quantidades de numeros negativos: {quantidades_negativos}')
            print(f'quantidades de numeros positivos: {soma_positivos}')