import os

os.system('cls')


def metros_e_cm(metros):
  return metros * 100


metros = float(input("Digite quantos metros para converter: "))
converter = metros_e_cm(metros)

print("\nExibir dados:")
print(f"{metros} m em centímetros são {converter} cm")
