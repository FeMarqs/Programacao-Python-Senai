from os import system
system('cls')
import time
import math

def calculadora(operacao, valor1, valor2):
    match operacao:
        case "1":
            resultado = valor1 + valor2
            print(f"\nO resultado da sua soma é: {resultado}")
        case "2":
            resultado = valor1 - valor2
            print(f"\nO resultado da sua subtração é: {resultado}")
        case "3":
            resultado = valor1 * valor2
            print(f"\nO resultado da sua multiplicação é: {resultado}")
        case "4":
            if valor2 == 0:
                print("Divisão por zero não é permitido.")
            else:
                resultado = valor1 / valor2
                print(f"\nO resultado da divisão é: {resultado}")
        case "5":
            resultado = valor1**valor2
            if resultado >= 0:
                raiz2 = math.sqrt(valor1)
                print(f'\nA raiz quadrada de {valor1} é: {raiz2:.2f}')
            else:
                print("A raiz quadrada de um número negativo não é um número real")
                return None
        case():
            print("Opção inválida.")
    return None