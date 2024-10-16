# Crear dos conjuntos con nombres de personas, mostrar los conjuntos: union, interseccion, diferencia, dif. simetrica.
# Mostrando subconjuntos, superconjuntos.

import os; os.system('clear')

A = {'Juan', 'Maria', 'Pedro', 'Jose', 'Rocio'}
B = {'Pedro', 'Juan', 'Pablo', 'Mateo', 'Esther'}


print(A, B)

print('\nUnion: ')
print('A union B', A.union(B))
print('A union B', A | B)

print('\nInterseccion')
print('A interseccion B', A.intersection(B))
print('A interseccion B', A & B)

print('\nDiferencia')
print('A Diferencia B', A.difference(B))
print('A Diferencia B', A - B)

print('\nDiferencia simetrica')
print('A Diferencia simetrica B', A.symmetric_difference(B))
print('A Diferencia simetrica B', A ^ B)

print('\nProbar por subconjuntos')
C = {'Pablo', 'Mateo'}
print('Pablo y Mateo son subconjuntos del B', C.issubset(B))
print('Pablo y Mateo son subconjuntos del B', C <= B)

print('\nProbar superconjuntos')
D = {'Reynaldo', 'Angelica'}
print('A es superconjuntos de Reynaldo y Angelica', A.issubset(D))
print('A es superconjuntos de Reynaldo y Angelica', A >= D)

print('\nVerificar pertenencia o no pertencia al conjunto')
print('Pedro esta en el A', 'Pedro' in A)
print('Lilia no esta en B', 'Lilia' not in B)
