# Construir um algoritmo que leia dois valores numéricos inteiros 
# e efetue a adição; caso o resultado seja maior que 10, apresentá-lo.
from os import system
system('cls')

valor_01 = int(input("Digite um número: "))
valor_02 = int(input("Digite um número: "))
total = valor_01+valor_02

if(total>10):
    print(f'Total: {total}')