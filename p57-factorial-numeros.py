# Cual es el factorial de un numero 

import os; os.system("Clear")

n = int(input("Dame un nunmero ? "))

for x in range (n+1):
    f = 1
    print(f"{x}! = ", end=" ")
    for i in range(1, x+1):
        f = f * i
        print(f"{i} {"x" if i!=x else ""}", end= " ")
        print(f" = {f}")



