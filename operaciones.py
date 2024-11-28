import heapq  # Usamos heapq para la cola de prioridad
from conexion import conectar_bd  # Importamos la función para conectar a la base de datos
from arbol_avl import ArbolAVL  # Importamos el Árbol AVL desde el archivo arbol_avl.py


# Definir la clase Producto para manejar la información de los productos
class Producto:
    def __init__(self, nombre, codigo, cantidad, precio):
        self.nombre = nombre  # Nombre del producto
        self.codigo = codigo  # Código único del producto
        self.cantidad = cantidad  # Cantidad disponible en el inventario
        self.precio = precio  # Precio del producto


# Inicializar el Árbol AVL
arbol_avl = ArbolAVL()


# Función para insertar un producto en la base de datos y en el Árbol AVL
def insertar_producto(nombre, codigo, cantidad, precio):
    """
    Inserta un producto en la base de datos y en el Árbol AVL.
    Antes de insertar, verifica si ya existe un producto con el mismo código.
    """
    conexion = conectar_bd()
    if not conexion:
        return

    cursor = None  # Inicializamos cursor como None

    try:
        cursor = conexion.cursor()
        consulta_verificacion = "SELECT id FROM productos WHERE codigo = %s"
        cursor.execute(consulta_verificacion, (codigo,))
        producto_existente = cursor.fetchone()

        if producto_existente:
            print(f"El producto con código {codigo} ya existe (ID: {producto_existente[0]}). No se insertará.")
            return

        # Crear el producto y añadirlo al Árbol AVL
        producto = Producto(nombre, codigo, cantidad, precio)
        arbol_avl.insertar_producto(producto)  # Insertamos en el árbol AVL

        # Inserción en la base de datos
        consulta_insercion = """
        INSERT INTO productos (nombre, codigo, cantidad, precio)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(consulta_insercion, (nombre, codigo, cantidad, precio))
        conexion.commit()

        # Crear el producto y añadirlo al Árbol AVL
        producto = Producto(nombre, codigo, cantidad, precio)
        arbol_avl.insertar_producto(producto)  # Insertamos en el árbol AVL

        print("Producto insertado correctamente en la base de datos y en el Árbol AVL")
    except Exception as e:
        print("Error al insertar producto:", e)
    finally:
        if cursor:
            cursor.close()  # Solo cerramos el cursor si fue creado
        if conexion:
            conexion.close()  # Cerramos la conexión
        print("Conexión cerrada")


# Función para consultar todos los productos desde el Árbol AVL
def consultar_productos():
    print("Lista de productos ordenados por código:")
    arbol_avl.mostrar()  # Muestra los productos ordenados por código desde el Árbol AVL

    # Si el Árbol AVL no contiene los productos, consultar desde la base de datos
    conexion = conectar_bd()
    if not conexion:
        return

    try:
        cursor = conexion.cursor()
        consulta = "SELECT * FROM productos ORDER BY codigo;"  # Consulta para obtener los productos desde la base de datos
        cursor.execute(consulta)
        productos = cursor.fetchall()
        for producto in productos:
            print(
                f"ID: {producto[0]}, Nombre: {producto[1]}, Código: {producto[2]}, Cantidad: {producto[3]}, Precio: {producto[4]}")
    except Exception as e:
        print("Error al consultar productos:", e)
    finally:
        cursor.close()
        conexion.close()


# Función para actualizar la información de un producto en la base de datos y en el Árbol AVL
def actualizar_producto(id_producto, nombre=None, codigo=None, cantidad=None, precio=None):
    conexion = conectar_bd()
    if not conexion:
        return

    try:
        cursor = conexion.cursor()
        partes_consulta = []
        valores = []

        if nombre:
            partes_consulta.append("nombre = %s")
            valores.append(nombre)
        if codigo:
            partes_consulta.append("codigo = %s")
            valores.append(codigo)
        if cantidad:
            partes_consulta.append("cantidad = %s")
            valores.append(cantidad)
        if precio:
            partes_consulta.append("precio = %s")
            valores.append(precio)

        consulta = f"UPDATE productos SET {', '.join(partes_consulta)} WHERE id = %s"
        valores.append(id_producto)
        cursor.execute(consulta, tuple(valores))
        conexion.commit()

        # Si el producto se ha actualizado en la base de datos, también lo actualizamos en el Árbol AVL
        # (asumiendo que el Árbol AVL está cargado con productos previamente)
        producto_actualizado = Producto(nombre, codigo, cantidad, precio)
        arbol_avl.insertar_producto(producto_actualizado)  # Actualizar en el Árbol AVL

        print(f"Producto con ID {id_producto} actualizado correctamente en la base de datos")

    except Exception as e:
        print("Error al actualizar el producto:", e)
    finally:
        cursor.close()
        conexion.close()


# Función para eliminar un producto
def eliminar_producto(id_producto):
    conexion = conectar_bd()
    if not conexion:
        return

    try:
        cursor = conexion.cursor()
        consulta = "DELETE FROM productos WHERE id = %s"
        cursor.execute(consulta, (id_producto,))
        conexion.commit()

        # Eliminar el producto del Árbol AVL
        arbol_avl.eliminar_producto(id_producto)  # Eliminar del Árbol AVL
        print(f"Producto con ID {id_producto} eliminado correctamente.")
    except Exception as e:
        print("Error al eliminar el producto:", e)
    finally:
        cursor.close()
        conexion.close()
        print("Conexión cerrada")


# Función para eliminar todos los productos de la base de datos
def eliminar_todos_los_productos():
    conexion = conectar_bd()
    if not conexion:
        return

    try:
        cursor = conexion.cursor()
        consulta = "DELETE FROM productos;"  # Elimina todos los registros de la base de datos
        cursor.execute(consulta)
        conexion.commit()  # Guarda los cambios
        print("Todos los productos han sido eliminados de la base de datos.")

        # También vaciar el Árbol AVL (si es necesario)
        global arbol_avl  # Resetear el Árbol AVL
        arbol_avl = ArbolAVL()  # Re-inicializamos el Árbol AVL vacío
    except Exception as e:
        print("Error al eliminar todos los productos:", e)
    finally:
        cursor.close()
        conexion.close()
        print("Conexión cerrada")


# Función para generar alertas de inventario bajo
def alertas_inventario(umbral):
    conexion = conectar_bd()
    if not conexion:
        return

    try:
        cursor = conexion.cursor()
        consulta = "SELECT * FROM productos WHERE cantidad < %s"
        cursor.execute(consulta, (umbral,))
        productos = cursor.fetchall()
        print(f"Productos con cantidad menor a {umbral}:")
        for producto in productos:
            print(f"ID: {producto[0]}, Nombre: {producto[1]}, Cantidad: {producto[3]}")
    except Exception as e:
        print("Error al generar alertas:", e)
    finally:
        cursor.close()
        conexion.close()


# Función para registrar una venta y actualizar el inventario
def registrar_venta(producto_id, cantidad_vendida):
    conexion = conectar_bd()
    if not conexion:
        return

    try:
        cursor = conexion.cursor()
        consulta_producto = "SELECT cantidad FROM productos WHERE id = %s"
        cursor.execute(consulta_producto, (producto_id,))
        producto = cursor.fetchone()

        if not producto or producto[0] < cantidad_vendida:
            print("Stock insuficiente o producto no encontrado.")
            return

        consulta_venta = """
        INSERT INTO ventas (producto_id, cantidad_vendida)
        VALUES (%s, %s)
        """
        cursor.execute(consulta_venta, (producto_id, cantidad_vendida))

        consulta_actualizar = "UPDATE productos SET cantidad = cantidad - %s WHERE id = %s"
        cursor.execute(consulta_actualizar, (cantidad_vendida, producto_id))
        conexion.commit()
        print("Venta registrada correctamente")
    except Exception as e:
        print("Error al registrar la venta:", e)
    finally:
        cursor.close()
        conexion.close()


# Función para generar la cola de reabastecimiento
def generar_cola_reabastecimiento(umbral=10):
    conexion = conectar_bd()
    if not conexion:
        return

    try:
        cursor = conexion.cursor()
        consulta = "SELECT id, nombre, cantidad FROM productos WHERE cantidad < %s;"  # Cambiar el umbral según sea necesario
        cursor.execute(consulta, (umbral,))
        productos = cursor.fetchall()

        # Usamos una cola de prioridad basada en heapq
        cola_prioridad = []

        for producto in productos:
            # Insertamos en la cola con la cantidad como prioridad
            # heapq usa el primer valor como clave de comparación
            heapq.heappush(cola_prioridad, (producto[2], producto[0], producto[1]))  # (cantidad, id, nombre)

        print("Cola de reabastecimiento generada:")
        # Mostrar la cola de productos con baja cantidad
        while cola_prioridad:
            cantidad, id_producto, nombre = heapq.heappop(cola_prioridad)
            print(f"Producto: {nombre}, ID: {id_producto}, Cantidad actual: {cantidad}")

    except Exception as e:
        print("Error al generar la cola de reabastecimiento:", e)
    finally:
        cursor.close()
        conexion.close()


def actualizar_producto_cantidad(id_producto, nueva_cantidad):
    conexion = conectar_bd()
    if not conexion:
        return

    try:
        cursor = conexion.cursor()
        consulta_actualizacion = """
        UPDATE productos
        SET cantidad = %s
        WHERE id = %s
        """
        cursor.execute(consulta_actualizacion, (nueva_cantidad, id_producto))
        conexion.commit()
        print(f"Cantidad del producto con ID {id_producto} actualizada a {nueva_cantidad}")
    except Exception as e:
        print("Error al actualizar la cantidad:", e)
    finally:
        cursor.close()
        conexion.close()
