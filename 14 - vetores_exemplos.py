import os
os.system('cls')
produtos = ['bife', 'batata', 'refrigerante', 'escova de dente', 'sabonete']
precos = [25, 20, 18, 15, 5]

total = 0

while True:
    print('\nOpções  Produtos         Preço')

    for i in range(len(produtos)):
        print(f'{i+1:<7} {produtos[i]:<16} R${precos[i]:.2f}')

    print('-' * 35)

    try:
        opcao = int(input('Digite uma opção de 1 a 5: '))

        if 1 <= opcao <= len(produtos):
            indice = opcao - 1

            print(f'\nVocê escolheu: {produtos[indice]} | Valor: R${precos[indice]:.2f}')

            total += precos[indice]

            print(f'Total da compra: R${total:.2f}')

        else:
            print('\nOpção inválida!')
            continue

    except ValueError:
        print('\nDigite um número válido!')
        continue

    continuar = input('\nDeseja escolher mais um produto? (s/n): ').strip().lower()

    if continuar != 's':
        break

print('\n' + '=' * 35)
print(f'Total final da compra: R${total:.2f}')
print('Obrigado pela compra!')
