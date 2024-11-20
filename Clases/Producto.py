#Clase para agregar cada producto a la lista de productos
class Producto:
    def __init__(self, codigo, nombre, cantidad, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} (Código: {self.precio}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f})"

    def editar(self, nombre=None, cantidad=None, precio=None):
        if nombre:
            self.nombre = nombre
        if cantidad is not None:
            self.cantidad = cantidad
        if precio is not None:
            self.precio = precio

        return f"Producto {self.codigo} actualizado: {self}"

    @staticmethod

    def agregar(codigo, nombre, cantidad, precio):
        return Producto(codigo, nombre, cantidad, precio)