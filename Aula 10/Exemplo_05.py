from os import system
system('cls')

# Definindo as funções

def somar(a,b):
    total = a+b
    print("Total: ",total)
    
def subtrair(a,b):
    total = a-b
    print("Total: ",total)
    
def multiplicar(a,b):
    total = a*b
    print("Total: ",total)

def dividir(a:float, b:float):
    try:
        total = a/b
        print("Total: ",total)
    except:
        print("Erro na divisão")
        
def escolherOperacao(op,a,b):
    if(op=="+"):
        somar(a,b)
    elif (op == "-"):
        subtrair(a,b)
    elif (op == "*"):
        multiplicar(a,b)
    elif (op == "/"):
        dividir(a,b)
    else:
        print("Operação Inválida")
    
#------------------------------------------ 
valor_01 = int(input("Digite um valor: "))
valor_02 = int(input("Digite um valor: "))

op = input("Escolha a operação: ")
escolherOperacao(op,valor_01,valor_02)