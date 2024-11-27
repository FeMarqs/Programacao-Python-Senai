from os import system
system('cls')

#Criar uma lista de números. Crie uma lista chamada números 
#contendo os números 10 a 20 (inclusive). Imprima a lista.

""" numeros = [10, 11, 12, 13, 14, 15, 16, 17 , 18 , 19 , 20]
print(numeros) """

numeros = []

for i in range(10, 21):
    numeros.append(i) #adciona o número à lista 
    print(i) #imprime o número durante o loop
    
#após o loop, imprime a lista inteira
print("Lista completa de números de 10 a 20:", numeros)



