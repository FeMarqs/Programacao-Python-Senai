from os import system
system('cls')
import time

texto = "senai"

cont = 0

for letra in texto:
    cont+=1

print(f'O texto tem {cont} caracteres.')