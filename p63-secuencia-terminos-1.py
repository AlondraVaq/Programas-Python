# Imprimoir la secuencia de numeros armonicos el num. de reglones que usuario desee y su suma

import os

os.system("Clear")

import math

n = int(input("Hasta que términos desea ? "))
suma = 0


print("Secuencia de terminos : ", end="")
for i in range(1, n + 1):
    termino = 1 / math.factorial(i)  
    suma += termino
    
    
    if i == n:
        print(f"1/{i}!", end=" ")
        
    else:
        print(f"1/{i}! + ", end=" ")


print(f", suma: {suma}")

print("\nProceso terminado...")