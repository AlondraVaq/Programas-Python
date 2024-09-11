# PRIMER EXAMEN PARCIAL
# Se desea llevar el control de la inscripción a un evento académico de la Universidad Patito. Se especifica: Tipo de usuario, paquete y cantidad.

import os; os.system("clear")
 
print("Universidad Patito SA de CV")
print("Sistema de Inscripción Congreso de Sistemas")

total_ventas_por_dia = 0

while (True):
    print("\nTipo de usuario: ")
    print("[1] Alumno - $100")
    print("[2] Trabajador - $200")
    print("[3] Docente - $500")
    tipo_usuario = int(input("Elige el usuario (1, 2, 3): "))
    

    print("\nTipo de paquete existente:")
    print("[1] Solo conferencias - $600")
    print("[2] Con eventos sociales - $800")
    print("[3] Con kit de acceso - $900")
    tipo_paquete = int(input("Elige el tipo de paquete que deseas (1, 2, 3): "))
     
    
    cantidad = int(input("Introduce la cantidad solicitada: "))


    if tipo_usuario == 1:
       precio_usuario = 100
       nombre_usuario = "Alumno"
    elif tipo_usuario == 2:
         precio_usuario = 200
         nombre_usuario = "Trabajador"
    elif tipo_usuario == 3:
         precio_usuario = 500
         nombre_usuario = "Docente"
    else:
         print("Tipo de usuario inválido.")
         continue


    if tipo_paquete == 1:
        precio_paquete = 600
        nombre_paquete = "Solo conferencias"
    elif tipo_paquete == 2:
        precio_paquete = 800
        nombre_paquete = "Con eventos sociales"
    elif tipo_paquete == 3:
        precio_paquete = 900
        nombre_paquete = "Con kit de acceso"
    else:
        print("Tipo de paquete no válido.")
        continue



    subtotal = (precio_usuario + precio_paquete) * cantidad

    if subtotal > 5000:
        if tipo_usuario == 1:  
            descuento = subtotal * 0.20
            porcentaje_descuento = 20
        elif tipo_usuario == 2:  
            descuento = subtotal * 0.10
            porcentaje_descuento = 10
        elif tipo_usuario == 3:  
            descuento = subtotal * 0.05
            porcentaje_descuento = 5
        else:
            descuento = 0
    else:
      descuento = 0

    total = subtotal - descuento


    print("\nResumen de la venta:")
    print(f"Tipo de usuario: {nombre_usuario} (Costo: ${precio_usuario})")
    print(f"Tipo de paquete: {nombre_paquete} (Costo: ${precio_paquete})")
    print(f"Cantidad: {cantidad}")
    print(f"Subtotal: ${subtotal:.2f} con un descuento de : ${descuento:.2f} ({porcentaje_descuento}%)\n")
    print(f"Total a pagar: ${total:.2f}")

    total_ventas_por_dia += total

    print(f"\nTotal de ventas del día: ${total_ventas_por_dia:.2f}")

    if input("\n\nDeceas continuar (S/N)?").upper().startswith("N"): break
    
    print("\nProceso Terminado. Gracias por usar el sistema...")


