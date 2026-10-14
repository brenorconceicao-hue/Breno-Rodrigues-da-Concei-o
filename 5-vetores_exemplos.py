import os 
os.system('cls')

print( '= INSERINDO NUMEROS NO VETOR = ')
vetor_numeros = []
for i in range(3):
    numero = int(input('digite um numero: '))
    vetor_numeros.append(numero)


print('\n= EXIBINDO NUMEROS DO VETOR =')

for valor in vetor_numeros:
    print(f'Valor: {valor}')