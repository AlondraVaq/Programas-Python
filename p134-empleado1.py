# Creamos una clase Empleado con atributos y metodos 

# Codigo clase
class Empleado:
    def __init__(self, nombre, edad):
        self.nombre =  nombre
        self.edad =  edad
    def __str__(self):
        return f'Nombre : {self.nombre}, Edad: {self.edad}'

# Programa principal
import os;os.system('Clear')
emp01 = Empleado ('Alondra Vaquera', 35) # Creamos instancia
emp02 = Empleado ('Juan Perez', 66) # Creamos instancia


print('\nDatos del empleado 1')
print(f'Nombre empleado : {emp01.nombre}')
print(f'Edad empleado : {emp01.edad}')
print(f'Empleado  {emp01}')
emp01.edad = 40
print(f'Empleado : {emp01}')

print('\nDatos del empleado 2')
print(f'Nombre empleado : {emp02.nombre}')
print(f'Edad empleado   : {emp02.edad}')
print(f'Empleado        : {emp02}')
