import os
os.system('cls')

numero = int(input("Digite o número para ver sua tabuada: "))
i = 1

for i in range(10):
    print(numero, "x", i, "=", numero * i)
    i += i