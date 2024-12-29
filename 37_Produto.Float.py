#Ler dois números inteiros e imprimir o produto
from os import system
system ('cls')

print("Informe dois números para obter um produto")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo valor: "))

produto = (num1 * num2)

print(f"O produto do número {num1} multiplicando o número {num2} é: {produto}")
