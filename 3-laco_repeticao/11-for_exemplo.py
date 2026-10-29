import os 
os.system('cls')

nota = 0

for i in range(3):
    nota += float(input('digite sua nota:'))
    media = nota / 3
if media >= 7:
        print('aprovado')
else:
    media <= 4
    print('reprovado')

print(f'a media e {media}')

