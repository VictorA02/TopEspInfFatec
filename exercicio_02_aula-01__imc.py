import os
os.system("cls")

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = (peso / pow(altura, 2))
print("O seu IMC é de ", round(imc, 3))

if imc < 18.5:
    print(f"Magreza")
elif imc > 18.5 and imc < 24.9:
    print(f"Normal")
elif imc > 24.9 and imc < 29.9:
    print(f"Sobrepeso")
elif imc > 29.9 and imc < 39.9:
    print(f"Obesidade")
else:
    print(f"Obesidade Grave")