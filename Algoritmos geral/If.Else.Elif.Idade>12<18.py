from os import system
system('cls')

idade = int(input("Digite a idade do candidato(a): "))

if (idade >= 18):
    print("Maior de idade")
elif (idade >=12 and idade <18):
    print("juvenil")
else:
    print("infantil")
