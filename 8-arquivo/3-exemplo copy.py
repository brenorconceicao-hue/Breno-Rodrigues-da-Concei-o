from dataclasses import dataclass
import os

os.system("cls")

@dataclass
class fornecedores:
    nome: str
    email: str
    telefone: str
    endereco: str

lista_fornecedores = []

with open("fornecedores.csv", "r") as arquivo:
    for linha in arquivo:
        nome, email, telefone, endereco = linha.split(",")
        novo_fornecedor = fornecedores(nome=nome, email=email, telefone=telefone, endereco=endereco)
        lista_fornecedores.append(novo_fornecedor)

for fornecedor in lista_fornecedores:
    print(f"Nome: {fornecedor.nome} | Email: {fornecedor.email} | Telefone: {fornecedor.telefone} | Endereço: {fornecedor.endereco}")
