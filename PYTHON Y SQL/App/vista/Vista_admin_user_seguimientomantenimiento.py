from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QScrollArea,
    QHBoxLayout, QFrame, QMessageBox, QDateEdit, QSizePolicy
)
from PyQt6.QtCore import Qt, QDate
from PyQt6.QtGui import QFont

class VistaMantenimientos(QWidget):
    def __init__(self, mantenimientos, controlador=None):
        super().__init__()
        self.controlador = controlador
        self.setWindowTitle('Seguimiento de Mantenimientos')
        self.setMinimumSize(800, 600)
        self.setStyleSheet("""
            QWidget {
                background-color: #f5f5f5;
                font-family: Arial;
            }
            QFrame {
                background-color: white;
                border-radius: 8px;
                border: 1px solid #ddd;
            }
            QLabel {
                color: #333;
            }
            QPushButton {
                background-color: #4a90e2;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #3a80d2;
            }
        """)
        
        self.init_ui(mantenimientos)
        
    def init_ui(self, mantenimientos):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)
        
        # Header
        header = QLabel("Seguimiento de Mantenimientos")
        header.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header.setStyleSheet("color: #1d4070; margin-bottom: 20px;")
        main_layout.addWidget(header)
        
        # Scroll area for maintenance records
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.Shape.NoFrame)
        
        content = QWidget()
        content_layout = QVBoxLayout(content)
        content_layout.setSpacing(15)
        content_layout.setContentsMargins(10, 10, 10, 10)
        
        if not mantenimientos:
            no_data_label = QLabel("No hay registros de mantenimientos disponibles")
            no_data_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            no_data_label.setStyleSheet("font-size: 14px; color: #666;")
            content_layout.addWidget(no_data_label)
        else:
            for m in mantenimientos:
                card = self.create_maintenance_card(m)
                content_layout.addWidget(card)
        
        content_layout.addStretch()
        scroll.setWidget(content)
        main_layout.addWidget(scroll)
        
        # Footer buttons
        footer_layout = QHBoxLayout()
        footer_layout.addStretch()
        
        close_btn = QPushButton("Cerrar")
        close_btn.setFixedWidth(120)
        close_btn.clicked.connect(self.close)
        
        footer_layout.addWidget(close_btn)
        main_layout.addLayout(footer_layout)
    
    def create_maintenance_card(self, maintenance_data):
        # Asegurarse de que tenemos los campos correctos
        id_mant = maintenance_data['id']
        id_cli = maintenance_data['id_cliente']
        nombre = maintenance_data['nombre_cliente']
        direccion = maintenance_data['direccion_cliente']
        fecha_programada = maintenance_data['fecha_programada']
        encargado = maintenance_data['encargado']
        completado = maintenance_data['completado']
        
        # Convertir fecha si es necesario
        if isinstance(fecha_programada, str):
            from datetime import datetime
            fecha_programada = datetime.strptime(fecha_programada, '%Y-%m-%d').date()
        
        card = QFrame()
        card.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        card_layout = QVBoxLayout(card)
        card_layout.setSpacing(10)
        card_layout.setContentsMargins(15, 15, 15, 15)
        
        # Client info
        client_header = QLabel(f"{nombre} (ID: {id_cli})")
        client_header.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        client_header.setStyleSheet("color: #357ABD;")
        
        # Details layout
        details_layout = QVBoxLayout()
        details_layout.setSpacing(5)
        
        address_label = QLabel(f"Dirección: {direccion}")
        programada_label = QLabel(f"Fecha programada: {fecha_programada.strftime('%d/%m/%Y')}")
        responsible = QLabel(f"👤 Encargado: {encargado}")
        status = QLabel(f"Completado: {'Sí' if completado else 'No'}")
        
        details_layout.addWidget(address_label)
        details_layout.addWidget(programada_label)
        details_layout.addWidget(responsible)
        details_layout.addWidget(status)
        
        # Buttons layout
        buttons_layout = QHBoxLayout()
        buttons_layout.addStretch()
        
        edit_btn = QPushButton("Editar")
        edit_btn.setFixedWidth(100)
        edit_btn.clicked.connect(lambda: self.controlador.editar_mantenimiento(id_mant))
        
        delete_btn = QPushButton("Eliminar")
        delete_btn.setFixedWidth(100)
        delete_btn.setStyleSheet("background-color: #e74c3c;")
        delete_btn.clicked.connect(lambda: self.controlador.eliminar_mantenimiento(id_mant))
        
        buttons_layout.addWidget(edit_btn)
        buttons_layout.addWidget(delete_btn)
        
        card_layout.addWidget(client_header)
        card_layout.addLayout(details_layout)
        card_layout.addLayout(buttons_layout)
        
        return card