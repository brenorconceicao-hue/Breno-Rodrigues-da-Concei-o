import os

# limpa terminal
os.system("cls")

# entrada
print('= solicitando dados =')
primeiro_numero = int(input('Digite o primeiro numero: '))
segundo_numero = int(input('Digite o segundo numero: '))

# processamento
soma = primeiro_numero + segundo_numero
subtracao = primeiro_numero - segundo_numero
multiplicacao = primeiro_numero * segundo_numero
divisao = primeiro_numero / segundo_numero

# saída
print('\n= exibindo dados =')
print('soma:', soma)
print('subtracao:', subtracao)
print('multiplicacao:', multiplicacao)
print('divisao:', divisao)
