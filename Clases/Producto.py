#Clase para agregar cada producto a la lista de productos
class Producto:
    def __init__(self, codido, nombre, cantidad, precio):
        self.codigo = codido
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} (Códgo: {self.precio}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f})"