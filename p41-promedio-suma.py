# Calcular la suma y el promedio de una serie de números introducidos hasta introducir 0.

import os; os.system("clear")

while True:
    print("Calcular la suma y el promedio de una serie de números, introducir 0 para finalizar proceso\n")

    cont = 0
    suma = 0

    while True:
        num = float(input("Introduce un numero ? "))
        if num == 0:  
            break
        suma += num
        cont += 1

    if cont > 0:  
        promedio = suma / cont
        print(f"La suma total es: {suma}")
        print(f"El promedio de los números es : {promedio}")
        print(f"Se ingresaron {cont} números")
    else:
        print("No se ingreso ningun numero valido ")

        if input("\n\nDeceas continuar (S/N)?").upper().startswith("N"): break

print("\n\nProceso Terminado...")

