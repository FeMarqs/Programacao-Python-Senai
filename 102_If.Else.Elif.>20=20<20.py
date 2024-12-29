from os import system 
system('cls')

# Entrar com um número e imprimir uma das mensagens:
#maior do que 20, igual a 20 ou menor do que 20.

numero = int(input("Insira um valor: "))

if(numero > 20):
    print("O número inserido é maior que 20!")
elif(numero < 20):
    print("O número inserido é menor que 20!")
else:
    print("o número inserido é igual a 20!")
