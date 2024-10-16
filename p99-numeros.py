# Crear 3 conjuntos de numeros, mostrando: uniones, difrencia, dif. simetrica e interseccion

import os; os.system('clear')


A = {50, 60, 70, 80, 90, 100, 200}
B = {60, 90, 100, 300, 400, 500}
C = {10, 20, 60, 90, 70, 100, 600, 700}


print(A, B, C)

print('\nUnion: ')
print('A union B', A.union(B))
print('B union C', B.union(C))

print('\nDiferencia')
print('A Diferencia C', A.difference(C))

print('\nDiferencia simetrica')
print('B Diferencia simetrica C', B.symmetric_difference(C))

print('\nInterseccion')
print('B interseccion C', B.intersection(C))

print('\nProbar por subconjuntos')
print('A es subconjuntos del B', A.issubset(B))
print('C es subconjuntos del A', C.issubset(A))

print('\nVerificar pertenencia o no pertencia al conjunto')
print('100 esta en el A?', 100 in A)
print('60 esta en el A?, Y en B?, Y en B?', 60 in (A and B and C))
print('900 no esta en C?', 900 not in C)

