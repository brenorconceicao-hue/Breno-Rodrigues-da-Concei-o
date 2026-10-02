import os
os.system('cls')

print('Opcoes  Produtos    preco')
print('1        bife        90')
print('2       batata       20')
print('3    refrigerante    10')
print('4    escova de dente 15')
print('5       sabonete     12')
bife = 90
batata = 20
refrigerante = 10
escova_dente = 15
sabonete = 12

opcoes = int(input('digite a opcao de 1 a 5: '))
match opcoes:
    case 1:
        print(f'bife  valor: {bife}')
    case 2:
        print(f'batata  valor: {batata}')
    case 3:
        print(f'refrigerante  valor: {refrigerante}')
    case 4:
        print(f'escova de dente  valor: {escova_dente}')
    case 5:
        print(f'sabonete  valor: {sabonete}')
    case _:
        print('opcao invalida')

