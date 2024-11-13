# Imprimir o quadrado dos números de 1 até 20

from os import system
system('cls')
import math 

i = 1

print("Imprima o quadrado dos números de 1 até 20: ")
for i in range (i, 21):
    resultado = pow(i, 2)
    print(f'{i} = {resultado}')