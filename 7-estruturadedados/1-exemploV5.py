from dataclasses import dataclass
import os
os.system("cls")

@dataclass
class Cliente:
    nome: str
    telefone: str
    email: str


lista_clientes = []

print("== CADASTRANDO DADOS ==")
dados_do_cliente = Cliente(
    nome = input('\nDigite seu nome: '),
    telefone = input("Digite seu número de telefone: "),
    email = input("Digite seu email: ")
)

lista_clientes.append(dados_do_cliente)

print("\n== EXIBINDO DADOS ==")
for cliente in lista_clientes:
    print(f'\nNome: {cliente.nome}')
    print(f'Telefone: {cliente.telefone}')
    print(f'Email: {cliente.email}')
    print('='*15)
