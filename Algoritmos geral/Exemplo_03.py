from os import system
system('cls')

idadep = 15
alturap = 1.75
etniap = "indigena"

print("------------ Dados da candidata -------------")
print("Dados da candidata")
idade = int(input("Digite a idade da candidata: "))
altura = float(input("Digite a altura da candidata: "))
etnia = input("Digite a etnia da canditada: ")


if(idadep == idade and alturap == altura and etniap == etnia):
    print("Aprovada")
else: 
    print("Reprovada")
