from os import system
system('cls')

""" frutas = ["maçã", "banana", "laranja"]
print(frutas)
indice = frutas.index("laranja")
print(indice)
frutas.pop(indice)
print(frutas)
print("=="*30) """


frutas = ["maçã", "banana", "laranja"]
print(frutas)
remover = input("Digite a palavra para remover: ")
indice = frutas.index(remover)
frutas.pop(indice)
print(frutas)
print("=="*30)