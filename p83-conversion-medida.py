# Conversion a mts de km, m, cm, mm

import os; os.system('Clear')

conversiones = {
    'Km' : 1000,    # kilometros
    'm'  : 1,       # metros 
    'cm' : 0.01,    # centimetros
    'mm' : 0.001    # milimetros
}

longitud = int(input('Longitud'))

while True:
    print('Unidades :', conversiones.keys())
    unidad = input()
    if unidad in conversiones:
        break


resultado = longitud * conversiones[unidad]

print(f'Longitud : {longitud} {unidad} son {resultado} metros' )