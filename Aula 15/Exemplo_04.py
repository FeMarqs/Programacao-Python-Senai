from os import system
system('cls')

tupla = (3.14, 0.45, 8, 9)
print(tupla[2])

print(tupla)

tupla2 = list(tupla)
tupla2[0]=10
tupla=tuple(tupla2)
print(tupla)
