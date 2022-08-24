import os
os.system("cls")

#Entrada de dados
num1 = float(input("Informe o primeiro valor: "))
num2 = float(input("Informe o segundo valor: "))
soma = num1 + num2

#Saída de dados usando %.2f para ARREDONDAR e inserir casas decimais de 0
print("Soma dos dois números é: %.2f" %soma)