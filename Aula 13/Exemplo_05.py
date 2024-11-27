from os import system
system('cls')

frutas = ["maçã", "banana", "laranja"]
print(frutas)
print("=="*30) #cria o "cabeçalho"
frutas.insert(1,"Kiwi") #apenas muda a posição que está no 1, direcionando para a próxima posição
print(frutas)
print("=="*30)
frutas.insert(4,"Morango")
print(frutas)
print("=="*30)
frutas.insert(10,"pitanga")
print(frutas)
print("=="*30)
print(frutas[5])