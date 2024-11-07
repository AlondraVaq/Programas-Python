# Modela un artículo, disño de una clase llamada ARTICULO, con id, descripción, cantidad y precio

class Articulo:
    def __init__(self, id, descripcion, cantidad, precio):
        self.id = id
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.precio = precio
        
    def obtenerTotal(self):
        return self.cantidad * self.precio
    
    def __str__(self):
        return f"Articulo [ID : {self.id}, Descripcion : {self.descripcion}, Cantidad : {self.cantidad}, Precio : {self.precio:.2f}], Total : {self.obtenerTotal():.2f}"

# PROGRAMA PRINCIPAL
import os; os.system("Clear")

art1 = Articulo('A101', 'Pluma Roja', 888, 0.08)
print(art1)
art1.cantidad = 999
art1.precio = 0.99

print("\nDetalles de articulo 1 despues de cambios:")
print("ID : ", art1.id)
print("Descripcion: ", art1.descripcion)
print("Dantidad :", art1.cantidad)
print("Precio : ", art1.precio)
print("Total : ", art1.obtenerTotal())

art2 = Articulo("A102", "Pluma Azul", 934, 1.2)
print(art2)

art3 = Articulo("P103", "Lapiz del 12", 456, 0.5)
print(art3)

total = art1.obtenerTotal() + art2.obtenerTotal() + art3.obtenerTotal()
print(f"\nTotal de todos los articulos: ${total:.2f}")