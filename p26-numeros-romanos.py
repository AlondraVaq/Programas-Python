# Muestar el equivalente en numero romano, dando numeros enteros del 1-10

import os; os.system("clear")

print("Dado un numero, mostrar el equvalente en  numero romano\n")

n = int(input("Igresa un numero: "))

if n == 1:
    print("Num. romano es:   I")
elif n == 2:
    print("Num. romano es:   II")
elif n == 3:
    print("Num. romano es:   III")
elif n == 4:
    print("Num. romano es:   IV")
elif n == 5:
    print("Num. romano es:   V")
elif n == 6:
    print("Num. romano es:   VI")
elif n == 7:
    print("Num. romano es:   VII")
elif n == 8:
    print("Num. romano es:   VIII")
elif n == 9:
    print("Num. romano es:   IX")
elif n == 10:
    print("Num. romano es:   X")
else:
    print("Número inválido invalido")

print ("\nProceso terminado")
