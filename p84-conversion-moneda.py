# Conversion de didferentes monedas a pesos mexicanos

import os; os.system('Clear')

monedas = {
             'USD': 20.50, #Dolares
             'EUR': 22.30,  #Euros
             'GBP': 25.80,  #Libra esterlina
             'JPY': 0.10,   #Yen japones
             'CDA': 16.20   #Dolar canadiense
}

print('Conversion de didferentes monedas a pesos mexicanos')
print('Monedas :')

for m in monedas.keys(): print(f'-{m}')

while True:
    moneda = input('Moneda ? ').upper()
    if moneda in monedas: break

cantidad = float(input('Cantidada ?'))

resultado = cantidad * monedas[moneda]

print(f'{cantidad} {moneda} son {resultado} pesos mex.')