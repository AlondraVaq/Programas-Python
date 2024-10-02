# Imprimir:  dos listas con 5 elementos, Multiplica las listas y guárdalos en una tercera lista

import os; os.system('Clear')

lista1 = []
lista2 = []
lista3 = []

print ('Introduce 5 numeros alaetorios para la lista1 : ')
for i in range(5) :
    n = int (input(f"Elemento [{i+1 }]="))
    lista1.append(n)
print(lista1)

print ('Introduce 5 numeros alaeatorios para lista2')
for i in range(5) :
    n = int (input(f"Elementos [{i+1}]="))
    lista2.append(n)
print(lista2)

print ('Multplica listas lista3 = lista1 + lista2')
for i in range(5):
    lista3.append(lista1[i] * lista2[i])
print(lista3)
