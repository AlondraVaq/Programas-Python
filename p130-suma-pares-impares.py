# Función que reciba tres parámetros: dos números (un rango), una letra P o I 
# Regrese la suma de números pares o impares en el rango de números especificados

import os
os.systema('Clear')

def suma_pares_impares(inicio, fin, tipo):
    suma = 0
    for numero in range(inicio, fin + 1):
        if tipo.upper() == 'P' and numero % 2 == 0:
            suma += numero
        elif tipo.upper() == 'I' and numero % 2 != 0:
            suma += numero
    return suma

def main():
    while True:
        print("\nOpciones:")
        print("[1] Sumar números pares en un rango")
        print("[2] Sumar números impares en un rango")
        print("[3] Salir")

        opcion = input("Selecciona una opción [1-3]: ")

        if opcion in ['1', '2']:
            inicio = int(input("Ingresa el número inicial del rango: "))
            fin = int(input("Ingresa el número final del rango: "))
            tipo = 'P' if opcion == '1' else 'I'

            resultado = suma_pares_impares(inicio, fin, tipo)
            tipo_str = "pares" if tipo == 'P' else "impares"
            print(f"La suma de los números {tipo_str} en el rango de {inicio} a {fin} es: {resultado}")
        
        elif opcion == '3':
            print("Saliendo...")
            break
        
        else:
            print("Error. Por favor, elige entre 1 y 3.")


