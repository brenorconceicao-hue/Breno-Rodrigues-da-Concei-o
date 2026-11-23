from dataclasses import dataclass
import os
os.system('cls')

@dataclass
class cliente:
    #variavel
    nome: str
    idade: int

# SOLICITANDO DADOS DE UM CLIENTE

cliente1 = cliente('Marta' , 30)
idade = 30


#SOLICITANDO DADOS DE OUTRO CLIENTE

nome = 'Jose'
idade = 40
cliente2 = cliente('Jose' , 40)

print(f'\n nome: {cliente1.nome}')
print(f'\n idade: {cliente1.idade}')

print(f"\n nome: {cliente2.nome}")
print(f"\n idade: {cliente2.idade}")