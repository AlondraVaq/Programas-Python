# Imprimir los números pares de forma decendente desde el 100 hasta donde el usuario lo desea y sumarlos 

import os; os.system("clear")

print("Imprimir los números pares de forma decendente desde el 100 hasta donde el usuario lo desea y sumarlos \n")

while True:
    n = int(input("Introduce el número par que deseas(n): "))
    
    if n > 100:
        print("El número debe ser menor o igual a 100.")
        continue  

    suma = 0
    i = 100  

    print(f"Números pares desde 100 hasta {n}:")
    
    while i >= n:
        if i % 2 == 0:  
            print(i, end=" ")
            suma += i  
        i -= 1
    print(f"\nSuma de los números pares: {suma}")


    if input("\n\nDeceas continuar (S/N)?").upper().startswith("N"): break

print("\n\nProceso Terminado...")




