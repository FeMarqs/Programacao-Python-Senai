# Imprimir os múltiplos de 5, no intervalo de 1 até 500.

from os import system
system('cls')
import time

print("Imprima todos os números múltiplos de 5, no intervalo de 1 a 500: ")
for i in range (1,501):
    if (i%5==0):
        print(f'{i}')