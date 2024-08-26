# Ejemplifica el uso de algunas funciones de la libreria math

import math as mt

w = 10.34
x = 10
y = 20
z = 35

print(f"Los numeros son : {w}, {x}, {y}, {z}")
print(f"Maximo comun divisor : {mt.gcd(x, y, z)}")
print(f"Valor maximo         : {max(x, y, z)}")
print(f"Valor minimo         : {min(x, y, z)}")
print(f"Elevar a una potencia  : {mt.pow(x, y, z)}\n")

print(f"Redondar hacia arriba   : {mt.ceil(w)}")
print(f"Redondar hacia abajo    : {mt.floor(w)}")
print(f"Redondar                : {round(w)}")
print(f"Truncar                 : {mt.trunc(w)}")


