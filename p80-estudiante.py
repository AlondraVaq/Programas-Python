# Datos de un estudiente usando diccionario

import os; os.system('Clear')

estudiante = { 'Nimbre'  : 'Juan Perez',
               'Edad'    :  45,
               'Correo'  : 'jperez@msn.com',
               'Carrera' : 'Sistemas'}

print('El estudiante :', estudiante, len(estudiante))

estudiante['Calificacion'] = 9.5
estudiante['Correo'] = 'juan@gmail.com'
print('El estudiante :', estudiante, len(estudiante))

print('\nLlaves', estudiante.keys())
for k in estudiante.keys():
    print(k, end=' ')

print('\n\nValores', estudiante.values())
for v in estudiante.values():
    print(v, end=' ')

print('\n\nLlaves y Valores al mismo tiempo')
for k, v in estudiante.items():
    print(f'{k:<15} : {v}')

print('\n\nLlaves y Valores al mismo tiempo - forma 2 ')
for k in estudiante.keys():
    print(f'{k:<15} : {estudiante[k]}')