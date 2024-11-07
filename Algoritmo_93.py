from os import system
system('cls')
import math
# Entrar com um número e imprimir a raiz quadrada do número 
# caso ele seja positivo e o quadrado do número caso ele seja negativo

numero = float(input("Digite um número: "))

raiz = numero**(1/2)
quadrado = math.pow(numero,2)

if(numero >0):
    print(f'Raiz quadrada: {raiz}')
else:  
    print(f'Exponenciação: {quadrado}')