import os
os.system("cls")

#For
str1 = "João da Silva"
    #For imprimindo na vertical
for c in str1:
    print(c)
    #For imprimindo na horizontal com algum caracter entre cada letra
for c in str1:
    print(c, end=' ')

#For com posição enumerada
str1 = "João da Silva"
for pos, valor in enumerate(str1):
    print("Posição", pos, ", Valor: ", valor)