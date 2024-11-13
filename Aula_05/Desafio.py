from os import system
system('cls')

nivel = int(input("----- Digite o nivel da mensalidade -----\n 1 - para nive I\n 2 - para nivel II\n 3 - para nivel III\n 4 - para nivel IV \n Digite: "))

if (nivel ==1):
    data = int(input("Digite a data do pagamento: "))
    if (data == 1):
        total = 51.50-(51.50*0.15)
        print(f'Valor da mensalidade: R$ {total}')
    elif (data >1 and data <=5):
        total = 51.50-(51.50*0.10)
        print(f'Valor da mensalidade: R$ {total}')
    elif (data >5 and data <=10):
        total = 51.50-(51.50*0.0385)
        print(f'Valor da mensalidade: R$ {total}')
    else:
        print("Valor da mensalidade R$ ", 51.50)
elif (nivel ==2):
    data = int(input("Digite a data do pagamento: "))
    if (data == 1):
        total = 65.00-(65.00*0.15)
        print(f'Valor da mensalidade: R${total}')
    elif (data >1 and data <=5):
        total = 65.00-(65.00*0.10)
        print(f'Valor da mensalidade: R${total}')
    elif (data >5 and data <=10):
        total = 65.00-(65.00*0.0385)
        print(f'Valor da mensalidade: R${total}')
    else:
        print("Valor da mensalidade R$", 65.00)
elif (nivel ==3):
    data = int(input("Digite a data do pagamento: "))
    if (data == 1):
        total = 80.00-(80.00*0.15)
        print(f'Valor da mensalidade:R$ {total}')
    elif (data >1 and data <=5):
        total = 80.00-(80.00*0.10)
        print(f'Valor da mensalidade: R${total}')
    elif (data >5 and data <=10):
        total = 80.00-(80.00*0.0385)
        print(f'Valor da mensalidade:R$ {total}')
    else:
        print("Valor da mensalidade R$", 80.00)
elif (nivel ==4):
    data = int(input("Digite a data do pagamento: "))
    if (data == 1):
        total = 100.00-(100.00*0.15)
        print(f'Valor da mensalidade:R$ {total}')
    elif (data >1 and data <=5):
        total = 100.00-(100.00*0.10)
        print(f'Valor da mensalidade: R${total}')
    elif (data >5 and data <=10):
        total = 100.00-(100.00*0.0385)
        print(f'Valor da mensalidade: R${total}')
    else:
        print("Valor da mensalidade R$", 100.00)
else:
    print("Nivel inválido")