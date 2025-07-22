import pymysql
from datetime import datetime

class ModeloCliente:
    def __init__(self, host='localhost', database='siger', user='root', password='1234'):
        self.connection_params = {
            'host': host,
            'database': database,
            'user': user,
            'password': password,
            'charset': 'utf8mb4',
            'cursorclass': pymysql.cursors.DictCursor
        }
        self._crear_tabla_si_no_existe()

    def _crear_tabla_si_no_existe(self):
        try:
            with self._get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("""
                        CREATE TABLE IF NOT EXISTS clientes (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            nombre VARCHAR(100) NOT NULL,
                            direccion VARCHAR(200),
                            telefono VARCHAR(20),
                            email VARCHAR(100),
                            fecha_registro DATE
                        )
                    """)
                    conn.commit()
        except pymysql.Error as e:
            print(f"Error al verificar/crear tabla: {e}")

    def _get_connection(self):
        try:
            return pymysql.connect(**self.connection_params)
        except pymysql.Error as e:
            print(f"Error de conexión: {e}")
            return None

    def insertar_cliente(self, nombre, direccion, telefono, email, fecha_registro):
        try:
            with self._get_connection() as conn:
                with conn.cursor() as cursor:
                    sql = """INSERT INTO clientes 
                            (nombre, direccion, telefono, email, fecha_registro)
                            VALUES (%s, %s, %s, %s, %s)"""
                    cursor.execute(sql, (nombre, direccion, telefono, email, fecha_registro))
                    conn.commit()
                    return True
        except pymysql.Error as e:
            print(f"Error al insertar cliente: {e}")
            return False
    def eliminar_cliente(self, email):
        try:
            with self._get_connection() as conn:
                with conn.cursor() as cursor:
                    sql = "DELETE FROM clientes WHERE email = %s"
                    cursor.execute(sql, (email,))
                    conn.commit()
                    return cursor.rowcount > 0
        except pymysql.Error as e:
            print(f"Error al eliminar cliente: {e}")
            return False

    def actualizar_cliente(self, email_original, nuevos_datos):
        try:
            with self._get_connection() as conn:
                with conn.cursor() as cursor:
                    sql = """UPDATE clientes SET 
                            nombre = %s, 
                            direccion = %s, 
                            telefono = %s, 
                            email = %s, 
                            fecha_registro = %s
                            WHERE email = %s"""
                    cursor.execute(sql, (
                        nuevos_datos['nombre'],
                        nuevos_datos['direccion'],
                        nuevos_datos['telefono'],
                        nuevos_datos['email'],
                        nuevos_datos['fecha_registro'],
                        email_original
                    ))
                    conn.commit()
                    return cursor.rowcount > 0
        except pymysql.Error as e:
            print(f"Error al actualizar cliente: {e}")
            return False

    def obtener_clientes(self):
        try:
            with self._get_connection() as conn:
                with conn.cursor() as cursor:
                    sql = "SELECT nombre, direccion, telefono, email, fecha_registro FROM clientes"
                    cursor.execute(sql)
                    return cursor.fetchall()
        except pymysql.Error as e:
            print(f"Error al obtener clientes: {e}")
            return []
