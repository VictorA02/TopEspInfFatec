# For - programa de operações matemáticas
import os
os.system("cls")

n1 = float(input("Insira um número: "))
n2 = float(input("Insira outro número: "))
operation = input("Digite a operação desejada (+ adição, - subtração, * multiplicação, / divisão): ")

if operation == '+':
    print("O resultado da soma é", n1 + n2)

elif operation == '-':
    if n1 > n2: 
        print("O resultado da subtração é", n1 - n2)
    else:
        print("O resultado da subtração é", n2 - n1)

elif operation == '*':
    print("O resultado da multiplicação é", n1 * n2)

elif operation == '/':
    if n2 != 0:
        print("O resultado da divisão é", n1 / n2)
    else:
        print("Divisão por zero inválida!")
        
else:
    print("Operação inválida")