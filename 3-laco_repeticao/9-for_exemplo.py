import os
os.system('cls')

nota = 0
for i in range(4):
    nota += int(input('digite sua nota:'))
    media = nota / 4
print(f'a media e {media}')
