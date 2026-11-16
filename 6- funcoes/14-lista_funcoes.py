import os 
os.system("cls")


def calcular_media(notas):
 return sum(notas) / len(notas)

def mostrar_notas():
 notas = []
 quantidade = int(input("Quantas notas deseja digitar? "))

 for i in range(quantidade):
  nota = float(input(f"Digite a Nota {i + 1}: "))
  notas.append(nota)

 print("\nLista de notas:")
 for i in range(len(notas)):
  print(f"Nota {i + 1}: {notas[i]}")

 print(f"Média: {calcular_media(notas):.2f}")

mostrar_notas()