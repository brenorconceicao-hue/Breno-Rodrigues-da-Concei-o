import os 
os.system('cls')

soma = 0
contador = 0

while True:
    nota = float(input("Digite uma nota: "))
    soma += nota
    contador += 1
    
    resposta = input("Deseja inserir mais uma nota: ")
    
    if resposta == "N":
        break

if contador > 0:
    media = soma / contador
    print(f'\n Quantidade de iterações (notas): {contador}')
    print(f"A média aritmética é: {media:.2f}")