import os
os.system("cls")

def calcular_soma(numero1, numero2):
    return numero1 + numero2

def calcular_subtracao(numero1, numero2):
    return numero1 - numero2

def calcular_multiplicacao(numero1, numero2):
    return numero1 * numero2

def calcular_divisao(numero1, numero2):
    if numero2 == 0:
        return "Não é possível dividir por zero."
    return numero1 / numero2


operacao = input("Escolha +, -, * ou /: ")

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if operacao == "+":
    resultado = calcular_soma(numero1, numero2)
elif operacao == "-":
    resultado = calcular_subtracao(numero1, numero2)
elif operacao == "*":
    resultado = calcular_multiplicacao(numero1, numero2)
elif operacao == "/":
    resultado = calcular_divisao(numero1, numero2)
else:
    resultado = "Operação inválida."

print(f"Resultado:", {resultado})

