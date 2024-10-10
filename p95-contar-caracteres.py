# Crear un diccionario donde la llave es el carácter y el valor el número de veces que aparece

import os; os.system("Clear")

cadena = input("Escribe una cadena: ")

contador = {}

for caracter in cadena:
    if caracter in contador:
            contador[caracter] += 1
    else:
            contador[caracter] = 1
            
print(contador)