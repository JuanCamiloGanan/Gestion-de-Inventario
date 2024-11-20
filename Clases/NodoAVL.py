# Nodo AVL para el arbol de productos
class NodoAVL:
    def __init__(self, producto):
        self.dato = producto
        self.izq = None
        self.der = None
        self.altura = 1


# Clase del Árbol AVL para gestionar el inventario de productos
class ArbolAVL:

    def __init__(self):
        self.raiz = None

    # Método para insertar un producto en el árbol AVL
    def insertar(self, raiz, producto):

        if not raiz:
            return NodoAVL(producto)

        if producto.codigo < raiz.producto.codigo:
            raiz.izq = self.insertar(raiz.izq, producto)
        elif producto.codigo > raiz.producto.codigo:
            raiz.der = self.insertar(raiz.der, producto)
        else:
            print(f"Error: Ya existe un producto con el código {producto.codigo}")
            return raiz

        # Actualizar la altura del nodo y balancear el árbol
        raiz.altura = 1 + max(self.getAltura(raiz.izq), self.getAltura(raiz.der))
        return self.balancear(raiz, producto)

    # Método para balancear el árbol si esta desbalanceado
    def balancear(self, raiz, producto):
        balance = self.getBalance(raiz)

        # Rotaciones necesarias para balancear el árbol
        if balance > 1 and producto.codigo < raiz.izq.producto.codigo:
            return self.rotacionDerecha(raiz)

        if balance < -1 and producto.codigo > raiz.der.producto.codigo:
            return self.rotacionIzquierda(raiz)

        if balance > 1 and producto.codigo > raiz.izq.producto.codigo:
            raiz.izq = self.rotacionIzquierda(raiz.izq)
            return self.rotacionDerecha(raiz)

        if balance < -1 and producto.codigo < raiz.der.producto.codigo:
            raiz.der = self.rotacionDerecha(raiz.der)
            return self.rotacionIzquierda(raiz)

        return raiz

    # Método para buscar un producto en el árbol AVL por su código
    def buscar(self, raiz, codigo):
        if not raiz or raiz.producto.codigo == codigo:
            return raiz
        elif codigo < raiz.producto.codigo:
            return self.buscar(raiz.izq, codigo)
        else:
            return self.buscar(raiz.der, codigo)

    #Metodo para editar un producto en el arbol AVL
    def editar_producto(self, raiz, codigo, nombre=None, cantidad=None, precio=None):
        nodo = self.buscar(raiz, codigo)
        if nodo:
            return nodo.producto.editar(nombre=nombre, cantidad=cantidad, precio=precio)
        return f"Error: No existe un producto con el código {codigo}"

    # Métodos para rotaciones (der o izq) para mantener el balance del árbol
    def rotacionDerecha(self, y):
        x = y.izq
        T2 = x.der

        x.der = y
        y.izq = T2

        y.altura = 1 + max(self.getAltura(y.izq), self.getAltura(y.der))
        x.altura = 1 + max(self.getAltura(x.izq), self.getAltura(x.der))

        return x

    def rotacionIzquierda(self, x):
        y = x.der
        T2 = y.izq

        y.izq = x
        x.der = T2

        x.altura = 1 + max(self.getAltura(x.izq), self.getAltura(x.der))
        y.altura = 1 + max(self.getAltura(y.izq), self.getAltura(y.der))

        return y

    # Método para obtener la altura y el balance de los nodos
    def getAltura(self, nodo):
        return nodo.altura if nodo else 0

    def getBalance(self, nodo):
        return self.getAltura(nodo.izq) - self.getAltura(nodo.der)