from os import system
system('cls')

idade= int(input("Digite a idade da candidata: "))
altura= float(input("Digite a altura da candidata: "))

# de 0 a 11 anos = Infantil
# de 12 a 17 anos = teen
# de 18 a 24 anos = jovem
# de 25 a 50 anos = adulto
alturaEsperada = 1.7

if (idade >= 0 and idade < 11 ):
    print("-------- Candidata aprovada ---------")
    print("-------- Categoria infantil ---------")
elif (idade >=12 and idade <= 17 and altura == alturaEsperada):
     print("-------- Candidata aprovada ---------")
     print("-------- Categoria Teen -------------")
elif (idade >17 and idade <= 24 and altura == alturaEsperada):
     print("-------- Candidata aprovada ---------")
     print("-------- Categoria Jovem ------------")
elif (idade >24 and idade <= 50 and altura == alturaEsperada):
     print("-------- Candidata aprovada ---------")
     print("-------- Categoria Jovem ------------")
else:
     print("-------- Candidata reprovada ---------")
   
   

