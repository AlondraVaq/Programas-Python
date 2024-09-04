# Cuenta numero, los suma, cuenta: positivos, negativos, ceros, para parar en -1

import os;os.system("Clear")

print("Cuenta numero, los suma, cuenta: positivos, negativos, ceros, para parar en -1\n")

c = s = 0
cp = cn = cc = 0

while True:
    num = int(input("Numero ?"))
    if num  == -1:
        break
    else:
        c = c + 1
        s = s + num
        if num > 0 : 
            cp = cp + 1
        elif num < 0 : 
            cn = cn + 1
        else: cc = cc + 1



print(f"Capturaste {c} numeros y su suma es {s}")

print(f"Positivos: {cp} \nNegativos: {cn} \nceros: {cc}")


print("Proceso terminado\n")