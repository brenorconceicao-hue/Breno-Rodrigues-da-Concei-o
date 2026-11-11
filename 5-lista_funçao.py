import os
import time
os.system('cls')

numero = int(input('Digite um numero para a tabuada: '))
def tabuada():
    for i in range(1, 11):
        print(f'{numero} x {i} = {numero * i }')
time.sleep(2)

print("\n = EXIBINDO RESULTADO = ")
tabuada()