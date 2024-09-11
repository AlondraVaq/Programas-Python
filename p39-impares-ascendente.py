# Imprimir los números impares de forma acendente y sumarlos 

import os; os.system("clear")

print("Imprimir los números impares de forma acendente y sumarlos\n")

while True:
    try:
        n = int(input("Ingrese un número impar ? "))
        if n <= 0:
            print("Por favor, ingrese un número impar.")
            continue
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número impar.")
        continue

    suma = 0
    i = 1
    while i <= n:
        print(i, end=' ')
        suma += i
        i += 2


    print(f"La suma de los números impares es: {suma}")

    if input("\n\nDeceas continuar (S/N)?").upper().startswith("N"): break

print("\n\nProceso Terminado...")