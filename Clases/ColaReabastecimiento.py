#Clase para gestionar la cola de reabastecimiento de productos con prioridad
import heapq #Biblioteca para implementar colas de prioridad

class ColaReabastecimiento:
    def __init__(self, limite_critico=10):

        self.cola = [] #Cola de prioridad para los productos
        self.pila_avisos = [] #Pila para los avisos generados
        self.limite_critico = limite_critico #Limite critico de productos en la cola

    def agregar(self, producto):
        if producto.cantidad <= self.limite_critico:
           heapq.heappush(self.cola, (producto.cantidad, producto))
           self.generar_aviso(producto)

    def generar_aviso(self, producto):
        aviso = f"El producto {producto.nombre} con código {producto.codigo} tiene {producto.cantidad} unidades"
        self.pila_avisos.append(aviso)

    #Método para obtener el producto con menor cantidad en la cola
    def getProductoReabastecimiento(self):
        return heapq.heappop(self.cola)[1] if self.cola else None

    def listar_prioridades(self):
        if not self.cola:
            return "No hay productos en la lista de reabastecimiento"

        #Crear una lista ordenada sin modificar la cola original
        lista_ordenada = sorted(self.cola, key=lambda x: x[0])
        return [
            f"{producto.nombre} (Código: {producto.codigo}, Cantidad: {producto.cantidad})"
            for _, producto in lista_ordenada
        ]

    def mostrar_avisos(self):
        return self.pila_avisos if self.pila_avisos else "No hay avisos generados"

    def limpiar_avisos(self):
        self.pila_avisos = []
        return "Avisos eliminados"

    #Metodo para eliminar un producto de la cola de reabastecimiento y sus avisos asociados
    def eliminar_producto(self, codigo):

        nueva_cola = [
            item for item in self.cola if item[1].codigo != codigo
        ]

        if len(nueva_cola) == len(self.cola):
            return f"El producto con código {codigo} no se encuentra en la lista de reabastecimiento"

        #Actualizar la cola con el nuevo orden despues de eliminar el producto
        self.cola = nueva_cola
        heapq.heapify(self.cola)

        #Eliinat el aviso relacionado con el producto
        self.pila_avisos = [
            aviso for aviso in self.pila_avisos
            if f"codigo {codigo}" not in aviso
        ]

        return f"El producto con código {codigo} ha sido eliminado de la lista de reabastecimiento"
