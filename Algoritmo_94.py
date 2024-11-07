from os import system
system('cls')
import math
# Entrar com um número e imprimir uma das mensagens: é multiplo de 3 
# ou não é multiplo de 3.

numero = int(input("Digite um número: "))

if(numero % 3 == 0):
    print("É múltiplo de 3")
else:
    print("Não é múltiplo de 3")