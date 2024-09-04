# Imprime numeros de 1 a 200 de 10 en 10 

import os;os.system("Clear")

print("Imprime numeros de 1 a 200 de 10 en 10\n")

c = 0

while c <= 200:
    c = c + 1
    if c % 10 != 0:
        continue
    print (c, end =  " ")