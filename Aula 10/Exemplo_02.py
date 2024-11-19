from os import system
system('cls')

#Criando uma função
def pedirCalcular():
    numero = int(input("Digite um valor: "))
    total = numero*2
    print(total)
pedirCalcular()