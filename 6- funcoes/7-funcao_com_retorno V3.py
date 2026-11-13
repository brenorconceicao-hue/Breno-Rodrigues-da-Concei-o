import os
os.system('cls')

def calcular_media(nota1, nota2):
    media = (nota1 + nota2 ) / 2
    return media
def verificar_resultado(media):
    if media >= 7:
        resultado = "aprovado"
    else:
        resultado = "reprovado"

    return resultado
print('= SOLICITANDO NOTAS = ')
nota1 = float(input('digite a primeira nota: '))
nota2 = float(input('digite a segunda nota: '))


media = calcular_media(nota1, nota2, ) / 2
situaçao = verificar_resultado(media)

print('= EXIBINDO NOTAS =')
print(f'media: {media}')
print(f"Resultado: {situaçao}")

