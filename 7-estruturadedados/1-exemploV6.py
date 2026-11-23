from dataclasses import dataclass
import os
os.system("cls")

@dataclass
class Cliente:
    nome: str
    telefone: str
    email: str

    def mostrar_dados(self):
        print(f'\nNome: {self.nome}')
        print(f'Telefone: {self.telefone}')
        print(f'Email: {self.email}')
        print('='*30)

lista_clientes = []

print("\n === SOLICITANDO DADOS ===")
for i in range(2):
    dados = Cliente(
        nome = input("Digite seu nome: "),
        telefone = input("Digite seu telefone: "),
        email = input("Digite seu email: ")
    )
    lista_clientes.append(dados)

print("\n=== EXIBINDO DADOS ===")
for cliente in lista_clientes:
    cliente.mostrar_dados()
