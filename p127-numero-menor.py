# Diseñar una función que pida 3 números enteros y devuelva el menor

import os

def numero_menor():
    num1 = int(input("Ingresa un número: "))
    num2 = int(input("Ingresa un número: "))
    num3 = int(input("Ingresa un número: "))
        
    if num1 < num2 and num1 < num3:
        return num1
    elif num2 < num1 and num2 < num3:
        return num2
    else:
        return num3

# PRINCIPAL
os.system('Clear')
menor = numero_menor()

print("El número menor es:", menor)


