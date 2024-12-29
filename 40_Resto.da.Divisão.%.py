#Entrar com dois numeros inteiros e imprimir a seguinte saída:
#dividendo:
#divisor:
#quociente:
#resto:

from os import system
system ('cls')

print("Insira dois números inteiros, o prgrama apresentará o: \nDividendo\nDivisor\nQuociente\nResto")

num1 = int(input("Insira o primeiro valor (dividendo): "))
num2 = int(input("Insira o segundo valor (divisor): "))

quociente = (num1 / num2)
resto = (num1 % num2)

print(f"O Divivendo da operação é: {num1}")
print(f"O Divisor da operação é: {num2}")
print(f"O Quociente da operação é: {quociente}")
print(f"O Resto da operação é: {resto}")

