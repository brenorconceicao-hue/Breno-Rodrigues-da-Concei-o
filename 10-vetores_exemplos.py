import os
os.system('cls')



print('= INSERIDO NOTAS =')
vetor_numeros = []
for i in range(5):
    notas = float(input(f'digite suas notas {i+1}º : '))
    vetor_numeros.append(notas)

menor_nota = min(vetor_numeros)
maior_nota = max(vetor_numeros)
        


print('\n= EXIBINDO NOTAS =')

for posicao, notas in enumerate(vetor_numeros, start=1):
    print(f' {posicao}ª numero: {notas}')
print(f'menor nota: {menor_nota}')
print(f'maior nota: {maior_nota}')