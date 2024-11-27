# Criar um algortimo que imprima os números pares de 1 a 600.

from os import system 
system('cls')
import math

print("Imprima os números pares de 1 a 600: ")

for i in range(1, 601):
    if(i%2==0):
        print(f'{i}')