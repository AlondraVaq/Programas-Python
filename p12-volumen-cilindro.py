# Calcular el volumen que hay en un cilindro

import math

print("Calcular el volumen que hay en un cilindro\n")

radio = float(input("Dame el valor del radio: "))

altura = float(input("Dame el valor de la altura: "))

Volumen = math.pi * (radio * radio) * altura

print(f"El volumen del cilindro es: {Volumen:.3f} cm^3")

