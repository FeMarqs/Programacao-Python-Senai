from os import system 
system('cls')

def raizCubica(numero):
    raizCubica = numero**(1/3)
    return raizCubica

resultado = 27**(1/3) #Usar **(1/3)
print(f'Raiz cubica de 27: {resultado}')

print(f'Raiz Cubica com função: {raizCubica(27)}')
