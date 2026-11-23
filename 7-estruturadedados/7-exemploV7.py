from dataclasses import dataclass
import os
os.system('cls')

@dataclass
class Paciente:
    nome: str
    idade: int
    telefone: str
    endereco: str

    def mostrar_tudo(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Telefone: {self.telefone}")
        print(f"Endereço: {self.endereco}")
        print('='*20)

    def mostrar_nome_idade(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print('='*20)

    def mostrar_nome_telefone(self):
        print(f"Nome: {self.nome}")
        print(f"Telefone: {self.telefone}")
        print('='*20)

lista_pacientes = []

print("\n== SOLICITANDO DADOS ==")
for i in range(2):
    dados = Paciente(
        nome = input("\nDigite o nome do paciente: "),
        idade = int(input("Digite sua idade: ")),
        telefone = input("Digite seu telefone: "),
        endereco = input("Digite seu endereço: ")
    )
    lista_pacientes.append(dados)

print("\n== TODOS OS DADOS ==")
for paciente in lista_pacientes:
    paciente.mostrar_tudo()

print("\n== NOME E IDADE ==")
for paciente in lista_pacientes:
    paciente.mostrar_nome_idade()

print("\n== NOME E TELEFONE ==")
for paciente in lista_pacientes:
    paciente.mostrar_nome_telefone()
