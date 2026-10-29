import os
os.system('cls')

print( '= INSERINDO 5 LIVROS = ')
vetor_livros = []
for i in range(5):
    livro = input('digite o nome do {i+1}º livro: ')
    vetor_livros.append(livro)


print('\n= EXIBINDO 5 LIVROS =')

for indice, livro in enumerate(vetor_livros, start=1):
        print(f'{indice}º: {livro}')