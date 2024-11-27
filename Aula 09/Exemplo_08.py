from os import system
system('cls')

texto = "Python é legal"
print(texto.startswith("Python")) #Startwith verifica se a frase começa com palavra "Python"
print(texto.endswith("Legal")) #Endswith verifica se a frase finaliza com a palava Legal com "L"
print("é" in texto) #In Verifica se a palavra especificada "é" está dentro da frase
print(texto.count("Python")) #Count conta quantas "Python" tem na frase
textoTrocado = texto.replace("legal","java") #Replace fará a troca de palavra escolhida
print(textoTrocado)

texto = "O rato roeu a roupa do rei de Roma"
print(texto.startswith("O")) #Startwith verifica se a frase começa com palavra "Python"
print(texto.endswith("Roma")) #Endswith verifica se a frase finaliza com a palava Legal com "L"
print("roupa" in texto) #In Verifica se a palavra especificada "roupa" está dentro da frase
print(texto.count("rato")) #Count conta quantas "rato" tem na frase
textoTrocado = texto.replace("rato","gato") #Replace fará a troca de palavra escolhida
print(textoTrocado)


texto = "O tempo perguntou para o tempo quanto tempo o tempo tem"
print(texto.startswith("O")) #Startwith verifica se a frase começa com palavra "O"
print(texto.endswith("tem")) #Endswith verifica se a frase finaliza com a palava Legal com "tem"
print("para" in texto) #In Verifica se a palavra especificada "é" está dentro da frase
print(texto.count("tempo")) #Count conta quantas "tempo" tem na frase
textoTrocado = texto.replace("tempo","horas") #Replace fará a troca de palavra escolhida
print(textoTrocado)
