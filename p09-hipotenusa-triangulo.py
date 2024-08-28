# Calcular la hipotensusa de un rectangulo

import os
os.system("Clear")

print ("Calcular la hipotensusa de un rectangulo\n")

from math import sqrt

Cateto1 = float(input("Selecciona el cateto a:"))
Cateto2 = float(input("Selecciona el cateto b:"))

# formula de pitagoras
hipotenusa = sqrt ((Cateto1**2)+(Cateto2**2))

print(f"La Hipotenusa de triangulo es: {hipotenusa:.2f}")