from os import system
system('cls')

class Calculadora:
    
    def __init__(self):
        self.total = 0
    
    def iniciarCalculadora(self):
        numero_01 = int(input("Digite um numero: "))
        numero_02 = int(input("Digete um numero: "))
        op = input("Digite a operação: ")
        
        if(op == "+"):
            self.somar(numero_01,numero_02)
        elif(op == "-"):
            self.subtrair(numero_01,numero_02)
        elif(op == "*"):
            self.multiplicar(numero_01,numero_02)
        elif(op == "/"):
            self.dividir(numero_01,numero_02)
        else:
            print("Operação Inválida")
        
    def somar(self, numero_01,numero_02):
            self.total = numero_01+numero_02
            print(f'Total: {self.total}')
        
    def subtrair(self, numero_01,numero_02):
            self.total = numero_01-numero_02
            print(f'Total: {self.total}')
        
    def multiplicar(self,numero_01,numero_02):
            self.total = numero_01*numero_02
            print(f'Total: {self.total}')
            
    def dividir(self, numero_01, numero_02):
            try:
                self.total = numero_01/numero_02
                print(f'Total: {self.total}')
            except:
                print("Valor inválido")
                
print("_="*20)
print("Calculadora")
calc=Calculadora()
calc.iniciarCalculadora()
print("_="*20)
                    
            
            
            
            
            
        