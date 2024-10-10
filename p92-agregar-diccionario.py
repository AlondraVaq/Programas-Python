# Crear un diccionario de llave de cadena, ventas y mostrar diccionario y agrergar elementos

import os; os.system('Clear')

ventas = {
    "Juan": 1550,
    "Jose": 2600,
    "Maria": 2220
}


print("Diccionario de ventas:" )
print (ventas)


ventas["Rocio"] = 2500
print("Después de agregar a Rocio:", ventas)


ventas["Mateo"] = 1567
print("Después de agregar a Mateo:", ventas)


ventas.update({"Andrea": 9567})
print("Después de agregar a Andrea:", ventas)


ventas.update({"Miguel": 1234})
print("Después de agregar a Miguel:", ventas)

# Mostrar el diccionario completo 
print("Diccionario actualizado:", ventas)

for key, value in ventas.items():
    print(f"{key}: {value}")