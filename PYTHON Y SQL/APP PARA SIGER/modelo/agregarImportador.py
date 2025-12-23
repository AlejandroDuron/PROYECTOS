from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit,
    QPushButton, QMessageBox
)
import pymysql
from pymysql import Error

# Una clase para añadir un importador
class add_importador(QWidget):
    def __init__(self, parent_callback):
        super().__init__()
        self.setWindowTitle("Añadir Importador")
        self.setFixedSize(400, 200)
        self.parent_callback = parent_callback
        self.init_interfaz_agregar()

    
    def init_interfaz_agregar(self):

        layout = QVBoxLayout()
        self.nombre_ingresado = QLineEdit()
        self.contacto_ingresado = QLineEdit()
        btn_guardar = QPushButton("Guardar")
        btn_guardar.clicked.connect(self.agregar_importador)

        layout.addWidget(QLabel("Nombre del importador: "))
        layout.addWidget(self.nombre_ingresado)
        layout.addWidget(QLabel("Contacto: "))
        layout.addWidget(self.contacto_ingresado)
        layout.addWidget(btn_guardar)
        btn_volver = QPushButton("Volver")
        btn_volver.clicked.connect(self.close)
        layout.addWidget(btn_volver)

        self.setLayout(layout)

    def agregar_importador(self):
        nombre = self.nombre_ingresado.text().strip()
        contacto = self.contacto_ingresado.text().strip()

        if not nombre or not contacto:
            QMessageBox.warning(self, "Campos vacios", "Debe completar todos los campos para añadir un nuevo importador")
            return

        try:
            conexion = pymysql.connect(
                host ='localhost',
                database ='siger',
                user ='root',
                password ='1234',
                charset ='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )

            with conexion.cursor() as cursor:
                sql = "INSERT INTO importadores (nombre_importador, contacto) VALUES (%s, %s)"
                cursor.execute(sql, (nombre, contacto))
                conexion.commit()

            QMessageBox.information(self, "Exito", "Nuevo importador agregado correctamente")
            self.parent_callback()
            self.close()

        except pymysql.MySQLError as e:
            QMessageBox.critical(self, "Error", f"No se pudo insertar el importador\n{e}")

        finally:
            if conexion:
                conexion.close()
