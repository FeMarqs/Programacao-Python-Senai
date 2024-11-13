from os import system
system('cls')

peso = int(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

imc = peso/(altura*altura)
print(f'Seu IMC é: {imc:.2f}')

imc = peso/altura*altura # deu ruim
print(f'Seu IMC é: {imc:.2f}')

imc = peso/altura**2
print(f'Seu IMC é: {imc:.2f}')