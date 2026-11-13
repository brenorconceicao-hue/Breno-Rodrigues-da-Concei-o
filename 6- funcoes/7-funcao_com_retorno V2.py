import os
os.system('cls')

def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media
print('= SOLICITANDO NOTAS = ')
nota1 = float(input('digite a primeira nota: '))
nota2 = float(input('digite a segunda nota: '))

media = calcular_media(nota1, nota2) / 2

print('= EXIBINDO NOTAS =')
print(f'media: {media}')