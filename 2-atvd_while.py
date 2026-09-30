import os 
os.system('cls')

while True:
    numero = int(input('digite a nota entre 0 e 10:'))
    if numero < 0 or numero > 10 :
        print(f'numero invalido{numero}')
        print('reprovado')
    else:
        print(f'numero entre 0 e 10{numero}')
        print('aprovado')
        break 
        print('FIM')