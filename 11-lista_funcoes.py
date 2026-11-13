import os 
os.system('cls')

def metros_e_cm():
    return metros*100
metros= float(input("digite quantos metros pra converter: "))

converter = metros_e_cm(metros)

print("\n exibir dados ")
print(f'{metros} em centimetros {converter}')