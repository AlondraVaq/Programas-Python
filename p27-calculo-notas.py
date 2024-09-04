#Calcula el promedio de 5 calificaciones

import os; os.system("clear")

print("Calculando el promédio de 5 calificaiones\n")

print("Ingresa las calificaciones separados por un espacio: ")

n1,n2,n3,n4,n5 = input().split()
n1,n2,n3,n4,n5 = [int(n1),int(n2),int(n3),int(n4),int(n5)]

prom = (n1+n2+n3+n4+n5)/5
print(f"{prom}")

if prom >= 0 and prom < 6:
    print(f"Promedio de {prom:.2f}. Quedas reprobado")
elif prom >= 6 and prom < 7:
    print(f"Promedio de {prom:.2f}. Pasas de panzazo")
elif prom >= 7 and prom < 8:
    print(f"Promedio de {prom:.2f}. Muy bien, pues mejorar")
elif prom >= 8  and prom < 9:
    print(f"Promedio de {prom:.2f}. Excelente sigue así")
elif prom >= 9 and prom <= 10:
    print(f"Promedio de {prom:.2f}. Perfecto tu esfuerzo valió la pena")