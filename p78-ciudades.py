# Nombres de ciudades: Imprimir cuantos elementos son, y la lista completa, ordenar de manera decendente.

import os; os.system('Clear')

ciudades = []


while True:
    ciudad = input("Introduce el nombre de una ciudad ($ para terminar): ")
    if ciudad == "$":
        break
    ciudades.append(ciudad)

print(f"\nNúmero de ciudades: {len(ciudades)}")
print(f"Lista de ciudades: {ciudades}")


ciudades.sort(reverse=True)
print(f"\nLista de ciudades en orden descendente: {ciudades}")


consonantes = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
ciudades_consonantes = [ciudad for ciudad in ciudades if ciudad[0] in consonantes]

print(f"\nNúmero de ciudades que empiezan con consonante: {len(ciudades_consonantes)}")
print(f"Ciudades que empiezan con consonante: {ciudades_consonantes}")