""" from operaciones import insertar_producto, consultar_productos
from operaciones import registrar_venta, consultar_productos
from operaciones import generar_cola_reabastecimiento


if __name__ == "__main__":
    # Insertar productos para pruebas
    insertar_producto("Maiz", "6665", 10, 750.50)
    #insertar_producto("Manzana", "456", 5, 150.00)
    #insertar_producto("Arroz", "789", 20, 25.00)

    # Consultar productos para verificar las inserciones
    consultar_productos()


if __name__ == "__main__":
    # Registrar una venta de 3 unidades del producto con ID 1
    registrar_venta(1, 3)

    # Consultar productos para verificar que el inventario se actualizó correctamente
    consultar_productos()




if __name__ == "__main__":
    # Generar la cola de reabastecimiento
    generar_cola_reabastecimiento(umbral=20)  # Ajusta el umbral si es necesario


from operaciones import insertar_producto, consultar_productos, actualizar_producto

if __name__ == "__main__":
    # Paso 1: Insertar un producto para probar
    print("Insertando un producto de prueba...")
    insertar_producto("Tomate", "88803", 200, 150.0)  # Nombre, código, cantidad, precio

    # Paso 2: Consultar productos antes de la actualización
    print("\nProductos antes de la actualización:")
    consultar_productos()

    # Paso 3: Actualizar el producto
    print("\nActualizando el producto con ID 66 (en este caso es Maiz)...")
    actualizar_producto(id_producto=65, cantidad=30, precio=160.0)  # Cambiar la cantidad y el precio

    # Paso 4: Consultar productos después de la actualización
    print("\nProductos después de la actualización:")
    consultar_productos()
 """

from operaciones import consultar_productos, insertar_producto, actualizar_producto, eliminar_producto, \
    alertas_inventario, registrar_venta


def mostrar_menu():
    print("------ Sistema de Gestión de Inventario ------")
    print("1. Ver productos")
    print("2. Insertar producto")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Generar alertas de inventario bajo")
    print("6. Registrar venta")
    print("7. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion


def ejecutar_opcion(opcion):
    if opcion == "1":
        consultar_productos()
    elif opcion == "2":
        nombre = input("Ingrese el nombre del producto: ")
        codigo = input("Ingrese el código del producto: ")
        cantidad = int(input("Ingrese la cantidad: "))
        precio = float(input("Ingrese el precio: "))
        insertar_producto(nombre, codigo, cantidad, precio)
    elif opcion == "3":
        id_producto = int(input("Ingrese el ID del producto a actualizar: "))
        cantidad = int(input("Ingrese la nueva cantidad: "))
        precio = float(input("Ingrese el nuevo precio: "))
        actualizar_producto(id_producto, cantidad=cantidad, precio=precio)
    elif opcion == "4":
        id_producto = int(input("Ingrese el ID del producto a eliminar: "))
        eliminar_producto(id_producto)
    elif opcion == "5":
        umbral = int(input("Ingrese el umbral de inventario bajo: "))
        alertas_inventario(umbral)
    elif opcion == "6":
        producto_id = int(input("Ingrese el ID del producto para la venta: "))
        cantidad_vendida = int(input("Ingrese la cantidad vendida: "))
        registrar_venta(producto_id, cantidad_vendida)
    elif opcion == "7":
        print("Saliendo del sistema...")
        exit()
    else:
        print("Opción no válida.")


def iniciar_sistema():
    while True:
        opcion = mostrar_menu()  # Muestra el menú y obtiene la opción
        ejecutar_opcion(opcion)  # Ejecuta la acción correspondiente a la opción seleccionada


# Iniciar el sistema
iniciar_sistema()

