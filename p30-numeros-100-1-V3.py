# Imprime los numeros del 100 a n en decrementos de p

import os;os.system("Clear")

print("\nImprime los numeros del 100 a 1 \n")

n = int(input("Desde donde ?"))
p = int(input("Decrementos de ?"))

c = n

while c >= 1 :
    print(c, end=" ")
    c = c - p


print ("\nCiclo terminado")