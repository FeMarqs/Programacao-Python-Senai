#Entrar com um número e imprimir a seguinte saída:
#numero:
#quadrado:
#raiz quadrada:
from os import system
system ('cls')
import math

numero = float(input("Insira um número e informaremos o seu quadrado e raiz quadrada: "))

quadrado = (numero * numero)

raiz_quadrada = math.sqrt(numero)

print(f"O quadrado do número informado é: {quadrado}")

print(f"A raiz quadrada do número é: {raiz_quadrada}")