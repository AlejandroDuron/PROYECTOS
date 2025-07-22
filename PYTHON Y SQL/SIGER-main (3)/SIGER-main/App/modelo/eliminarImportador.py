from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox, QApplication
import pymysql
from pymysql import Error
import sys

class EliminarImportador(QWidget):
    def __init__(self, id_importador, nombre, callback_actualizar):
        super().__init__()
        self.id_importador = id_importador
        self.callback_actualizar = callback_actualizar
        self.setWindowTitle("Eliminar Importador")
        self.setFixedSize(400, 150)

        layout = QVBoxLayout()
        layout.addWidget(QLabel(f"¿Seguro que desea eliminar a: {nombre}?"))
        layout.addWidget(QLabel("Se eliminarán también todos sus productos asociados."))

        btn_afirmar = QPushButton("Si, eliminar")
        btn_negar = QPushButton("Cancelar")
        btn_afirmar.clicked.connect(self.eliminar)
        btn_negar.clicked.connect(self.close)
        btn_volver = QPushButton("Volver")
        btn_volver.clicked.connect(self.close)
        layout.addWidget(btn_volver)

        layout.addWidget(btn_afirmar)
        layout.addWidget(btn_negar)
        self.setLayout(layout)

    def eliminar(self):
        try:
            conexion = pymysql.connect(
                host='localhost',
                user='root',
                password='1234',
                database='siger',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
            
            with conexion.cursor() as cursor:
                # Paso 1: Eliminar los detalles de factura relacionados con productos de este importador
                sql = """
                DELETE df FROM detalle_factura df
                JOIN productos p ON df.id_producto = p.id_producto
                WHERE p.id_importador = %s
                """
                cursor.execute(sql, (self.id_importador,))
                
                # Paso 2: Eliminar los productos de este importador
                sql = "DELETE FROM productos WHERE id_importador = %s"
                cursor.execute(sql, (self.id_importador,))
                
                # Paso 3: Finalmente eliminar el importador
                sql = "DELETE FROM importadores WHERE id_importador = %s"
                cursor.execute(sql, (self.id_importador,))
                
                conexion.commit()
                
            QMessageBox.information(self, "Éxito", "Importador y todos sus productos asociados eliminados correctamente")
            self.callback_actualizar()
            self.close()
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo completar la eliminación:\n{str(e)}")
        finally:
            if 'conexion' in locals() and conexion:
                conexion.close()