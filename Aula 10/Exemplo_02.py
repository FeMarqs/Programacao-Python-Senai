from os import system
system('cls')

#Criando uma função (sem retorno)
def pedirCalcular():
    numero = int(input("Digite um valor: "))
    total = numero*2
    print(total)
pedirCalcular()