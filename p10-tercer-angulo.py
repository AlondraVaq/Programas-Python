# Calcular el tercer angulo de un trinagulo

print("Calcular el tercer angulo de un trinagulo\n")

angulo1 = int(input("Ingresa el valor del primer ángulo en grados: "))
angulo2 = int(input("Ingresa el valor del segundo ángulo en grados: "))

   
   
if angulo1 <= 0 or angulo2 <= 0:
        print("Los ángulos deben ser mayores que 0")
elif angulo1 + angulo2 >= 180:
        print("La suma de los dos ángulos no puede ser mayor o igual a 180 grados")
else:
    angulo3 = 180 - (angulo1 + angulo2)
        

print(f"El tercer ángulo es: {angulo3} grados")
