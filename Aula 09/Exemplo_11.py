from os import system
system('cls')

lista = [1,2,3]

try:
    print(lista[0]) #Poisção 0 do vetor, igual a 1
except IndexError:
    print("Erro: Índice fora do intervalo")    