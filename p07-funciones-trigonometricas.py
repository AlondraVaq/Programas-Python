# Calcula las funciones trigonometricas sobre un angulo

print("Calcula las funciones trigonometricas sobre un angulo")

import math as mt

angulod = float(input("Dame un angulo ?"))
angulor = mt.radians(angulod)

print(f"Angulo original : {angulod} , Angulo en radianes : {angulor}")

salida = ("Resumen de funciones trigoinometricas \n"
f"Seno       :{mt.sin(angulor)}\n"
f"Coseno    :{mt.cos(angulor)}\n"
f"Tangente   :{mt.tan(angulor)}\n")

print(salida)