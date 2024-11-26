from os import system
system('cls')

class Animal:
    def fazer_som(self):
        print("O animal fez um um som")
  
class Gato(Animal):
    def fazer_som(self):
        print("O gato mia")

gato = Gato()
gato.fazer_som()