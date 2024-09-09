# El usuario adivina un numdero entero entre el 1 y 100

import os, random

while (True):
    os.system("Clear")
    num_secreto = random.randint(1,100)
    intentos = 0


    while (True):

        num_ingresado = int(input("Adivina el numero secreto (1-100) ?"))
        intentos  += 1
        if num_ingresado == num_secreto :
            print(f"\nFelicidades adivinaste en {intentos} intentos.")
            break
        elif num_ingresado < num_secreto:
            print("El numero secreto es mayor")
        else:
             print("El numero secreto es menor")


    if input("\n\nDeceas continuar (S/N)?").upper().startswith("N"): break

print("\n\nProceso Terminado...")