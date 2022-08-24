import os
os.system("cls")

preco = float(input("Insira o valor do produto que vai sofrer reajuste: "))
preco_novo = preco * 1.12
print("O novo preço do produto é: %.2f" %preco_novo)