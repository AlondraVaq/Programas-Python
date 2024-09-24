# Imprimir la secuencia de numeros mostrando el numero de renglones que usuario desee

import os

os.system("Clear")

renglones = int(input("Dame número ?  "))

for i in range(1, renglones + 1):
    print((str(i) + ' ') * i)

print("\nProceso terminado...")