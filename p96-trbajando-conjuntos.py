# Realizar operaciones basicas en un conjunto

import os; os.system('clear')

muns = {'Zacatecas', 'Guadalupe', 'Jerez', 'Fresnillo', 'Fresnillo'}

print('El conjunto:', muns, len(muns))

print('Lista de muncipios')
for mun in muns:
    print(mun, end =' ')

print('\nEsta zacatecas en los municipios - ', 'Zacatecas' in muns)

muns.add('Teul')
print('El conjunto :' , muns, len(muns))

mas = {'Luis Moya', 'Ojocaliente', 'Tepetongo', 'Rio Grande'}

muns.update(mas)
print('El conjunto :', muns, len(muns))

muns.remove('Luis Moya')
print('El conjunto :', muns, len(muns))

muns.discard('Luis Moya')
print('El conjunto :', muns, len(muns))

mun = muns.pop()
print(mun)
print('El conjunto :', muns, len(muns))

muns.clear()
print('El conjunto :', muns, len(muns))
