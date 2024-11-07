from os import system
system('cls')

nome_Vendedor = input("Digite o nome do vendedor: ")
janeiro = float(input("Digite o valor de vendas de janeiro: "))
fevereiro = float(input("Digite o valor de vendas de fevereiro: "))
marco = float(input("Digite o valor de vendas de março: "))

totalVendas = janeiro+fevereiro+marco

if(totalVendas >= 5000):
    comissao = totalVendas*0.04
    print("-------------- Resultado ----------")
    print(f'Vendedor: {nome_Vendedor} \nTotal de vendas: R$ {totalVendas} \nComissão: R${comissao}')
    
else:
    comissao = totalVendas*0.01
    print(f'Vendedor: {nome_Vendedor} \nTotal de vendas: R$ {totalVendas} \nComissão: R${comissao}')