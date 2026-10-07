import os 
os.system('cls')

soma_salario = 0
total_de_pessoas = 0
maior_de_idade = None
menor_de_idade = None
Mulheres_maior_5000 = 0

while True:
    print('----MENU DE OPCAO----')
    print('Codigo |  Descriçao')
    print('  1    |  adicionar familia')
    print('  2    |  exibir resultados')
    print('  3    |    sair')
    opcao = input('digite a opçao :')

    if opcao == 1:
        print('----ADICIONAR PESSOA----')
        idade = int(input('digite sua idade'))
        sexo = input('digite seu sexo M/F')
        salario = input('digite seu salario')
        soma += salario
        total_de_pessoas =+ 1
    if maior_de_idade >= menor_de_idade  :
        maior_de_idade = idade
    if  menor_de_idade <= maior_de_idade:
        menor_de_idade = idade

