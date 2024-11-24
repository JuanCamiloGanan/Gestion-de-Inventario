# Clase del Árbol AVL para gestionar el inventario de productos
class NodoAVL:
    def __init__(self, producto):
        self.producto = producto
        self.izq = None
        self.der = None
        self.altura = 1
