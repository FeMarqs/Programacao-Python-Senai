#Fazer um algoritmo que possa entrar com o saldo 
#de uma aplicação e imprima o
#novo saldo, considerando o reajuste de 1%.

from os import system
system ('cls')
import math

print("Informe o saldo e receba o novo saldo com reajuste de 1% ")

saldo_atual = float(input("Informe o saldo atual: "))

novo_saldo = (saldo_atual * 1.01)

print(f"O novo saldo é: {novo_saldo}")