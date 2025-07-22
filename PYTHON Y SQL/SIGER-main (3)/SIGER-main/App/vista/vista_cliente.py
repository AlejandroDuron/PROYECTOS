from PyQt6.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton, 
                            QVBoxLayout, QHBoxLayout, QMessageBox, QDateEdit)
from PyQt6.QtCore import Qt, QDate
from PyQt6.QtGui import QFont

class VistaCliente(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.main_window = parent
        self.setWindowTitle("Registro de Cliente")
        self.setFixedSize(1000, 600)
        self.setStyleSheet("background-color: white;")
        self.interfaz()

    def interfaz(self):
        main_layout = QVBoxLayout()
        
        # Título
        titulo = QLabel("Registro de Cliente")
        titulo.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titulo.setStyleSheet(
            "color: #1d4070;"
            "margin-bottom: 20px;"
        )
        main_layout.addWidget(titulo)
        
        # Campos del formulario
        form_layout = QVBoxLayout()
        
        self.inputs = {}
        campos = [
            ("Nombre", QLineEdit()),
            ("Dirección", QLineEdit()),
            ("Teléfono", QLineEdit()),
            ("Email", QLineEdit()),
            ("Fecha de Registro", QDateEdit(QDate.currentDate()))
        ]
        
        for label_text, input_field in campos:
            label = QLabel(f"{label_text}:")
            label.setStyleSheet("""
                font-weight: bold;
                color: #34495e;
                font-size: 12px;
            """)
            
            input_field.setStyleSheet("""
                QLineEdit, QDateEdit {
                    padding: 8px;
                    border: 1px solid #B0C4DE;
                    border-radius: 4px;
                    background-color: #f0f8ff;
                    color: black;
                    font-size: 12px;
                }
                QLineEdit:focus, QDateEdit:focus {
                    border: 1px solid #357ABD;
                }
            """)
            
            form_layout.addWidget(label)
            form_layout.addWidget(input_field)
            self.inputs[label_text] = input_field

        main_layout.addLayout(form_layout)

        # Botones
        btn_layout = QHBoxLayout()
        
        self.boton_guardar = QPushButton("Guardar Cliente")
        self.boton_limpiar = QPushButton("Limpiar Campos")
        self.boton_volver = QPushButton("Volver")
        
        # Formato botones
        for btn in [self.boton_guardar, self.boton_limpiar, self.boton_volver]:
            btn.setStyleSheet("""
                background-color: #357ABD;
                color: white;
                padding: 8px 16px;
                border-radius: 8px;
                font-weight: bold;
                font-family: Arial;
                font-size: 13px;
            """)
            btn.setMinimumHeight(35)
            btn_layout.addWidget(btn)
        
        main_layout.addLayout(btn_layout)
        self.setLayout(main_layout)

        # Conexiones de botones
        self.boton_guardar.clicked.connect(self.guardar_cliente)
        self.boton_limpiar.clicked.connect(self.limpiar_campos)
        self.boton_volver.clicked.connect(self.volver_menu)

    def volver_menu(self):
        if self.main_window: 
            self.main_window.show()
        self.close()

    def guardar_cliente(self):
        try:
            datos = self.obtener_datos()
            # Aquí iría la lógica para guardar
            self.mostrar_mensaje("Éxito", "Cliente guardado correctamente")
        except Exception as e:
            self.mostrar_mensaje("Error", f"Error al guardar: {e}", "error")

    def limpiar_campos(self):
        for field in self.inputs.values():
            if isinstance(field, QLineEdit):
                field.clear()
            elif isinstance(field, QDateEdit):
                field.setDate(QDate.currentDate())

    def obtener_datos(self):
        return {
            'nombre': self.inputs['Nombre'].text().strip(),
            'direccion': self.inputs['Dirección'].text().strip(),
            'telefono': self.inputs['Teléfono'].text().strip(),
            'email': self.inputs['Email'].text().strip(),
            'fecha_registro': self.inputs['Fecha de Registro'].date().toString("yyyy-MM-dd")
        }

    def mostrar_mensaje(self, titulo, mensaje, tipo="info"):
        msg = QMessageBox()
        msg.setWindowTitle(titulo)
        msg.setText(mensaje)
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
        
        if tipo == "error":
            msg.setIcon(QMessageBox.Icon.Critical)
        else:
            msg.setIcon(QMessageBox.Icon.Information)
            
        msg.exec()

if __name__ == "__main__":
    from PyQt6.QtWidgets import QApplication
    import sys
    
    app = QApplication(sys.argv)
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
    
    window = VistaCliente()
    window.show()
    sys.exit(app.exec())