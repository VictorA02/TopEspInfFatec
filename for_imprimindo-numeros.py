import os
os.system('cls')

for i in range(5): #Começa com o número 0
    print(i)

for i in range(1,10,2): #Começa com 1 // Vai até 2 // Soma de 2 em 2
    print(i)

for i in range(10,1,-1): #Começa com 10 // Vai até 1 // Subtrai 1 em 1
    print(i)

soma = 0
for i in range(5): #Começa com 0 // Resultado de 0 até 5
    soma += i
else:
    print("Soma = %d" %soma)