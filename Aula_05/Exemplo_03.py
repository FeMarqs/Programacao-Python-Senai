from os import system
system('cls')

nota_01 = float(input("Digite a nota"))
nota_02 = float(input("Digite a nota"))
nota_03 = float(input("Digite a nota"))
nota_04 = float(input("Digite a nota"))

media = (nota_01+nota_02+nota_03+nota_04)/4

if(media >= 7):
    print("Aluno aprovado")
else:
    print("Alunor reprovado")