# lista con 2 diccionarios
autos = [
    {"marca": "Ford", "modelo": "Mustang", "año": 1964},
    {"marca": "VW", "modelo": "Jetta", "año": 2015}
]

# agregar elemento al diccionario
autos.append({"marca": "Ford", "modelo": "Focus", "año": 2000})

# Mostrar todos los autos
print("\nTodos los autos:", autos, len(autos))

# Mostrar cada auto dentro de la lista de autos
print("\nCada auto dentro de los autos:\n")
for auto in autos:
    print(auto)


print("\nDatos en forma de Tabla:\n")


for k in autos[0].keys():
    print(f"{k}\t", end=" ")
print()

for auto in autos:
    for v in auto.values():
        print(f"{v}\t", end=" ")
    print()  


print("\nDatos en forma de Registro\n")
for auto in autos:
    for k, v in auto.items():
        print(f"{k:<12} : {v}")
    print(" ")  