# Calcula e imprime los numeros de la conjuntura de collatz

import os

while(True):
    os.system("Clear")
    num = int(input("Dame un numero posistivo ?"))

    while num!=1 :
        print(num, end = " ")
        if num % 2 == 0 :
            num = num // 2
    else:
        num= num *3 +1 
        print (num, end= "") 


    if input ("\n n Deseas continuar (S/N)").upper().startswith("N"): break

print("\n Proceso terminado...")
