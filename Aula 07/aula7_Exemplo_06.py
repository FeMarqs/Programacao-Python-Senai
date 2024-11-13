from os import system
system('cls')
import time

soma = 0 

while (True):
    num = int(input("Digite um número: "))
    if (num <0):
        break
    soma += num
print(f'A soma dos números é: {soma}')