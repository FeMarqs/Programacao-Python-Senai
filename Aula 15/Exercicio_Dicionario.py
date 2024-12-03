from os import system
system('cls')

#Criando um dicionário
dicionario = {'nome':'João','idade': 21,'cidade':'São Paulo'}
chave = input("digite a chave para localizar: ")
if chave in dicionario:
    print(f"A chave {chave} existe.")
else:
    print(f"A chave {chave} não existe.")