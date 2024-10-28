# Creamos una clase Empleado con atributos y metodos 
# Ampliamos la clase

# Codigo clase
class Empleado:
    def __init__(self, nombre, edad, sexo, casado):
        self.nombre =  nombre
        self.edad =  edad
        self.sexo =  sexo
        self.casado =  casado
    def __str__(self):
        return f'Nombre : {self.nombre}, Edad: {self.edad}, sexo : {'Mujer' if self.sexo=='M' else 'Hombre'}, Casado : {'Casad@' if self.casado else 'Solter@'}'

# Programa principal
import os;os.system('Clear')
emp01 = Empleado ('Alondra Vaquera', 23, 'M', False) # Creamos instancia
print(f'Nombre    :  {emp01.nombre}')
print(f'Edad      :  {emp01.edad}')
print(f'Sexo      :  {emp01.sexo}')
print(f'Casado    :  {emp01.casado}')

print()
emp02 = Empleado ('Emmanuel Prerez', 32, 'H', True) # Creamos instancia
print(f'Nombre    :  {emp02.nombre}')
print(f'Edad      :  {emp02.edad}')
print(f'Sexo      :  {emp02.sexo}')
print(f'Casado    :  {emp02.casado}')
print(f'Empleado  : {emp02} ')
print()

emp03 = Empleado('Rebeca Soto', 22, 'M', True)
print(f'Empleado  : {emp03} ')

promedad = (emp01. edad + emp02.edad + emp03.edad) / 3
print(f'Promedio de edad de los empleado {promedad}')


