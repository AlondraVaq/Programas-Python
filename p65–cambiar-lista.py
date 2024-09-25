# CAMBIAR LOS ELEMENTOS DE UNA LISTA DE NUMEROS 

import os;os.system('Clear')

nums = [10, 9, 8.5, 6.5, 7.5, 6.2, 9.5]

print('Cambiar o modificar los elementos de una lista ')

print(type(nums))
print('La lista : ' , nums, len(nums))

print('Modificar elementos de las posisciones 0 y 1')

nums [0] = 7
nums [1] = 7
print('Resuelta en : ' , nums)

print('Modificar elementos de las posisciones 2 y 5')
nums [2:5] = [9.0, 9.0, 9.0]
print('Resulta en :', nums)
