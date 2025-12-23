from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtCore import Qt
import pymysql

class EditarImportador(QWidget):
    def __init__(self, id_importador, nombre, contacto, callback_actualizar):
        super().__init__()
        self.id_importador = id_importador
        self.callback_actualizar = callback_actualizar
        
        self.setWindowTitle(f"Editar Importador - ID: {id_importador}")
        self.setFixedSize(400, 200)
        
        layout = QVBoxLayout()
        
        # Campos de entrada
        layout.addWidget(QLabel("Nombre del Importador:"))
        self.input_nombre = QLineEdit(nombre)
        layout.addWidget(self.input_nombre)
        
        layout.addWidget(QLabel("Contacto:"))
        self.input_contacto = QLineEdit(contacto)
        layout.addWidget(self.input_contacto)
        
        # Botones
        btn_guardar = QPushButton("Guardar cambios")
        btn_guardar.clicked.connect(self.guardar)
        
        btn_volver = QPushButton("Volver")
        btn_volver.clicked.connect(self.close)
        
        layout.addWidget(btn_guardar)
        layout.addWidget(btn_volver)
        
        self.setLayout(layout)
        self.show()  # Asegurar que la ventana se muestre
        
    def guardar(self):
        nuevo_nombre = self.input_nombre.text().strip()
        nuevo_contacto = self.input_contacto.text().strip()

        if not nuevo_nombre or not nuevo_contacto:
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios")
            return

        try:
            with pymysql.connect(
                host='localhost',
                user='root',
                password='1234',
                database='siger',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            ) as conexion:
                with conexion.cursor() as cursor:
                    sql = "UPDATE importadores SET nombre_importador=%s, contacto=%s WHERE id_importador=%s"
                    cursor.execute(sql, (nuevo_nombre, nuevo_contacto, self.id_importador))
                    conexion.commit()
                    
            QMessageBox.information(self, "Éxito", "Cambios guardados correctamente")
            self.callback_actualizar()
            self.close()
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudieron guardar los cambios:\n{str(e)}")