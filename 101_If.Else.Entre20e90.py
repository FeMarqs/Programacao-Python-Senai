from os import system
system('cls')

# Construir um algoritmo que indique se o número digitado 
# está compreendido entre 20 e 90 ou não.

numero = int(input("Digite um valor: "))

if(numero >= 20 and numero <= 90):
    print("O valor digitado está entre os números 20 e 90")
else:
    print("O valor digitado está fora do limite entre os números 20 e 90")
