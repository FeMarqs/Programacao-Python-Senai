from os import system
system('cls')

# Crinado uma função (Def)
def verificarPar(a): # Def é a definição da função (geralmente usamos no verbo primitivo, uma ação, correr, falar, andar...)
   if(a%2==0):
       print("É par")
   else:
       print("Não é par")

#------------------------------------------       
numero = int(input("Digite um número: "))
verificarPar(numero)