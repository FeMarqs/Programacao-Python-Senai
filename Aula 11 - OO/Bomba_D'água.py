from os import system
system('cls')
import time

class Bomba:
    def __init__(self):
        self.status = False
    
    def ligar(self):
        print("Bomba Ligada")
        self.status = True
        for i in range(5,0,-1):
            print(f'Tempo restante {i}')
            time.sleep(1)
    def desligar(self):
        print("Atenção bomba desligada!")
        self.status = False
bomba = Bomba()
op = input("Deseja ligar a bomba? ")
if (op.upper() == "S"):
    bomba.ligar()
bomba.desligar()