# Verificar si un numero es positivo, negativo o es cero

print("Verificar si un numero es positivo, negativo o es cero: \n")

import os; os.system("clear")

numero = int(input("Dame un numero entero ?"))

if numero > 0:
    print("\nEl numero es positivo")

if numero < 0:
    print("\nEl numero es negativo")

if numero == 0:
    print("\nEl numero es cero")

print("\nProceso terminado ...")
