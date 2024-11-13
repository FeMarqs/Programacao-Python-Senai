# Construir um algoritmo que leia dois números e efetue a adição. 
# Caso o valor somado seja maior que 20, este deverá ser apresentado 
# somando-se a ele mais 8;caso o valor somado seja menor ou igual a 20, 
# este deverá ser apresentado subtraindo-se 5.
from os import system
system('cls')

valor_01 = int(input("Digite um número: "))
valor_02 = int(input("Digite um número: "))

total = valor_01+valor_02

if(total > 20):
    total = total+8
    print(f'Total mais 8: {total}')
elif (total <=20):
    total = total-5
    print(f'Total menos 5: {total}')