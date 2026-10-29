import os
os.system('cls')


for i in range(2):
    if i == 0:
        nota = float(input('Digite a 1ª nota (0 a 10): '))
    else:
        nota = float(input('Digite a 2ª nota (0 a 10): '))
    while nota < 0 or nota > 10:
        print('Nota inválida! A nota deve ser entre 0 e 10.\n')
        nota = float(input('Digite a ' + ('1ª' if i == 0 else '2ª') + ' nota (0 a 10): '))

media = (nota + nota) / 2
print(f'A média do aluno é: {media:.2f}')