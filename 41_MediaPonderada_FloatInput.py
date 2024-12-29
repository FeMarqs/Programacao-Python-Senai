#Entrar com quatro números e imprimir a média
#  ponderada, sabendo-se que os pesos são 
# respectivamente: 1, 2, 3 e 4.

from os import system
system ('cls')

print("Informe 4 números, informaremos a média ponderada, sabendo-se que os pesos são respectivamente: 1, 2, 3, 4")

num1 = float(input("Insira o primerio número: "))
num2 = float(input("Insira o segundo número: "))
num3 = float(input("Insira o terceiro número: "))
num4 = float(input("Insira o quarto número: "))

peso1 = 1
peso2 = 2
peso3 = 3
peso4 = 4

media_ponderada = ((num1*peso1) + (num2*peso2) + (num3*peso3) + (num4*peso4)) / (peso1 + peso2 + peso3 + peso4)

print(f"A Média Ponderada dos valores informados é: ", media_ponderada) 

#for i in range(4):
#    numero = int(input("Digite um número: "))




