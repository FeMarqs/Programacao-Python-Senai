from os import system
system('cls')
import time

i = 1
soma = 0

while (i<=5):
    #soma = soma +1
    soma +=i
    print("volta: ",i)
    time.sleep(3)
    i+=1
print("Soma dos números: ",soma)