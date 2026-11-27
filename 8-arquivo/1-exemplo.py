from dataclasses import dataclass
import os

os.system("cls")

@dataclass
class clientes:
    nome: str
    idade: int
    altura: float

QUANTIDADE_CLIENTES = 2
lista_clientes = []

for i in range(QUANTIDADE_CLIENTES):
    novo_cliente = clientes(
        nome=input("Digite o nome: "),
        idade=int(input("Digite a idade: ")),
        altura=float(input("Digite a altura: "))
    )
    lista_clientes.append(novo_cliente)

with open("clientes", "a") as arquivo:
    for cliente in lista_clientes:
        arquivo.write(f"{cliente.nome}, {cliente.idade}, {cliente.altura}\n")

print("Dados salvos com sucesso!")
