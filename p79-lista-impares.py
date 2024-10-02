# Imprimir numeros impares, su suma y promedio, mostrar los números que son divisibles entre 3 y sumarlos
# Pedir un elemento a buscar en la lista original y decir si esta y en que posición

import os; os.system('Clear')

while True:
    try:
        n = int(input("Que números impares que desceas ? "))
        if n > 0:
            break
        else:
            print("introduce un número entero positivo.")
    except ValueError:
        print("Error. Debe ser un número entero e impar.")

impares = []
num = 1
while len(impares) < n:
    impares.append(num)
    num += 2

suma_impares = sum(impares)
promedio_impares = suma_impares / n

print(f"\nLista de los primeros {n} números impares: {impares}")
print(f"Suma de los números impares: {suma_impares}")
print(f"Promedio de números impares: {promedio_impares:.2f}")


division = [x for x in impares if x % 3 == 0]
suma_divisibles_3 = sum(division)

print(f"\nNúmeros impares divisibles entre 3: {division}")
print(f"Suma de los números divisibles entre 3: {suma_divisibles_3}")

while True:
    try:
        buscar = int(input("\nQue número deseea buscar en la lista ? "))
        break
    except ValueError:
        print("Error, introduce un número entero.")

if buscar in impares:
    posicion = impares.index(buscar)
    print(f"El número {buscar} está en la posición {posicion}.")
else:
    print(f"El número {buscar} no está en la lista.")