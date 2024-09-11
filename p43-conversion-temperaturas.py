# Calcular la temperatura convertida de grados centígrados a grados farenheit de un rango de valores
#   Introducidos por el usuario

import os; os.system("clear")

while True:
    print("Convertir temperaturas de Celsius a Fahrenheit\n")
    temperatura_inicial = int(input("Ingresa la temperatura inicial en grados Celsius: "))
    temperatura_final = int(input("Ingresa la temperatura final en grados Celsius: "))

    if temperatura_inicial > temperatura_final:
        print("La temperatura inicial debe ser menor o igual a la temperatura final.")
        continue

    print("\nTemperaturas convertidas:")
    celsius = temperatura_inicial
    while celsius <= temperatura_final:
        fahrenheit = (9/5) * celsius + 32
        print(f"Conversion : {celsius} °C = {fahrenheit:.2f} °F")
        celsius += 1

    if input("\n\nDeceas continuar (S/N)?").upper().startswith("N"): break

print("\n\nProceso Terminado...")