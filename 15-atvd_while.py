import os
os.system
soma_salarios = 0
quantidade = 0
maior_idade = 0
menor_idade = 0
mulheres = 0

while True:
    print("===== MENU =====")
    print("1 - Adicionar pessoa")
    print("2 - Exibir resultados")
    print("3 - Sair")
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        idade = int(input("Digite a idade: "))
        sexo = input("Digite o sexo (M/F): ").upper()
        salario = float(input("Digite o salário: R$ "))

        soma_salarios += salario
        quantidade += 1

        if quantidade == 1:
            maior_idade = idade
            menor_idade = idade
        else:
            if idade > maior_idade:
                maior_idade = idade

            if idade < menor_idade:
                menor_idade = idade

        if sexo == "F" and salario >= 5000:
            mulheres += 1
        os.system("cls")

    elif opcao == 2:
        os.system("cls")

        if quantidade > 0:
            media = soma_salarios / quantidade

            print("\n===== RESULTADOS =====")
            print(f"Média salarial: R$ {media:.2f}")
            print(f"Maior idade: {maior_idade} anos")
            print(f"Menor idade: {menor_idade} anos")
            print(
                "Mulheres com salário a partir de "
                f"R$ 5.000,00: {mulheres}")
        else:
            print("Nenhuma pessoa cadastrada.")
    elif opcao == 3:
        print("Programa encerrado!")
        break
    else:
        print("Opção inválida!")