from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QPushButton, 
                            QTableWidget, QTableWidgetItem, QLabel, QMessageBox,
                            QHeaderView)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class PantallaPrincipal(QWidget):
    def __init__(self, modelo):
        super().__init__()
        self.modelo = modelo
        self.cliente_seleccionado = None
        self.setWindowTitle("Clientes Registrados")
        self.setFixedSize(1000, 600)
        self.setStyleSheet("background-color: white;")
        self.initUI()
        self.cargar_clientes()

    def initUI(self):
        layout = QVBoxLayout()
        
        titulo = QLabel("Clientes Registrados")
        titulo.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titulo.setStyleSheet("color: #1d4070; margin-bottom: 10px;")
        layout.addWidget(titulo)

        self.tabla = QTableWidget()
        self.tabla.setColumnCount(5)
        self.tabla.setHorizontalHeaderLabels(["Nombre", "Dirección", "Teléfono", "Email", "Fecha Registro"])
        self.tabla.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tabla.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.tabla.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.tabla.cellClicked.connect(self.seleccionar_cliente)
        
        self.tabla.setStyleSheet("""
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
        """)
        
        layout.addWidget(self.tabla)

        botones_layout = QHBoxLayout()
        
        self.boton_agregar = QPushButton("Agregar Cliente")
        self.boton_editar = QPushButton("Editar Cliente")
        self.boton_eliminar = QPushButton("Eliminar Cliente")
        
        for btn in [self.boton_agregar, self.boton_editar, self.boton_eliminar]:
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
            botones_layout.addWidget(btn)
        
        self.boton_editar.setEnabled(False)
        self.boton_eliminar.setEnabled(False)
        
        layout.addLayout(botones_layout)
        self.setLayout(layout)

    def seleccionar_cliente(self, row, column):
        self.cliente_seleccionado = {
            'nombre': self.tabla.item(row, 0).text(),
            'direccion': self.tabla.item(row, 1).text(),
            'telefono': self.tabla.item(row, 2).text(),
            'email': self.tabla.item(row, 3).text(),
            'fecha_registro': self.tabla.item(row, 4).text(),
            'row': row
        }
        self.boton_editar.setEnabled(True)
        self.boton_eliminar.setEnabled(True)

    def cargar_clientes(self):
        try:
            clientes = self.modelo.obtener_clientes()
            self.tabla.setRowCount(len(clientes))
            
            for row, cliente in enumerate(clientes):
                self.tabla.setItem(row, 0, QTableWidgetItem(cliente['nombre']))
                self.tabla.setItem(row, 1, QTableWidgetItem(cliente['direccion']))
                self.tabla.setItem(row, 2, QTableWidgetItem(cliente['telefono']))
                self.tabla.setItem(row, 3, QTableWidgetItem(cliente['email']))
                
                fecha = str(cliente['fecha_registro'])
                fecha_item = QTableWidgetItem(fecha)
                fecha_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.tabla.setItem(row, 4, fecha_item)
            
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.setWindowTitle("Error")
            msg.setText(f"Error al cargar clientes: {str(e)}")
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