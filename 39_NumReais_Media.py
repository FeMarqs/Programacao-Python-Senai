#Entrar com dois números reais e imprimir a média 
#Aritmética com a mensagem "Média" antes do resultado.
from os import system 
system ('cls')

print("Insira 2 números reais e receberá a média ")

num1 = float(input("Entre com o primeiro número: "))
num2 = float(input("Entre com o segundo número: "))
media = (num1 + num2) / 2


print(f'A média dos dois números inseridos é: ', media) 
