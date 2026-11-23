from dataclasses import dataclass
import os
os.system('cls')


@dataclass
class Cliente:
    nome: str
    idade: int

lista_clientes = []


lista_clientes.append(Cliente(nome='Marta',idade= 30))
lista_clientes.append(Cliente(nome='Jose', idade=40))


for cliente in lista_clientes:
    print(f'\nNome: {cliente.nome}')
    print(f'Idade: {cliente.idade}')
    print('='*15)