from os import system
system('cls')

class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    def andar(self, estado):
        if(estado == True):
            print("posso andar")
        else:
            print("Não posso andar")
    def exibir(self):
        print(f'Nome: {self.nome}, idade: {self.idade}')
            
class Menino(Pessoa):
    def __init__(self, nome, idade,cpf,rg):
        super().__init__(nome,idade)
        self.cpf = cpf
        self.rg = rg
    def exibir(self):
        print(f'Nome: {self.nome}, idade: {self.idade}')
        print(f'CPF: {self.cpf}, RG: {self.rg}')

menino = Menino("João","12","123.456789/09","2345678-02")
menino.exibir()
menino.andar(True)

