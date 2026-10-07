import os
import time
os.system('cls')

qtd_pares = 0
qtd_impares = 0
qtd_total = 0
soma_pares = 0
soma_total = 0

while True:
    numero = int(input("Digite um número inteiro positivo (0 para encerrar): "))
    
    
    if numero == 0:
        break
        
    soma_total += numero
    qtd_total += 1
    

    if numero % 2 == 0:
        qtd_pares += 1
        soma_pares += numero
    else:
        qtd_impares += 1


print("\n--- RESULTADOS ---")
print(f"Quantidade de números pares: {qtd_pares}")
print(f"Quantidade de números ímpares: {qtd_impares}")

if qtd_pares > 0:
    media_pares = soma_pares / qtd_pares
    print(f"Média dos valores pares: {media_pares:.2f}")
else:
    print("Média dos valores pares: Nenhum número par foi inserido.")

if qtd_total > 0:
    media_geral = soma_total / qtd_total
    print(f"Média geral dos números lidos: {media_geral:.2f}")
else:
    print("Média geral: Nenhum número foi inserido.")
    time.sleep(2)
    os.system('cls')