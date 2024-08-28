# Verificar si la suma de dos numeros es igual a un tercero

import os
os.system("Clear")

print("Verificar si la suma de dos numeros es igual a un tercero\n")

n1 = int(input("Dame un  numero 1 ? "))
n2 = int(input("Dame un  numero 2 ? "))
n3 = int(input("Dame un  numero 3 ? "))

if n1+n2 == n3:
    print("\nSon iguales")
else:
    print("\nson diferentes")


print("\nProceso terminado...")
