class NodoAVL:
    def __init__(self, producto):
        self.producto = producto  # El nodo contiene el producto
        self.izquierda = None  # Subárbol izquierdo
        self.derecha = None  # Subárbol derecho
        self.altura = 1  # Altura del nodo (inicializada en 1)

class ArbolAVL:
    def __init__(self):
        self.raiz = None  # El árbol comienza vacío

    def obtener_altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura

    def actualizar_altura(self, nodo):
        nodo.altura = 1 + max(self.obtener_altura(nodo.izquierda), self.obtener_altura(nodo.derecha))

    def obtener_factor_balance(self, nodo):
        return self.obtener_altura(nodo.izquierda) - self.obtener_altura(nodo.derecha)

    def rotar_derecha(self, nodo):
        nueva_raiz = nodo.izquierda
        nodo.izquierda = nueva_raiz.derecha
        nueva_raiz.derecha = nodo
        self.actualizar_altura(nodo)
        self.actualizar_altura(nueva_raiz)
        return nueva_raiz

    def rotar_izquierda(self, nodo):
        nueva_raiz = nodo.derecha
        nodo.derecha = nueva_raiz.izquierda
        nueva_raiz.izquierda = nodo
        self.actualizar_altura(nodo)
        self.actualizar_altura(nueva_raiz)
        return nueva_raiz

    def balancear(self, nodo):
        factor_balance = self.obtener_factor_balance(nodo)

        if factor_balance > 1:
            if self.obtener_factor_balance(nodo.izquierda) < 0:
                nodo.izquierda = self.rotar_izquierda(nodo.izquierda)
            return self.rotar_derecha(nodo)

        if factor_balance < -1:
            if self.obtener_factor_balance(nodo.derecha) > 0:
                nodo.derecha = self.rotar_derecha(nodo.derecha)
            return self.rotar_izquierda(nodo)

        return nodo

    def insertar(self, nodo, producto):
        if not nodo:
            return NodoAVL(producto)

        if producto.codigo < nodo.producto.codigo:
            nodo.izquierda = self.insertar(nodo.izquierda, producto)
        else:
            nodo.derecha = self.insertar(nodo.derecha, producto)

        self.actualizar_altura(nodo)
        return self.balancear(nodo)

    def insertar_producto(self, producto):
        self.raiz = self.insertar(self.raiz, producto)

    def recorrer_en_orden(self, nodo):
        if nodo:
            self.recorrer_en_orden(nodo.izquierda)
            print(f"ID: {nodo.producto.codigo}, Nombre: {nodo.producto.nombre}, Código: {nodo.producto.codigo}, Cantidad: {nodo.producto.cantidad}, Precio: {nodo.producto.precio}")
            self.recorrer_en_orden(nodo.derecha)

    def mostrar(self):
        self.recorrer_en_orden(self.raiz)
