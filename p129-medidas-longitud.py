# Diseña dos funciones que convierta: pulgadas a centímetros y metros a pies.

import os
def pulgadas_a_centimetros(pulgadas):
    return pulgadas * 2.54

def metros_a_pies(metros):
    return metros * 3.281

# PRINCIPAL
os.system('Clear')
while True:
    print("\nCONVERSION DE UNIDADES ")
    print("[1] Convertir pulgadas a centímetros")
    print("[2] Convertir metros a pies")
    print("[3] Salir")

    opcion = int(input("\nElige una de las 3 opciones: "))

    if opcion == 1:
        pulgadas = float(input("Ingresa las pulgadas: "))
        cm = pulgadas_a_centimetros(pulgadas)
        print(f"\n{pulgadas} pulgadas son {cm:.4f} centímetros")
    elif opcion == 2:
        metros = float(input("Ingresa los metros: "))
        pies = metros_a_pies(metros)
        print(f"\n{metros} metros son {pies:.4f} pies")
    elif opcion == 3:
        print("Salir")
        break
    else:
        print("Error, elige entre 1 y 3.")

