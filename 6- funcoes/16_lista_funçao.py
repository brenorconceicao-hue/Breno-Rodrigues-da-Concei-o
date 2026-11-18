import os
os.system('cls')

def analisar_imc(peso, altura):

    imc = peso / (altura * altura)
    
    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 24.9:
        classificacao = "Peso normal"
    elif imc < 30:
        classificacao = "Sobrepeso"
    elif imc < 35:
        classificacao = "Obesidade grau I"
    elif imc < 40:
        classificacao = "Obesidade grau II"
    else:
        classificacao = "Obesidade grau III"
        
    return imc, classificacao


altura = 1.75
lista_pesos = [50, 68, 82, 95, 112, 130]

print(f"Análise de IMC para altura de {altura}m:\n")

for peso in lista_pesos:
    valor_imc, categoria = analisar_imc(peso, altura)
    print(f"Peso: {peso:3} kg | IMC: {valor_imc:.2f} | Resultado: {categoria}")