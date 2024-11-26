from HerancaBasica_02 import Pessoa
import os
os.system('cls')

class Menina(Pessoa):
    def __init__(self, nome, idade,cpf,rg):
        self.cpf = cpf
        self.rg = rg
    def exibir(self):
        print(f'CPF:{self.cpf}, RG: {self.rg}')
        return super().exibir()

menina = Menina("Janaina","15","987654321","2589-98")
menina.exibir()