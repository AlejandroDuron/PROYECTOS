import pymysql
import pymysql.cursors
from PyQt6.QtWidgets import QMessageBox

class ModeloBD:
    def __init__(self):
        try:
            self.conn = pymysql.connect(
                host='localhost',
                database='siger',
                user='root',
                password='1234',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
            self.cursor = self.conn.cursor()
            
            # Verificar y crear tabla si no existe
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS mantenimientos (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    id_cliente INT NOT NULL,
                    fecha_programada DATE NOT NULL,
                    direccion TEXT NOT NULL,
                    encargado VARCHAR(100) NOT NULL,
                    completado BOOLEAN DEFAULT FALSE,
                    CONSTRAINT `fk_cliente` FOREIGN KEY (`id_cliente`) REFERENCES `clientes` (`id_cliente`)
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci
            """)
            self.conn.commit()
            
        except pymysql.Error as e:
            QMessageBox.critical(None, "Error de conexión", 
                               f"No se pudo conectar a la base de datos:\n{str(e)}")
            raise

    def obtener_usuario(self, nombre_usuario):
        try:
            self.cursor.execute("""
                SELECT u.id, u.username, r.role_name
                FROM users u
                JOIN roles r ON u.role_id = r.id
                WHERE u.username = %s
            """, (nombre_usuario,))
            return self.cursor.fetchone()
        except pymysql.Error as e:
            QMessageBox.critical(None, "Error de consulta", 
                               f"Error al obtener usuario:\n{str(e)}")
            return None
        
    def obtener_mantenimientos(self):
        try:
            self.cursor.execute("""
                SELECT 
                    m.id,
                    m.id_cliente,
                    c.nombre AS nombre_cliente,
                    c.direccion AS direccion_cliente,
                    m.fecha_programada,
                    m.encargado,
                    m.completado
                FROM mantenimientos m
                JOIN clientes c ON m.id_cliente = c.id_cliente
                ORDER BY m.fecha_programada ASC
            """)
            resultados = self.cursor.fetchall()
            
            # Asegurar que las fechas sean objetos date
            for resultado in resultados:
                if isinstance(resultado['fecha_programada'], str):
                    from datetime import datetime
                    resultado['fecha_programada'] = datetime.strptime(resultado['fecha_programada'], '%Y-%m-%d').date()
                    
            return resultados
        except pymysql.Error as e:
            QMessageBox.critical(None, "Error de consulta", f"Error al obtener mantenimientos:\n{str(e)}")
            return []

    def crear_mantenimiento(self, id_cliente, fecha_programada, direccion, encargado):
        try:
            self.cursor.execute("""
                INSERT INTO mantenimientos 
                (id_cliente, fecha_programada, direccion, encargado)
                VALUES (%s, %s, %s, %s)
            """, (id_cliente, fecha_programada, direccion, encargado))
            self.conn.commit()
            return True
        except pymysql.Error as e:
            QMessageBox.critical(None, "Error de creación", 
                               f"Error al crear mantenimiento:\n{str(e)}")
            self.conn.rollback()
            return False

    def actualizar_mantenimiento(self, id, fecha_programada=None, encargado=None, completado=None):
        try:
            updates = []
            params = []
            
            if fecha_programada is not None:
                updates.append("fecha_programada = %s")
                params.append(fecha_programada)
            if encargado is not None:
                updates.append("encargado = %s")
                params.append(encargado)
            if completado is not None:
                updates.append("completado = %s")
                params.append(completado)
            
            if not updates:
                return False
                
            params.append(id)
            
            query = f"""
                UPDATE mantenimientos
                SET {', '.join(updates)}
                WHERE id = %s
            """
            
            self.cursor.execute(query, params)
            self.conn.commit()
            return True
        except pymysql.Error as e:
            QMessageBox.critical(None, "Error de actualización", 
                               f"Error al actualizar mantenimiento:\n{str(e)}")
            self.conn.rollback()
            return False

    def eliminar_mantenimiento(self, id):
        try:
            self.cursor.execute("""
                DELETE FROM mantenimientos
                WHERE id = %s
            """, (id,))
            self.conn.commit()
            return self.cursor.rowcount > 0
        except pymysql.Error as e:
            QMessageBox.critical(None, "Error de eliminación", 
                               f"Error al eliminar mantenimiento:\n{str(e)}")
            self.conn.rollback()
            return False

    def obtener_mantenimiento_por_id(self, id_mantenimiento):
        try:
            self.cursor.execute("""
                SELECT * FROM mantenimientos 
                WHERE id = %s
            """, (id_mantenimiento,))
            return self.cursor.fetchone()
        except pymysql.Error as e:
            QMessageBox.critical(None, "Error de consulta", 
                            f"Error al obtener mantenimiento:\n{str(e)}")
            return None

    def __del__(self):
        if hasattr(self, 'cursor'):
            self.cursor.close()
        if hasattr(self, 'conn') and self.conn.open:
            self.conn.close()