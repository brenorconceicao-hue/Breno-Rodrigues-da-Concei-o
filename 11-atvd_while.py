import os
import time
os.system('cls')

media = 0
print('RESULTADO FINAL')

for i in range(3):
    nota = float(input(f'Digite a  nota final (0 a 10): '))
    while nota < 0 or nota > 10:
        print('Nota inválida! A nota deve ser entre 0 e 10.')
        nota = float(input(f'Digite a  nota final (0 a 10): '))
        if media >= 7:
            print('Aprovado!')
        elif media < 5 or media <= 6.9:
            print('Recuperação!')
        else:
            media < 5
            print('Reprovado!')
    media += nota

media /= 3
print(f'A média final do aluno é: {media:.2f}') 
time.sleep(3)
os.system('cls')