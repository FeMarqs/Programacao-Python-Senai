# Criar um algortimo que imprima todos os números de 1 até 100 e a soma deles.

from os import system
system('cls')
import math

i = 1
soma = 0

print("Imprima todos os números de 1 até 100 e some tudo: ")
for i in range(i, 101):
    soma +=i
    print(f'{i}+{soma}')