#Clase para gestionar la cola de reabastecimiento de productos con prioridad
import heapq #Biblioteca para implementar colas de prioridad

class ColaReabastecimiento:
    def __init__(self):
        self.cola = []

    def agregar(self, producto):
        heapq.heappush(self.cola, (producto.cantidad, producto))

    def getProductoReabastecimiento(self):
        return heapq.heappop(self.cola)[1] if self.cola else None