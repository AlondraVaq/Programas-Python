# Crear un diccionario de llaves de cadena países y mostrar el diccionario y modificar elementos.

import os; os.system('Clear')

paises = {
    "Argentina": 100,
    "Brasil": 200,
    "Colombia": 300,
    "Chile": 400,
    "Ecuador": 500,
    "Bolivia": 600,
    "Jamaica": 700
}

# Mostrar el diccionario
print("Diccionario de países:")
print("paises")

paises["Brasil"] = 250
print("Después de modificar Brasil:", paises)

paises["Chile"] = 450
print("Después de modificar Chile:", paises)

paises.update({"Bolivia": 650})
print("Después de modificar Bolivia:", paises)

paises.update({"Jamaica": 750})
print("Después de modificar Jamaica:", paises)

# Mostrar el diccionario modificado
print("\nDiccionario modificado:")

for key, value in paises.items():
    print(f"{key}: {value}")