import os 
os.system('cls')

def calcular_notas(nota1, nota2):
    resultado = nota1 + nota2
    return resultado
print('= SOLICITANDO NOTAS = ')
nota1 = float(input('digite a primeira nota: '))
nota2 = float(input('digite a segunda nota: '))

soma = calcular_notas(nota1, nota2)

print('= EXIBINDO NOTAS =')
print(f'Soma: {soma}')