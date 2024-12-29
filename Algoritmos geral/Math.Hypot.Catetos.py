from os import system
system('cls')
import math

cateto_01 = 3
cateto_02 = 4

resultado = math.hypot(cateto_01,cateto_02)
print(f'Hipotenusa de um triangulo com catetos 3 e 4: {resultado}')
