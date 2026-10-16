import os

os.system('cls')

vetor = []

for i in range(5):
    numero = float(input(f'Digite o {i+1}º número: '))
    

    if numero < 0:
        vetor.append(0)
    else:
        vetor.append(numero)


print(f'\nValores no vetor: {vetor}')
print('Itens do vetor:')
for num in vetor:
    print(num)