# Aceptar estudiante en base a: nombre, sexo, edad y 3 calificaciones


import os; os.system("clear")

print("Aceptar estudiante en base a: nombre, sexo, edad y 3 calificaciones\n")

nombre = input("Ingresa tu nombre ? ")
sexo = input("Ingresa tu genero [M] - [F] ? ")

if sexo != "F":
    print("Solo se aceptan a mujeres")
else: 
    edad = int(input("Ingresa tu edad: "))
    if edad < 21:
        print("Eres mujer, pero no tienes la edad, solo mayores de 21 años")
    else:
        print("Ingresa primera claificacion:  ")
        print("Ingresa segunda claificacion:  ")
        print("Ingresa tercera claificacion:  ")
        c1,c2,c3 = input().split()
        c1,c2,c3 = [int(c1),int(c2),int(c3)]
        prom = (c1+c2+c3)/3
        if prom >= 8 and prom <= 9.5:
            print(f"{nombre} Bienvenida a la Universidad Kitty Kat SA, tu edad {edad} y calificaciones {c1}, {c2} y {c3} lo permiten")
        elif prom > 9.5: 
            print(f"{nombre} Bienvenida a la Universidad Kitty Kat SA, por tu exelencia academica")
        else:
            print("Eres mujer, tienes la edad, pero tu promédio no alcanza, solo promedios de 8 a 9.5")


print("\nProceso terminado")