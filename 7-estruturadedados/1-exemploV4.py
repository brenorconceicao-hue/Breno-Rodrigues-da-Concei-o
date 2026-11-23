from dataclasses import dataclass
import os
os.system('cls')

@dataclass
class Cliente:
    nome: str
    idade: int
    altura: float
    peso : float
lista_clientes = []
print("SOLICITANDO DADOS DOS DOIS CLIENTES")
for i in range(2):
    dados_do_cliente = Cliente(
        nome = input('\n Digite seu nome: '),
        idade = int(input('Digite sua idade: ')),
        altura = float(input("digite sua altura: ")),
        peso = float(input("digite seu peso: "))
    )
    lista_clientes.append(dados_do_cliente)

print("\n EXIBINDO DADOS")
for cliente in lista_clientes:
    print(f'\nNome: {cliente.nome}')
    print(f'Idade: {cliente.idade}')
    print(f"altura: {cliente.altura}")
    print(f"peso: {cliente.peso}")
    print('='*15)