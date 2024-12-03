from os import system
system('cls')

dicionario = {'nome':'João','idade':21, 'cidade':'São Paulo' }
dicionario2 = {'email':'joao@exemplo.com'}

dicionario.update(dicionario2)
print(dicionario)

dicionarioComposto = {('nome', 'sobrenome'):'João da Silva', 'idade':25}
print(dicionarioComposto)

dicionario.clear()
print(dicionario)