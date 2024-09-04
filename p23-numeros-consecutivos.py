#  Verificar si los tres números son consecutivos, confirmando o mandar mensaje de error

import os; os.system("clear")

print("Verificar si los tres números son consecutivos, confirmando o mandar mensaje de error\n")

print("Dame 3 números enteros separados por un espacio: ")

n1,n2,n3 = input().split()
n1,n2,n3 = [int(n1),int(n2),int(n3)]

if n1 < n2 and n1 < n3 and n2 < n3:
    print(f"Los números {n1}, {n2}, {n3} Si son consecutivos")
else:
    print(f"Error los números {n1}, {n2}, {n3} No son consecutivos")

print ("\nProceso terminado")