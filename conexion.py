import psycopg2

#función para conectar a la base de datos
def conectar_bd():
    try:
        #datos de conexión
        conexion = psycopg2.connect(
            host="localhost",
            database="inventario",
            user="postgres",
            password="1207",
            port="5432"
        )
        print("Conexión exitosa a la base de datos")
        return conexion
    except Exception as e:
        print("Error al conectar a la base de datos:", e)
        return None

""" # Probar la conexión
if __name__ == "__main__":
    conexion = conectar_bd()
 """