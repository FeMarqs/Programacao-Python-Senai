# Fórmula de juros compostos A = P*(1+R/N)^(N*T)
# p = 1000 #(valor Principal)
# r = 5% # é juros por ano
# n = 12 # (meses)
# t = 5 # anos

from os import system
system('cls')
import math

p = 160000 #(valor Principal)
r = 0.05 # é juros por ano
n = 12 # (meses)
t = 30 # anos

a = p*(1+r/n)**(n*t)
print(f' O valor final com juros compostos: {a:.2f}')