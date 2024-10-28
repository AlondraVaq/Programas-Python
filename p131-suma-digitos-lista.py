# crear funciones que: leea arreglo de num, sume digitos individuales, capturar lista, e inprimir lista

def leer_arreglo():
    nums = list(map(int, input("Dame números (separados x espacio): ").split()))
    return nums

def sumar_digitos(num):
    suma = 0
    while num > 0:
        suma += num % 10  
        num //= 10        
    return suma

def lista_suma_digitos(lista):
    suma_digitos = []
    for num in lista:
        suma_digitos.append(sumar_digitos(num))
    return suma_digitos

# PRINCIPAL
numeros = leer_arreglo()
suma_digitos_lista = lista_suma_digitos(numeros) 

print("\nLa lista de números original:", numeros)
print("La lista con la suma de los dígitos de los números:", suma_digitos_lista)