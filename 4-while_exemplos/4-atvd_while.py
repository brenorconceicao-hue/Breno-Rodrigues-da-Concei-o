import os 
os.system('cls')

soma = 0

for i in range(2):
    while True:
        nota = float(input(f'Digite a {i+1}ª nota do aluno: '))
        nota += nota
        if nota > 0 or nota < 10:
            
            break
        else:
            soma = soma + nota 
            print('Número inválido! Digite uma nota entre 0 e 10.\n')
            print('nota entre 0 e 10 ')
            


