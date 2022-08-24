import os
os.system("cls")

for i in range(10): #Continue - volta ao programa após o IF estar concluido.
    if (i > 5 and i < 8):
        continue
    print(i)

for i in range(10): #Break - interrompe o programa
    if (i > 5 and i < 8):
        break
    print(i)