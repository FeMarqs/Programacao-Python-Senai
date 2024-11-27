from os import system
system('cls')

frutas = ["maçã", "banana", "laranja"]
print(frutas)
print("=="*30) #cria o "cabeçalho"
frutas.append("Kiwi")
print(frutas)
print("=="*30) #cria o "cabeçalho"
frutas.append("pitanga")
print(frutas)
aux = input("Digite uma fruta:")
frutas.append(aux)
print(frutas)