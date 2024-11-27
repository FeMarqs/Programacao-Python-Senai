from os import system
system('cls')

frutas = ["maçã", "banana", "laranja"]
print(frutas)
print("=="*30) #cria o "cabeçalho"
frutas.remove("maçã") #remove o item da posição
print(frutas)
print("=="*30)
frutas.insert(0,"maça")
print(frutas)
print("=="*30)

