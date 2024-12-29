from os import system
system('cls')
import math

# Ler um número inteiro de 4 casas e imprimir se é ou não 
# múltiplo de quatro o número formado pelos algarismos
# que estão nas casas das unidades de milhar

numero = int(input("Digite um número de 4 dígitos: "))

if(numero % 4 ==0):
    print("O valor digitado é múltiplo de 4")
else:
    print("O valor digitado não é múltiplo de 4")
