#Entrar com um número no formato CDU e imprimir 
# invertido: UDC. (Exemplo: 123, sairá 321.) 
# O número deverá ser armazenado em outra variável 
# antes de ser impresso.

from os import system
system ('cls')


# Leitura do número
numero = input("Digite um número no formato CDU: ")

# Invertendo o número
numero_invertido = numero[::-1] #Inversão da string: Utilizamos o slicing [::-1] para inverter a string. Isso funciona de maneira simples e eficiente para inverter qualquer string

# Exibição do número invertido
print(f"Número invertido: {numero_invertido}")

""" # Leitura do número
numero = input("Digite um número no formato CDU: ")

# Invertendo o número usando um laço for
numero_invertido = ""
for i in range(len(numero) - 1, -1, -1):
    numero_invertido += numero[i]

# Exibição do número invertido
print(f"Número invertido: {numero_invertido}") """



