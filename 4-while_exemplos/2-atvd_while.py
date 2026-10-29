import os
os.system('cls')

while True:
    numero = float(input('Digite a nota entre 0 e 10: '))
    
    if numero < 0 or numero > 10:
        print(f'Número inválido: {numero}. Tente novamente.')
    else:
        print(f'Nota válida digitada: {numero}')
        if numero >= 6:
            print('Aprovado!')
        else:
            print('Reprovado!')
        break

print('FIM')