# Dado un numero del 1-7, mostrar el dia de la semana

import os; os.system("clear")

print("Dado un numero del 1-7, mostrar el dia de la semana\n")

n = int(input("Igresa un numero: "))

if n == 1:
    print("Lunes")
elif n == 2:
    print("Martes")
elif n == 3:
    print("Miércoles")
elif n == 4:
    print("Jueves")
elif n == 5:
    print("Viernes")
elif n == 6:
    print("Sabado")
elif n == 7:
    print("Domingo")
else:
    print("Dia invalido")

print ("\nProceso terminado")