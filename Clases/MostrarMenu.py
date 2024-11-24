from SistemaInventario import SistemaInventario

#Inicializa el sistema de inventario
class MostrarMenu:
    def __init__(self):
        self.inventario = SistemaInventario()

    #Metodo para mostrar el menu de opciones
    def mostrar_menu(self):

        print("\n--- Menú de Opciones del Sistema de Inventario---")
        print("1. Agregar un producto")
        print("2. Editar un producto")
        print("3. Listar productos")
        print("4. Eliminar un producto")
        print("5. Listar productos de reabastecimiento prioritarios")
        print("6. Mostrar avisos de reabastecimiento")
        print("7. Limpiar avisos")
        print("8. Salir")

    #Metodo para ejecutar el menu de opciones
    def ejecutar (self):

        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.agregar_producto()
            elif opcion == "2":
                self.editar_producto()
            elif opcion == "3":
                self.listar_productos()
            elif opcion == "4":
                self.eliminar_producto()
            elif opcion == "5":
                self.listar_prioridades()
            elif opcion == "6":
                self.mostrar_avisos()
            elif opcion == "7":
                self.limpiar_avisos()
            elif opcion == "8":
                print("Saliendo del sistema...")
                break
            else:
                print("Opción inválida. Intente de nuevo.")

    #Metodo para agregar un producto al inventario
    def agregar_producto(self):

        print("\n--- Agregar un Producto ---")
        codigo = input("Ingrese el código del producto: ")
        nombre = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad del producto: "))
        precio = float(input("Ingrese el precio del producto: "))
        print(self.inventario.agregar_producto(codigo, nombre, cantidad, precio))


    #Metodo para editar un producto del inventario
    def editar_producto(self):

        print("\n--- Editar un Producto ---")
        codigo = input("Ingrese el código del producto a editar: ")
        nombre = input("Ingrese el nuevo nombre del producto: (Deje en blanco si no desea cambiarlo) ") or None
        cantidad = input(input("Ingrese la nueva cantidad del producto: (Deje en blanco si no desea cambiarlo) ") or None)
        cantidad = int(cantidad) if cantidad else None
        precio = input(input("Ingrese el nuevo precio del producto: (Deje en blanco si no desea cambiarlo) ") or None)
        precio = float(precio) if precio else None
        print(self.inventario.editar_producto(codigo, nombre, cantidad, precio))

    #Metodo para listar los productos del inventario
    def listar_productos(self):

        print("\n--- Listar Productos ---")
        print(self.inventario.listar_productos())

    #Metodo para eliminar un producto del inventario
    def eliminar_producto(self):

        print("\n--- Eliminar un Producto ---")
        codigo = input("Ingrese el código del producto a eliminar: ")
        print(self.inventario.eliminar_producto(codigo))

    #Metodo para listar los productos de reabastecimiento prioritarios
    def listar_prioridades(self):

        print("\n--- Listar Productos de Reabastecimiento Prioritarios ---")
        prioridades = self.inventario.listar_prioridades()
        if isinstance(prioridades, str):
            print("\n".join(prioridades))

        else:
            print(prioridades)

    #Metodo para mostrar los avisos de reabastecimiento
    def mostrar_avisos(self):

        print("\n--- Mostrar Avisos de Reabastecimiento ---")
        avisos = self.inventario.mostrar_avisos()
        if isinstance(avisos, str):
            print("\n".join(avisos))
        else:
            print(avisos)

    #Metodo para limpiar los avisos de reabastecimiento
    def limpiar_avisos(self):

        print("\n--- Limpiar Avisos de Reabastecimiento ---")
        print(self.inventario.limpiar_avisos())
