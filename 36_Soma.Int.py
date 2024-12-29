#Ler dois números e imprimir a soma.
#Antes do resultado, deverá aparecer a mensagem: Soma

from os import system
system ('cls')

print("Programa para somar dois valores")

num1 = int(input("Insira o primeiro valor: "))
num2 = int(input("Insira o segundo valor: "))
soma = (num1 + num2)
print("Soma: ", soma)
