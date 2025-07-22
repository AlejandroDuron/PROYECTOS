import pymysql

class ModeloProductos:
    def __init__(self):
        try:
            self.conn = pymysql.connect(
                host='localhost',
                user='root',
                password='1234',
                database='siger',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
            self.cursor = self.conn.cursor()
        except pymysql.Error as e:
            raise Exception(f"Error al conectar a la base de datos: {str(e)}")

    def obtener_productos(self):
        try:
            consulta = """
            SELECT p.id_producto, p.nombre_producto, p.precio, p.descripcion,
            pr.nombre_proveedor, i.nombre_importador
            FROM productos p
            INNER JOIN proveedores pr ON p.id_proveedor = pr.id_proveedor
            INNER JOIN importadores i ON p.id_importador = i.id_importador
            """
            self.cursor.execute(consulta)
            return self.cursor.fetchall()
        except pymysql.Error as e:
            raise Exception(f"Error al obtener productos: {str(e)}")

    def insertar_producto(self, nombre, precio, descripcion, id_prov, id_imp):
        try:
            self.cursor.execute("""
                INSERT INTO productos (nombre_producto, precio, descripcion, id_proveedor, id_importador)
                VALUES (%s, %s, %s, %s, %s)
            """, (nombre, precio, descripcion, id_prov, id_imp))
            self.conn.commit()
            return True
        except pymysql.Error as e:
            self.conn.rollback()
            raise Exception(f"Error al insertar producto: {str(e)}")

    def eliminar_producto(self, id_producto):
        self.cursor.execute("DELETE FROM productos WHERE id_producto = %s", (id_producto,))
        self.conn.commit()

    def editar_producto(self, id_producto, nombre, precio, descripcion, id_prov, id_imp):
        self.cursor.execute("""
            UPDATE productos
            SET nombre_producto=%s, precio=%s, descripcion=%s, id_proveedor=%s, id_importador=%s
            WHERE id_producto=%s
        """, (nombre, precio, descripcion, id_prov, id_imp, id_producto))
        self.conn.commit()

    def __del__(self):
        try:
            if hasattr(self, 'cursor'):
                self.cursor.close()
            if hasattr(self, 'conn') and self.conn.open:
                self.conn.close()
        except Exception as e:
            print(f"Error al cerrar conexión: {str(e)}")