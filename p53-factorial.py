# Imprime cual es el factorial de un número

import os; os.system("Clear")

print("Imprime el factorial de un número \n")

n = int(input("Ingresa el número que deseas ? "))
f = 1
for i in range(1,n+1):
    f = f * i

print(f"\nEl factorial es: {f}")