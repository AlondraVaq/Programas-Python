# Imprinme los numeros de 1 hasta donde el usuario desce, de 10 en 10

import os; os.system("Clear")

n = int(input("Hasta que numero desea llegar ? "))  

for i in range(1, n, 10):
    print(i, end=' ')


print("\nProceso terminado...")
