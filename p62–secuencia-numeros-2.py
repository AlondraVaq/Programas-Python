# Imprimir una secuencia de numeros mostrando el num. de renglones que usario desee


import os

os.system("Clear")

renglones = int(input("igresa un  número ? "))

for i in range(1, renglones + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("\nProceso terminado...")