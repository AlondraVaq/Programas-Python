# Crear una funcion que leea un arreglo de num. enteros
# Crear funcion para: Mayor, Menor y Media, Varianza y desiviacion estandar

import os, math

def leer_arreglo():
    numeros = input("Dame los números (separados por espacios): ")
    lista = []
    for numero in numeros:
        lista.append(int(numero))
    return lista

def mayor(lista):
    mayorValor = lista[0]
    for numero in lista:
        if numero > mayorValor:
            mayorValor = numero
    return mayorValor

def menor(lista):
    menorValor = lista[0]
    for numero in lista:
        if numero > menorValor:
            menorValor = numero
    return menorValor

def media(lista):
    suma = 0
    for numero in lista:
       suma += numero
    return suma / len(numero)

def varianza(lista):
    m = media(lista)
    sumaCuadrados = 0
    for x in lista:
     sumaCuadrados += (x -m) ** 2
    return sumaCuadrados / len(lista)

def desviacion_estandar(lista):
    return math.sqrt(varianza(lista))



# PRINCIPAL
os.system('Clear')

numeros = leer_arreglo()

media = media(numeros)
mayor = mayor(numeros)
menor = menor(numeros)
varianza = varianza(numeros)
desviacion_estandar = desviacion_estandar(numeros)
    
# Imprimir los resultados
print(f"Lista de números: {numeros}")
print(f"La media: {media:.3f}")
print(f"Mayor de los datos: {mayor}")
print(f"Menor de los datos: {menor}")
print(f"Varianza: {varianza:.3f}")
print(f"Desviación estándar: {desviacion_estandar:.3f}")


