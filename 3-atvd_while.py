import os 
os.system('cls')

soma = 0

for i in range(2):
    while True:
        nota = float(input(f'Digite a {i+1}ª nota do aluno: '))

        if nota >= 0 and nota <= 10:
            soma = soma + nota
            break  
        else:
            print('Número inválido! Digite uma nota entre 0 e 10.\n')

media = soma / 2

print(f'\nMédia: {media:.2f}')


    
