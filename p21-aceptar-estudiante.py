# Aceptar un estudiante en base a su edad y dos calificaciones

# >= 18    c1>=8   y   c2>=8

import os; os.system("clear")

print("Universidad Patito SA de CV")
print("Aceptar un estudiante en base a su edad y dos calificaciones")


nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))

if edad < 18 :
    print("Solo aceptamos mayores de 18 años")
else :
    print("Ingresa 2 calificaciones separadas por enter:  ")
    c1, c2 = int(input()), int(input())
if c1 < 8 or c2 < 8 :
    print("solo aceptamos alumnos con calificaciones mayores a 8")
else :
    print(f"{nombre} bienvenid@ a la Universidad Patito, tu edad {edad} y calificaciones {c1} y {c2} lo permiten")

print("Gracias por utilizar el programa")
