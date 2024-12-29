#Criar um algotitmo que imprima a média aritmética 
#entre os números 8, 9 e 7

from os import system
system('cls')

print("Insira três valores, para receber a média:")

valor1 = float(input("Insira o primeiro valor: "))
valor2 = float(input("Insira o segundo valor: "))
valor3 = float(input("Insira o terceiro valor: "))
media = (valor1 + valor2 + valor3) / 3
print("A média dos três valores inseridos é: ", media)
