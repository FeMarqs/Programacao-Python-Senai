from os import system
system('cls')

#Criando um dicionário
dicionario = {'nome':'João','idade': 21,'cidade':'São Paulo'}
print(dicionario)

#verificando se existe uma determinada chave
if 'nome' in dicionario:
    print("A chave 'nome' existe.")

#Usando o metodo get() para retornar um valor
idade = dicionario.get('idade')
print

#Método keys() para acessar as chaves
chaves = dicionario.keys()
print(chaves)

#Método values() para acessar os valores
valores = dicionario.values()
print(valores)

#verificando se existe uma determinada chave com input

#Usando o método get() para retornar um valor
idade = dicionario.get('idade')

#Método keys() para acessar as chaves
chaves = dicionario.keys()
print(chaves)

#Método values() para acessar os valores
valores = dicionario.values()
print(valores)

