from os import system
system('cls')
import time

i=1

while (i<=10):
    if (i % 2 == 0):
        print(f'{i} é um número par')
    else:
        print(f'{i} é um número ímpar')
        time.sleep(2)
    i+=1
print("Fim do Loop")