# Crear un diccionario de llave numérica dias.

import os; os.system('Clear')

dias = {
    1: "Lunes",
    2: "Martes",
    3: "Miércoles",
    4: "Jueves",
    5: "Viernes",
    6: "Sábado",
    7: "Domingo"
}

# Mostrar el diccionario
print("Diccionario de días:", dias)

# Acceder y mostrar el primer elemento
primer_elemento = dias[1]
print("Primer elemento:", primer_elemento)

# Acceder y mostrar el último elemento
ultimo_elemento = dias[7]
print("Último elemento:", ultimo_elemento)

# Acceder y mostrar el quinto elemento usando get()
quinto_elemento = dias.get(5)
print("Quinto elemento:", quinto_elemento)

# Acceder y mostrar el séptimo elemento usando get()
septimo_elemento = dias.get(7)
print("Séptimo elemento:", septimo_elemento)

# Mostrar el diccionario completo
print("\nDiccionario completo:")
for key, value in dias.items():
    print(f"{key}: {value}")