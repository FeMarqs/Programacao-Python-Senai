from os import system
system('cls')
import math
# Entrar com um número e informar se ele é ou não divisível por 5.

numero = float(input("Digite um número: "))

if(numero % 5 ==0):
    print("É divisível por 5")
else:
    print("Não é divisível por 5")
