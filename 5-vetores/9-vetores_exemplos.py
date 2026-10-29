import  os 
os.system('cls')


print('= INSERIDO NOTAS =')
vetor_notas = []
for i in range(4):
    notas = float(input(f'digite suas notas {i+1}º : '))
    vetor_notas.append(notas)
    if notas >= 7:
        print('aprovado')
    elif notas == 5 :
        print('recuperaçao')
    else:
        notas <= 5
        print('reprovado')
        
soma = sum(vetor_notas)
media = soma / 4

print('\n= EXIBINDO NOTAS =')

for indice, notas in enumerate(vetor_notas, start=1):
    print(f'{indice}º nota: {notas}')
    print(F'media: {media}')
    