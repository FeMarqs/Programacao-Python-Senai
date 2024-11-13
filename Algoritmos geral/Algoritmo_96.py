from os import system 
system('cls')
import math
# Entrar com um número e informar se ele é divisível por 3 e por 7.

numero = float(input("Digite um número: "))

if(numero % 3 ==0 and numero % 7 ==0):
    print("O número é divisível por 3 e por 7")
else:
    print("O número não é divisível por 3 nem por 7.")

