import math
import os
os.system('cls')

ano = float(input("Insira um ano para descobrir seu século: "))
seculo = math.ceil(ano / 100)

print("Ano:", ano, "| Século:", seculo)