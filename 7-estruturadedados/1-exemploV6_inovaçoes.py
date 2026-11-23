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

    
    def mostrar_marketing(self):
        print(f'\nNome: {self.nome}')
        print(f'Email: {self.email}')
        print('='*30)

    
    def mostrar_whatsapp(self):
        print(f'\nNome: {self.nome}')
        print(f'WhatsApp: {self.telefone}')
        print('='*30)

lista_clientes = []

print("\n=== SOLICITANDO DADOS ===")
for i in range(2):
    dados = Cliente(
        nome = input("\nDigite seu nome: "),
        telefone = input("Digite seu WhatsApp/Telefone: "),
        email = input("Digite seu email: ")
    )
    lista_clientes.append(dados)

print("\n=== LISTA PARA WHATSAPP ===")
for cliente in lista_clientes:
    cliente.mostrar_whatsapp()
