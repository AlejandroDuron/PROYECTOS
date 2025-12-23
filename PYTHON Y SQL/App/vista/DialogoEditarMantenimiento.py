from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QLabel, QLineEdit, 
    QDateEdit, QCheckBox, QDialogButtonBox
)
from PyQt6.QtCore import QDate
from datetime import datetime

class DialogoEditarMantenimiento(QDialog):
    def __init__(self, parent, id_mantenimiento, id_cliente, fecha_programada, encargado, completado):
        super().__init__(parent)
        self.setWindowTitle(f"Editar Mantenimiento ID: {id_mantenimiento}")
        self.setModal(True)
        
        layout = QVBoxLayout(self)
        
        # ID Cliente
        layout.addWidget(QLabel(f"ID Cliente: {id_cliente}"))
        
        # Fecha Programada
        layout.addWidget(QLabel("Fecha Programada:"))
        self.fecha_edit = QDateEdit()
        self.fecha_edit.setCalendarPopup(True)
        
        # Convertir fecha a QDate correctamente
        if isinstance(fecha_programada, str):
            qdate = QDate.fromString(fecha_programada, "yyyy-MM-dd")
        elif hasattr(fecha_programada, 'year'):  # Para objetos date o datetime
            qdate = QDate(fecha_programada.year, fecha_programada.month, fecha_programada.day)
        else:
            qdate = QDate.currentDate()
            
        self.fecha_edit.setDate(qdate)
        layout.addWidget(self.fecha_edit)
        
        # Encargado
        layout.addWidget(QLabel("Encargado:"))
        self.encargado_edit = QLineEdit(encargado)
        layout.addWidget(self.encargado_edit)
        
        # Completado
        self.completado_check = QCheckBox("Completado")
        self.completado_check.setChecked(bool(completado))
        layout.addWidget(self.completado_check)
        
        # Botones
        button_box = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)
    
    def obtener_valores(self):
        return {
            'fecha_programada': self.fecha_edit.date().toPyDate(),  # Devuelve datetime.date
            'encargado': self.encargado_edit.text(),
            'completado': self.completado_check.isChecked()
        }