# Imprimir todos os números de 100 até 1

from os import system
system('cls')
import time

""" i = 100
while (i>=1):
    print(f'Volta: {i}')
    time.sleep(0.3)
    i-=1 """
    
for i in range (100, 0, -1):
    print(f'{i}')