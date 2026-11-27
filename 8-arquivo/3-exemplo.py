from dataclasses import dataclass
import os

os.system("cls")

@dataclass
class fornecedores:
    nome: str
    email: str
    telefone: str
    endereco: str

QUANTIDADE_FORNECEDORES = 2
lista_fornecedores = []

for i in range(QUANTIDADE_FORNECEDORES):
    novo_fornecedor = fornecedores(
        nome=input("Digite o nome: "),
        email=input("Digite o email: "),
        telefone=input("Digite o telefone: "),
        endereco=input("Digite o endereço: ")
    )
    lista_fornecedores.append(novo_fornecedor)

with open("fornecedores.csv", "a") as arquivo:
    for fornecedor in lista_fornecedores:
        arquivo.write(f"{fornecedor.nome}, {fornecedor.email}, {fornecedor.telefone}, {fornecedor.endereco}\n")
