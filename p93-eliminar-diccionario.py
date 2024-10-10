# Cree un diccionario de llave de cadena municipios, mostrarlo y eleiminar elementos.

import os; os.system('Clear')

municipios = {
    "Apozol": 1863,
    "Calera": 1868,
    "Fresnillo": 1554,
    "Guadalupe": 1821,
    "Jalpa": 1824,
    "Jerez": 1824,
    "Loreto": 1931,
    "Mazapil": 1824,
    "Momax": 1857
}

# Mostrar el diccionario
print("Diccionario de municipios:")
print(municipios)

del municipios["Apozol"]
print("Después de eliminar Apozol:", municipios)


fresnillo_value = municipios.pop("Fresnillo")
print("Después de eliminar Fresnillo:", municipios)

# Eliminar la llave 
momax_item = municipios.popitem()
print("Después de eliminar Momax:", municipios)

# Borrar todos los elementos 
municipios.clear()
print("Después de borrar todos los elementos:", municipios)

# Mostrar diccionario final
print("Diccionario completo:")
print(municipios)