from os import system
system('cls')
import math

ponto_01 = (3,4)
ponto_02 = (6,8)

resultado = math.dist(ponto_01, ponto_02)
print(f'A distancia entre os pontos é: {resultado}')