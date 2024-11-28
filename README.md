# Proyecto 2: Gestión de inventario

## Integrantes

- Estudiantes: Shirley Ramírez López - Juan Camilo Gañan Blandon
- Código: 29077 - 50831
- Universidad de Caldas
- Tercer semestre
- Ingeniería Informática
- Estructura de datos aplicadas

# Carpeta principal

- [Gestion-Inventario](https://github.com/JuanCamiloGanan/Gestion-de-Inventario/tree/main/Gestion-Inventario)

# Clases principales

- [arbol_avl](https://github.com/JuanCamiloGanan/Gestion-de-Inventario/blob/main/Gestion-Inventario/arbol_avl.py)
- [conexion](https://github.com/JuanCamiloGanan/Gestion-de-Inventario/blob/main/Gestion-Inventario/conexion.py)
- [operaciones](https://github.com/JuanCamiloGanan/Gestion-de-Inventario/blob/main/Gestion-Inventario/operaciones.py)
- [pruebas](https://github.com/JuanCamiloGanan/Gestion-de-Inventario/blob/main/Gestion-Inventario/pruebas.py)

# Información del desarrollo

## gestion-inventarios
Sistema de gestión de inventarios utilizando Árbol AVL y base de datos PostgreSQL
gestion-inventarios/
│
├── main.py                # Archivo principal del sistema

├── config.py              # Archivo de configuración para la base de datos

├── requirements.txt       # Lista de dependencias del proyecto

├── README.md              # Documentación del proyecto

├── .gitignore             # Archivos y carpetas que Git debe ignorar

    └── src/               # Carpeta para módulos y funciones del sistema
    ├── __init__.py        # Para definir un paquete de Python
    ├── inventario.py      # Lógica principal del inventario
    ├── conexion.py        # Conexión a la base de datos
    └── reportes.py        # Lógica para generación de reportes

# Sistema de Gestión de Inventarios con Árbol AVL y PostgreSQL

## Descripción
Este sistema permite gestionar el inventario de productos utilizando un Árbol AVL para almacenar y organizar los datos de manera eficiente en memoria. Los productos se sincronizan con una base de datos PostgreSQL, y se pueden realizar operaciones como agregar, actualizar y eliminar productos. Además, el sistema permite generar reportes de productos con bajo inventario y registrar ventas para actualizar automáticamente el stock.

### Características principales
- **Gestión de Inventarios:** Permite agregar, actualizar y eliminar productos en el inventario.
- **Base de Datos PostgreSQL:** Utiliza PostgreSQL para almacenar los productos y sus cantidades de manera persistente.
- **Árbol AVL:** Los productos están organizados en un Árbol AVL en memoria, lo que permite realizar operaciones eficientes de búsqueda, inserción y eliminación.
- **Generación de Reportes:** Genera reportes de productos con bajo inventario y productos vendidos recientemente.
- **Sincronización Automática:** Los cambios realizados en el Árbol AVL se sincronizan con la base de datos PostgreSQL.

## Requisitos

Este proyecto está desarrollado en Python y usa **PostgreSQL** como sistema de gestión de base de datos. Para ejecutar el proyecto, necesitarás tener los siguientes requisitos:

- **Python 3.x** (Recomendado Python 3.7 o superior)
- **PostgreSQL**: Asegúrate de tener PostgreSQL instalado y en funcionamiento en tu máquina.
- **psycopg2**: Paquete de Python para interactuar con PostgreSQL.

### Instalación de Requisitos

1. **Instala Python 3.x** (si no lo tienes aún):
    - Descargalo desde [python.org](https://www.python.org/downloads/).

2. **Instala PostgreSQL**:
    - Puedes descargar PostgreSQL desde [postgresql.org](https://www.postgresql.org/download/). Asegúrate de configurar la base de datos y crear un usuario para tu aplicación.

3. **Instala las dependencias del proyecto**:
    Clona el repositorio y navega al directorio del proyecto:
    ```bash
    git clone https://github.com/tuusuario/gestion-inventarios.git
    cd gestion-inventarios
    ```

    Luego, instala las dependencias necesarias:
    ```bash
    pip install -r requirements.txt
    ```

4. **Configura la base de datos PostgreSQL**:
    - Crea una base de datos en PostgreSQL:
    ```sql
    CREATE DATABASE gestion_inventarios;
    ```
    - Crea un usuario para la aplicación y asigna los permisos necesarios:
    ```sql
    CREATE USER tu_usuario WITH PASSWORD 'tu_contraseña';
    ALTER ROLE tu_usuario SET client_encoding TO 'utf8';
    ALTER ROLE tu_usuario SET default_transaction_isolation TO 'read committed';
    ALTER ROLE tu_usuario SET timezone TO 'UTC';
    GRANT ALL PRIVILEGES ON DATABASE gestion_inventarios TO tu_usuario;
    ```

    - Asegúrate de que los parámetros de conexión en el código apunten a esta base de datos.

## Configuración del Proyecto

1. Crea el archivo de configuración para la base de datos (por ejemplo, `config.py`) donde se definan los detalles de conexión:

```python
import psycopg2

def conectar():
    return psycopg2.connect(
        host="localhost",
        database="gestion_inventarios",
        user="tu_usuario",
        password="tu_contraseña"
    )

#Inicializa las tablas de la base de datos: Ejecuta el script para crear las tablas necesarias en PostgreSQL, por ejemplo
CREATE TABLE productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    cantidad INTEGER,
    precio DECIMAL
)

#Para ejecutar el sistema de gestión de inventarios, simplemente corre el archivo principal
python main.py

""" Opciones del Sistema
Insertar Producto: Permite agregar un nuevo producto al inventario.
Actualizar Producto: Permite modificar la cantidad o el precio de un producto existente.
Eliminar Producto: Permite eliminar un producto del inventario.
Ver Inventario: Muestra todos los productos en el inventario, ordenados por su ID.
Registrar Ventagg: Registra una venta y actualiza la cantidad del producto en el inventario.
Generar Reporte: Genera un reporte de productos con bajo inventario y ventas recientes. """

