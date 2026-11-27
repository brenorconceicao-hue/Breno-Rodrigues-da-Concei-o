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

arquivo = open("clientes", "r")

for i in range(QUANTIDADE_CLIENTES):
    nome, idade, altura = arquivo.readline().split(",")
    novo_cliente = clientes(nome=nome, idade=int(idade), altura=float(altura))
    lista_clientes.append(novo_cliente)

arquivo.close()

for cliente in lista_clientes:
    print(f"Nome: {cliente.nome} | Idade: {cliente.idade} | Altura: {cliente.altura}")
