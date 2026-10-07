import os 
os.system('cls')

soma = 0
quantidade = 0

while True:
    valor = int(input('Digite um valor : '))
    
    if valor < 0:
        break
        
    soma += valor
    quantidade += 1

if quantidade > 0:
    media = soma / quantidade
    print(f"A média aritmética dos {quantidade} números digitado é: {media}")
else:
    print("Nenhum número positivo foi colocado.")