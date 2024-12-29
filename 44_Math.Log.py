#Entrar com o número e a base em que se deseja 
# calcular o logaritmo desse número
#e imprimi-lo.
from os import system
system ('cls')
import math

# Leitura do número (logaritmando)
num = float(input("\nEntre com o logaritmando: "))

# Leitura da base
base = float(input("\nEntre com a base: "))

# Cálculo do logaritmo na base fornecida
logaritmo = math.log(num, base)

# Exibição do resultado
print(f"\nO logaritmo de {num} na base {base} é: {logaritmo}")
print("\n")
