from os import system
system('cls')

try: #Try identifica o erro, e joga para o Except para validar o erro
    x = int(input("Didite um numero: ")) #ValueError digitado um valor (letra) que não é numero
    y = 10/x #ZeroDivisionError
    print(y)
except ValueError:
    print("Erro: Você digitou um numero inválido!!!")
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero!!!")
else:
    print("Operação concluída com sucesso!!!")