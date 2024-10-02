# Imprimir: un número de mes, días del mes, y nombre del mes, guarda días en una lista, y nombres de mes en otra.

import os; os.system('Clear')

nombres_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
dias_meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while True:
    try:
        numero_mes = int(input("Número de mes : "))
        if 1 <= numero_mes <= 12:
            break
        else:
            print("Por favor, un número entre 1 y 12")
    except ValueError:
        print("Entrada no válida")

nombre_mes = nombres_meses[numero_mes - 1]  

dias_mes = dias_meses[numero_mes - 1]

print(f"\nMes: {nombre_mes}")
print(f"Días: {dias_mes}")