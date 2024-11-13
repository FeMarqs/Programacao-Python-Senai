#Entrar com um número e imprimi-ló caso seja maior que 20.

from os import system
system('cls')

numero = int(input("Digite um número: "))

if (numero >= 20):
    print(f'Número: {numero}')