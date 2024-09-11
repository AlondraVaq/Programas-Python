# Calcular el número mayor de una serie de números introducidos, introduciendo 0 termina proceso

import os; os.system("clear")

while (True):
    print("Introduce números para encontrar el mayor. Ingresa 0 para finalizar.")
    mayor = -1

    while (True):
        numero = int(input("Introduce un número: "))
        if numero == 0:
            break
        
        if numero > mayor:  
            mayor = numero
        
    if mayor == -1:
            print("\nNo se ingresaron números positivos")
    else:
          print(f"\nEl número mayor ingresado es: {mayor}")
    
    
    if input("\n\nDeceas continuar (S/N)?").upper().startswith("N"): break

print("\n\nProceso Terminado...")