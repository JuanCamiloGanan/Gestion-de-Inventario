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

    def getProductoReabastecimiento(self):
        return heapq.heappop(self.cola)[1] if self.cola else None

    def listar_prioridades(self):
        if not self.cola:
            return "No hay productos en la cola de reabastecimiento"

        #Crear una lista ordenada sin modificar la cola original
        lista_ordenada = sorted(self.cola, key=lambda x: x[0])
        return [
            f"{producto.nombre} (Código: {producto.codigo}, Cantidad: {cantidad})"
            for _, producto in lista_ordenada
        ]

    def mostrar_avisos(self):
        return self.pila_avisos if self.pila_avisos else "No hay avisos generados"

    def limpiar_avisos(self):
        self.pila_avisos = []
        return "Avisos eliminados"