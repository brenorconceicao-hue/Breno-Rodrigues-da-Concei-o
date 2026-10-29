
import os
import time
os.system('cls')

total_de_familias = 0
soma_salario = 0
soma_filho = 0
maior_salario = 0
menor_salario = 0

while True:
    print('\n------ MENU ------')
    print('1 - Adicionar familia')
    print('2 - Exibir resultados')
    print('3 - Sair')

    opcao = int(input('Escolha uma opcao: '))

    if opcao == 1:
        salario = float(input('Digite seu salario R$: '))
        filhos = int(input('Digite a quantidade de filhos: '))

        soma_salario += salario
        soma_filho += filhos
        total_de_familias += 1

        if total_de_familias == 1:
            maior_salario = salario
            menor_salario = salario
        else:
            if salario > maior_salario:
                maior_salario = salario

            if salario < menor_salario:
                menor_salario = salario

        print('Familia adicionada com sucesso!')

    elif opcao == 2:
        if total_de_familias > 0:
            media_de_salarios = soma_salario / total_de_familias
            media_de_filhos = soma_filho / total_de_familias

            print('\n==== RESULTADOS ====')
            print(f'Total de familias: {total_de_familias}')
            print(f'Media dos salarios: R$ {media_de_salarios:.2f}')
            print(f'Media de filhos: {media_de_filhos:.2f}')
            print(f'Maior salario: R$ {maior_salario:.2f}')
            print(f'Menor salario: R$ {menor_salario:.2f}')
            
        else:
            print('Nenhuma familia foi adicionada.')

    elif opcao == 3:
        print('\nPrograma encerrado!')
        break

    else:
        print('Opcao invalida!')
        input('aperte a tecla enter para continuar...')
        os.system('cls')
        time.sleep(3)