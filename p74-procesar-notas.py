# Imprimir: cuantas notas, las notas, suma, promedio, notas menores al promedio y cuantas son nota máxima y nota mínima

import os; os.system('Clear')

notas = []

while True:
    try:
        nota = float(input("Introduce una nota (0 para terminar)  ? "))
        if nota == 0:
            break
        elif 0 <= nota <= 100:
            notas.append(nota)
        else:
            print("La nota debe estar entre 0 y 100.")
    except ValueError:
        print("Entrada no válida")

if len(notas) == 0:
    print("No hay notas")
else:
    suma_notas = sum(notas)
    promedio = suma_notas / len(notas)
    max_nota = max(notas)
    min_nota = min(notas)

menores_al_promedio = [nota for nota in notas if nota < promedio]

    
print(f"\nNúmero de notas: {len(notas)}")
print(f"Notas: {notas}")
print(f"Suma de las notas: {suma_notas}")
print(f"Promedio de las notas: {promedio:.2f}")
print(f"Notas menores al promedio: {menores_al_promedio}")
print(f"Número de notas menores al promedio: {len(menores_al_promedio)}")
print(f"Nota máxima: {max_nota}")
print(f"Nota mínima: {min_nota}")


