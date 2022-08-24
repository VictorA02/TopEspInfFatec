import decimal
import os
os.system("cls")

#Decimal - muitas casas decimais
x = 23
y = 1.05
d = decimal.Decimal(23) / decimal.Decimal("1.05")

print(x/y)
print(d)