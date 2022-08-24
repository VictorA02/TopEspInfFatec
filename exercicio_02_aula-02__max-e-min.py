import os
os.system('cls')

Re1 = float(input("Insira o valor da primeira resistência: "))
Re2 = float(input("Insira o valor da segunda resistência: "))
Re3 = float(input("Insira o valor da terceira resistência: "))
Re4 = float(input("Insira o valor da quarta resistência: "))
soma = Re1 + Re2 + Re3 + Re4
maior = max(Re1, Re2, Re3, Re4)
menor = min(Re1, Re2, Re3, Re4)

print("Primeira resistência: ", Re1)
print("Segunda resistência: ", Re2)
print("Terceira resistência: ", Re3)
print("Quarta resistência: ", Re4)
print("Resistência equivalente: ", soma)
print("Maior resistência: ", maior)
print("Menor resistência: ", menor)