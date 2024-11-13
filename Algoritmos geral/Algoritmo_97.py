from os import system
system('cls')
import math
# Entrar com um número e informar se ele é
# divisível por 10, por 5, por 2 ou se não é 
# divisível por nenhum destes.

numero = float(input("Digite um número: "))

if(numero % 10 ==0 and numero % 5 ==0 and numero % 2 ==0):
    print("O número é divisível por 10, por 5 e por 2")
else:
    print("O número não é divisível por 10, 5 nem por 2")
