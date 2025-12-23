from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QTableWidget, QTableWidgetItem, QPushButton, 
    QHeaderView, QMessageBox, QLabel
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
import pymysql
import sys


from modelo.agregarImportador import add_importador
from modelo.editarImportador import EditarImportador
from modelo.eliminarImportador import EliminarImportador


class ImportadoresWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.main_window = parent
        self.setWindowTitle("Proveedores")
        self.setFixedSize(1000, 600)
        self.setStyleSheet("background-color: white;")
        self.interfaz()
        self.main_layout = QVBoxLayout()
        self.load_data()

    def interfaz(self):
        try:
            self.main_layout = QVBoxLayout()
            
            # Título
            titulo = QLabel("Proveedores")
            titulo.setFont(QFont("Arial", 16, QFont.Weight.Bold))
            titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.main_layout.addWidget(titulo)
            
            titulo.setStyleSheet(
                "color: #1d4070;"
                "margin-bottom: 10px;"
            )
            
            self.setup_table()
            self.setup_buttons()
            self.setLayout(self.main_layout)
        except Exception as e:
            self.show_error(f"Error al configurar interfaz: {e}")

    def setup_table(self):
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["ID", "Nombre", "Contacto"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        
        # Para el formato:
        self.table.setStyleSheet("""
        QTableWidget {
            background-color: #f0f8ff;
            gridline-color: #cccccc;
            font-size: 12px;
        }
        QHeaderView::section {
            background-color: #357ABD;
            color: white;
            font-weight: bold;
            padding: 5px;
        }
        QTableWidget::item:selected {
            background-color: #a0c4ff;
            color: black;
        }
        """) ## Los "::" son para la herencia.
        
        self.main_layout.addWidget(self.table)

    def setup_buttons(self):
        button_layout = QHBoxLayout()
        
        # Nombre del botón, conexión:
        buttons = [
            ("Añadir", self.open_add_window),
            ("Editar", self.open_edit_window),
            ("Eliminar", self.open_delete_window),
            ("Volver", self.volver_menu)
        ]
        
        # Bucle:
        for text, callback in buttons:
            btn = QPushButton(text)
            btn.clicked.connect(callback)

            # Para el formato de los botones:
            btn.setStyleSheet(
                "background-color: #357ABD;"
                "color: white;"
                "padding: 8px 16px;"
                "border-radius: 8px;"
                "font-weight: bold;"
                "font-family: Arial;"
                "font-size: 13px;"
            )

            btn.setMinimumHeight(35)
            button_layout.addWidget(btn)
            
        self.main_layout.addLayout(button_layout)

    def volver_menu(self):
        if self.main_window: 
            self.main_window.show()
        self.close()

    def open_add_window(self):
        try:
            self.add_window = add_importador(self.load_data)
            self.add_window.show()
        except Exception as e:
            self.show_error(f"No se pudo abrir ventana: {e}")

    def open_edit_window(self):
        try:
            fila = self.table.currentRow()
            if fila < 0:
                QMessageBox.warning(self, "Advertencia", "Seleccione un importador")
                return
            
            id_importador = int(self.table.item(fila, 0).text())
            nombre = self.table.item(fila, 1).text()
            contacto = self.table.item(fila, 2).text()

            self.edit_window = EditarImportador(id_importador, nombre, contacto, self.load_data)
            self.edit_window.show()
        except Exception as e:
            self.show_error(f"No se pudo abrir editor: {e}")

    def open_delete_window(self):
        try:
            fila = self.table.currentRow()
            if fila < 0:
                QMessageBox.warning(self, "Advertencia", "Seleccione un importador")
                return
            
            id_importador = int(self.table.item(fila, 0).text())
            nombre = self.table.item(fila, 1).text()

            self.delete_window = EliminarImportador(id_importador, nombre, self.load_data)
            self.delete_window.show()
        except Exception as e:
            self.show_error(f"No se pudo abrir eliminador: {e}")

    def load_data(self):
        try:
            with pymysql.connect(
                host='localhost',
                user='root',
                password='1234',
                database='siger',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            ) as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT * FROM importadores")
                    data = cursor.fetchall()
                    
                    self.table.setRowCount(len(data))
                    for row_idx, row in enumerate(data):
                        self.table.setItem(row_idx, 0, QTableWidgetItem(str(row['id_importador'])))
                        self.table.setItem(row_idx, 1, QTableWidgetItem(row['nombre_importador']))
                        self.table.setItem(row_idx, 2, QTableWidgetItem(row['contacto']))
        except Exception as e:
            self.show_error(f"Error al cargar datos: {e}")

    def show_error(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setWindowTitle("Error")
        msg.setText(message)
        msg.setStyleSheet("""
            QMessageBox {
                font-family: Arial;
                font-size: 12px;
                background-color: white;
            }
            QMessageBox QLabel {
                color: black;
            }
        """)
        msg.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    
    # Para el formato de los Message:
    app.setStyleSheet("""
        QMessageBox {
            font-family: Arial;
            font-size: 12px;
        }
        QMessageBox QLabel {
            font-weight: bold;
            color: black;
        }
    """)
    
    try:
        # Verificación rápida de conexión
        pymysql.connect(
            host='localhost',
            user='root',
            password='1234'
        ).close()
        
        window = ImportadoresWindow()
        window.show()
        sys.exit(app.exec())
    except pymysql.MySQLError:
        QMessageBox.critical(None, "Error", "No se pudo conectar a la base de datos")
        sys.exit(1)
    except Exception as e:
        QMessageBox.critical(None, "Error", f"Error inesperado: {str(e)}")
        sys.exit(1)