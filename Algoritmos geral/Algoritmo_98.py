from os import system
system('cls')
import math

""" A prefeitura do Rio de Janeiro abriu uma linha
de crédito para os funcionários estatutários.
O valor máximo da prestação não poderá ultrapassar 
30% do salário bruto. Fazer um algoritmo que permita 
entrar com o salário bruto e o valor da prestação e informar
se o empréstimo pode ou não ser concedido. """

salario = float(input("Digite o seu salário: "))
prestacao = float(input("Digite o valor da prestação: "))

if(prestacao <= 0.3 * salario):
    print("O empréstimo foi concedido")
else:
    print("Empréstimo foi negado.")