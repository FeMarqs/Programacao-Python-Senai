from os import system
system('cls')
import math

#Ler um número inteiro de 3 decimais e imprimir 
#se o algorismo da casa das centenas é par ou ímpar

numero = int(input("Digite um número inteiro com 3 decimais: "))

if(numero % 2 ==0):
    print("O número inserido é par")
else:
    print("O número inserido é impar")
