import os
os.system("cls")

nome = input("Digite o nome do produto: ")
valor = float(input("Digite o valor do produto: "))

print("Produto:", nome)
print("Valor s/ desconto:", valor)

if valor <= 0:
    print("Digite um valor aicma de 0!")

elif valor > 0 and valor < 50:
    print("Produto não tem desconto")

elif valor >= 50 and valor < 200:
    novo_valor = valor - (valor * 0.05) 
    print("Produto c/ desconto:", novo_valor)

elif valor >= 200 and valor < 500:
    novo_valor = valor - (valor * 0.06)
    print("Produto c/ desconto:", novo_valor)

elif valor >= 500 and valor < 1000:
    novo_valor = valor - (valor * 0.07)
    print("Produto c/ desconto:", novo_valor)

else:
    novo_valor = valor - (valor * 0.08)
    print("Produto c/ desconto:", novo_valor)