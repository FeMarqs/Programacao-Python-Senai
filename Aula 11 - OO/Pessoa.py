from os import system
system('cls')

class Pessoa:
    especie = "Homo sapiens"
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def apresentar(self):
        print(f"Meu nome é {self.nome} e tenho {self.idade} anos")

pessoa_01 = Pessoa("João", 30)
pessoa_02 = Pessoa("Maria", 25)

pessoa_01.apresentar()
pessoa_02.apresentar()

pessoa_01.nome="Zé"
print(pessoa_01.nome)

print(pessoa_01.especie)

pessoa_01.especie = "Qualquer coisa que vier"
print(pessoa_01.especie)