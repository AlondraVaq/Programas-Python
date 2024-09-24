# Imprimir numeros pares, apertir del numero 2 hasta donde el usuario lo desce y sumarlos 

import os; os.system("Clear")

num = int(input("Hasta que numero par desea ? "))

suma = 0

for i in range(2, num + 1, 2):
    print(i, end=' ')
    suma += i

print(f"La suma de los números pares es = {suma}")

print("\nProceso terminado...")