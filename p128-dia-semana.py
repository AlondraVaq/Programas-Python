# Función que pida un número entero entre 1 y 7 y devuelva el día de la semana con letra.

import os

def dia_semana():
    
    num = int(input("Elige un número (1-7) : "))

    if num < 1 or num > 7:
        return "Número incorrecto, elige nuevamente"
       
    dia_semana = {
        1: "Lunes",
        2: "Martes",
        3: "Miércoles",
        4: "Jueves",
        5: "Viernes",
        6: "Sábado",
        7: "Domingo"
    }
    
    return dia_semana[num]

# PRINCIPAL
os.system('Clear')
dia = dia_semana()
print("El día de la semana es :", dia)