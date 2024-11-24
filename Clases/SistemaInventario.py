# Importar las clases necesarias

from Producto import Producto
from ArbolAVL import ArbolAVL  # Ahora ArbolAVL maneja todo el árbol AVL
from ColaReabastecimiento import ColaReabastecimiento

class SistemaInventario:
    def __init__(self, limite_critico=10):

        self.raiz = None  # Raíz del árbol AVL
        self.arbol_avl = ArbolAVL()  # Inicializa el árbol AVL
        self.cola_reabastecimiento = ColaReabastecimiento(limite_critico)  # Inicializa la cola de reabastecimiento

    def agregar_producto(self, codigo, nombre, cantidad, precio):
        producto = Producto(codigo, nombre, cantidad, precio)

        # Insertar el producto en el Nodo AVL
        if not self.raiz:
            self.arbol_avl.raiz = self.arbol_avl.insertar(self.arbol_avl.raiz, producto)
        else:
            self.raiz = self.raiz.insertar(self.raiz, producto)

        # Agregar el producto a la cola de reabastecimiento si tiene existencias críticas
        self.cola_reabastecimiento.agregar(producto)

        return f"Producto '{nombre}' agregado con éxito."

    def editar_producto(self, codigo, nombre=None, cantidad=None, precio=None):
        nodo = self.raiz.buscar(self.raiz, codigo)
        if nodo:
            mensaje = nodo.producto.editar(nombre=nombre, cantidad=cantidad, precio=precio)

            # Si la cantidad editada es crítica, actualiza la cola de reabastecimiento
            self.cola_reabastecimiento.agregar(nodo.producto)

            return mensaje
        else:
            return f"No se encontró un producto con el código {codigo}."

    def listar_productos(self):
        productos = self._listar_en_orden(self.raiz)
        if not productos:
            return "No hay productos registrados."
        return "\n".join(productos)

    def _listar_en_orden(self, nodo):
        if not nodo:
            return []
        return (
            self._listar_en_orden(nodo.izquierda)
            + [str(nodo.producto)]
            + self._listar_en_orden(nodo.derecha)
        )

    #Metodo para eliminar un producto del inventario y la cola de reabastecimiento
    def eliminar_producto(self, codigo):
        if not self.raiz:
            return "El inventario esta vacio"

        nodo = self.raiz.buscar(self.raiz, codigo)
        if not nodo:
            return f"No se encontro un producto con el codigo {codigo}"

        self.raiz = self.raiz.eliminar(self.raiz, codigo)
        mensaje_cola = self.cola_reabastecimiento.eliminar_producto(codigo)
        return f"El producto con código{codigo} eliminado del inventario. \n{mensaje_cola}"

    def listar_prioridades(self):
        return self.cola_reabastecimiento.listar_prioridades()

    def mostrar_avisos(self):
        return self.cola_reabastecimiento.mostrar_avisos()

    def limpiar_avisos(self):
        return self.cola_reabastecimiento.limpiar_avisos()
