#Entrar com um número e imprimir o logaritmo 
# desse número na base 10.

from os import system
system ('cls')
import math

# Leitura do número
num = float(input("\nEntre com o logaritmando: "))

# Cálculo do logaritmo na base 10
logaritmo = math.log(num, 10)

# Exibição do resultado
print("\nLogaritmo:", logaritmo)
print("\n")
