from os import system
system('cls')

# maior 7 = aprovado
# entre 5 e menor que 7 = recuperação
# menor que 5 = reprovado

media = 5

if(media >=7 ):
    print("Aprovado")
elif (media >=5 and media <7):
    print("Recuperação")
else:
    print("Reprovado")
