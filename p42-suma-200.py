# Calcular la suma de números introducidos por el usuario hasta que la suma sea >= 200, 
# Luego mostrar cuantos números fueron introducidos y la suma de estos.

import os; os.system("clear")

while (True):
    print ("Introduce números para sumar, la suma debe ser >= 200 para finalizar")
    suma = 0
    contador = 0

    while suma < 200:
        num = int(input("Introduce un numero ?"))
        suma += num
        contador +=1
    
    print(f"La suma de los números es: {suma}")
    print(f"Se introdujeron {contador} números.")

    if input("\n\nDeceas continuar (S/N)?").upper().startswith("N"): break

print("\n\nProceso Terminado...")