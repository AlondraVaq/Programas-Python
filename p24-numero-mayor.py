# Verificar cual es el numero mayor, de tres numeros dados

import os; os.system("clear")

print("Verifica cuál de los tres números es mayor\n")

n1 = int(input("Ingresa el primer numero: "))
n2 = int(input("Ingresa el segundo numero: "))
n3 = int(input("Ingresa el tercer numero: "))


if n1 >= n2 and n1 >= n3:
     mayor = n1
elif n2 >= n1 and n2 >= n3:
    mayor = n2
else:
    mayor = n3


print(f"El numero mayor es: {mayor}")


print ("\nProceso terminado")