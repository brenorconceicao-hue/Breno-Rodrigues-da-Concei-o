import os 
os.system('cls')

print('= INSERIDO NOTAS =')
vetor_notas = []
for i in range(3):
    notas = float(input(f'digite suas notas {i+1}º : '))
    vetor_notas.append(notas)

soma = sum(vetor_notas)
media = soma / 3

print('\n= EXIBINDO NOTAS =')

for indice, notas in enumerate(vetor_notas, start=1):
    print(f'{indice}º nota: {notas}')
    print(f'soma: {soma}')
    print(F'media: {media}')