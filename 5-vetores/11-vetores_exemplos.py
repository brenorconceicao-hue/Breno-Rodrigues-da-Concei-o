import os 
os.system('cls')

print('INSERINDO NOTAS')
pares = 0
impares = 0
vector_numeros = []

for i in range(6):
    numero = float(input(f'digite os numeros {i+1}º : '))
    vector_numeros.append(numero)
    if numero % 2 == 0:
        
        pares = pares + 1
    else:
        impares = impares + 1 
        print(f'quantidades de pares : {pares}')
        print(f'quantidades de impares : {impares}')
