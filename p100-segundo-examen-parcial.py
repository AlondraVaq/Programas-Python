# SEGUNDO EXAMEN PARCIAL 
# Procesar empleados de una empresa de muebles lo cual se requiere:
# Solicitar algunos datos al usuario : nombre, edad, sexo, pasatiempos, sueldo
# Almacenar en una lista los datos del empleado (diccionario) e imprimir 

import os; os.system('clear')

print("Mubleria Dico")
print("Procesamiento de Empleados : ")


print("Captura de datos de empleados:")
print("Pulsa * para terminar")

empleados = []

while True:
    nombre = input("Nombre: ")
    if nombre == "*": 
        break



    edad = int(input("Edad: "))
    sexo = input("Sexo (H/M): ").lower()
    sueldo = float(input("Sueldo: "))
    pasatiempo = input("Pasatiempos (separados por coma y espacio): ").lower().split(", ")

    empleado = {
        "Nombre": nombre,
        "Edad": edad,
        "Sexo": sexo,
        "Sueldo": sueldo,
        "Pasatiempos": pasatiempo
    }
empleados.append(empleado)
print()

# Datos tabulados
print("\nTabla de datos:")

for X in empleados[0].keys():
    print(f"{X:<10}", end="")
print()

for K in empleados:
    nombre = K['Nombre']
    edad = K['Edad']
    sexo = K ['Sexo']
    sueldo = K['Sueldo']
    pasatiempo = ', '.join(K['Pasatiempos'])
    print(f"{nombre:<10} {edad:<10} {sexo:<10} {sueldo:<10,.3f} {pasatiempo}")
print()

numH = sum(1 for e in empleados if e['Sexo'] == 'H')
numM = sum(1 for e in empleados if e['Sexo'] == 'M')

pasatisum = {}
for empleado in empleados:
    for pasatiempo in empleado['Pasatiempos']:
        pasatisum[pasatiempo] = pasatisum.get(pasatiempo, 0) + 1

suma_edades = sum(e['Edad'] for e in empleados)
promedio_edades = suma_edades / len(empleados) if len(empleados) > 0 else 0
sumasueldos = sum(e['Sueldo'] for e in empleados)
promedio_sueldos = sumasueldos / len(empleados) if len(empleados) > 0 else 0
print()

maximoedad = empleados[0]
minimoedad = empleados[0]
for empleado in empleados:
    if empleado['Edad'] > maximoedad['Edad']:
        maximoedad = empleado
    if empleado['Edad'] < minimoedad['Edad']:
        minimoedad = empleado


print("Resumen:")
print("Empleados :", len(empleados))
print("Mujeres   :", numH)
print("Hombres   :", numM)
print("Pasatiempos:", ', '.join(f"{x}/{y}" for x, y in pasatisum.items()))
print(f"Edad - suma: {suma_edades}, Promedio: {promedio_edades:.1f}")
print(f"Sueldo - suma: {sumasueldos:,.2f}, promedio: {promedio_sueldos:,.2f}")
print(f"{maximoedad['Nombre']} de {maximoedad['Edad']} es el mayor, {minimoedad['Nombre']} de {minimoedad['Edad']} es el menor.")