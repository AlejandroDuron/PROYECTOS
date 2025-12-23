from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox, QHBoxLayout
from PyQt6.QtCore import Qt
import pymysql

class EliminarFactura(QWidget):
    def __init__(self, id_factura, callback_actualizar=None):
        super().__init__()
        self.id_factura = id_factura
        self.callback_actualizar = callback_actualizar
        self.setWindowTitle("Confirmar Eliminación")
        self.setFixedSize(400, 150)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout()
        
        lbl_mensaje = QLabel(f"¿Eliminar la factura #{self.id_factura}?")
        lbl_mensaje.setStyleSheet("font-size: 14px;")
        layout.addWidget(lbl_mensaje)
        
        btn_layout = QHBoxLayout()
        
        btn_confirmar = QPushButton("Confirmar")
        btn_confirmar.setStyleSheet("background-color: #ff4444; color: white;")
        btn_confirmar.clicked.connect(self.eliminar_factura)
        
        btn_cancelar = QPushButton("Cancelar")
        btn_cancelar.clicked.connect(self.close)
        
        btn_layout.addWidget(btn_confirmar)
        btn_layout.addWidget(btn_cancelar)
        layout.addLayout(btn_layout)
        
        self.setLayout(layout)
    
    def eliminar_factura(self):
        conn = None
        try:
            conn = pymysql.connect(
                host='localhost',
                user='root',
                password='1234',
                database='siger',
                cursorclass=pymysql.cursors.DictCursor
            )
            
            with conn.cursor() as cursor:
                # Eliminar registros relacionados
                cursor.execute("DELETE FROM deduccion_fiscal WHERE id_factura = %s", (self.id_factura,))
                cursor.execute("DELETE FROM detalle_factura WHERE id_factura = %s", (self.id_factura,))
                
                # Eliminar la factura principal
                cursor.execute("DELETE FROM factura WHERE id_factura = %s", (self.id_factura,))
                
                conn.commit()
                
                # Llamar al callback con True indicando éxito
                if self.callback_actualizar:
                    self.callback_actualizar(True)
                
                self.close()
                
        except pymysql.Error as e:
            QMessageBox.critical(
                self,
                "Error", 
                f"No se pudo eliminar la factura:\n{str(e)}"
            )
            if conn:
                conn.rollback()
            
            # Llamar al callback con False indicando fallo
            if self.callback_actualizar:
                self.callback_actualizar(False)
        finally:
            if conn:
                conn.close()