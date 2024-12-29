#Ler nome, endereço e telefone e imrpimí-los.
from os import system
system ('cls')

nome = input("Insira um nome: ")
endereco = input("Insira um endereço: ")
telefone = int(input("Insira um telefone: "))

print(f"As informações inseridas foram: {nome}, {endereco} e {telefone}")

resultado = nome, endereco, telefone
print("As informações inseridas foram: ", resultado)