# Crear funcion: leea un arreglo de numeros, calcula factorial, capturar listas e imprimir listas 

import os 

def leer_arreglo():
    numeros = input("Dame los números (separados por espacios): ")
    return numeros

def calcular_factorial(num):
    if num == 0 or num == 1:
        return 1
    factorial = 1
    for i in range(2, num + 1):
        factorial *= i
    return factorial

def lista_factoriales(lista_numeros):
    factoriales = []
    for num in lista_numeros:
        factoriales.append(calcular_factorial(num))
    return factoriales

#PRINCIPAL 
os.system('Clear')
lista_numeros = leer_arreglo()
lista_factoriales_resultado = lista_factoriales(lista_numeros)

print(f"La lista de números originales: {lista_numeros}")
print(f"La lista con los factoriales: {lista_factoriales_resultado}")


