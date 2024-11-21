from os import system
system('cls')

class Retangulo:
    def __init__(self,largura,altura):
        self.largura = largura
        self.altura = altura 
        
    def area(self):
        return self.altura * self.largura
    
largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))
    
retangulo = Retangulo(largura,altura)
print(f"A area do retangulo é: {retangulo.area()}")
    
retangulo = Retangulo(5,3)
print(f"A area do retangulo é: {retangulo.area()}")
    
   
    