#Ler um número inteiro e imprimir seu sucessor e seu antecessor.
from os import system
system ('cls')

# Lê um número inteiro do usuário
numero = int(input("Insira um número inteiro: "))

# Calcula o sucessor e o antecessor
sucessor = numero + 1
antecessor = numero - 1

# Imprime o sucessor e o antecessor
print(f"O sucessor de {numero} é {sucessor} e o antecessor é {antecessor}.")

