# Convertir temperatura de grados Celcius a grados Farenheit

import os
os.system("Clear")

print("Convertir temperatura de grados Celcius a grados Farenheit\n")

celsius = float(input("Introduce la temperatura en grados Celsius: "))

fahrenheit = (celsius * 9/5) + 32


print(f"{celsius} grados Celsius equivalen a {fahrenheit:.2f} grados Fahrenheit.")