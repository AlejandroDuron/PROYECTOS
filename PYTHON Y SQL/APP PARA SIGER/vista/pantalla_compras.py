import sys
import pymysql
from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QTableWidget, QTableWidgetItem, QPushButton, 
    QLabel, QHeaderView, QMessageBox, QApplication
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from modelo.agregarcompras import AgregarFacturaView
from modelo.eliminarfactura import EliminarFactura
from modelo.editarCompras import EditarFactura
from vista.grafica_productos import ProductosVendidosWindow  # Importar la ventana de gráficos

class FacturasView(QMainWindow):
    def __init__(self, menu_principal=None):
        super().__init__()
        self.menu_principal = menu_principal
        self.setWindowTitle("Visualización de Facturas")
        self.setFixedSize(1000, 600)
        self.setStyleSheet("background-color: white; color:black")
        
        # Configuración de la base de datos
        self.db_config = {
            'host': 'localhost',
            'user': 'root',
            'password': '1234',
            'database': 'siger',
            'cursorclass': pymysql.cursors.DictCursor
        }
        self.conn = None
        self.cursor = None
        
        self.init_ui()
        self.cargar_facturas()  # Carga datos al iniciar
    
    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
       # Título
        titulo = QLabel("Listado de Facturas")
        titulo.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titulo.setStyleSheet("color: #1d4070; margin-bottom: 10px;")
        layout.addWidget(titulo)
        
        # Tabla de facturas
        self.tabla_facturas = QTableWidget()
        self.tabla_facturas.setColumnCount(5)
        self.tabla_facturas.setHorizontalHeaderLabels([
            "ID Factura", "ID Cliente", "Fecha", "Estado", "Monto"
        ])
        self.tabla_facturas.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        
        # Para el formato de la tabla:
        self.tabla_facturas.setStyleSheet("""
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
        layout.addWidget(self.tabla_facturas)
        
        # Fila de botones
        btn_layout = QHBoxLayout()
        
        buttons = [
            ("Agregar Factura", self.mostrar_agregar_factura),
            ("Mostrar Gráfico", self.mostrar_grafico),
            ("Actualizar", self.cargar_facturas),
            ("Editar", self.editar_factura),
            ("Eliminar", self.delete_factura),
            ("Volver", self.volver_al_menu)
        ]
        
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
            btn_layout.addWidget(btn)
            
        layout.addLayout(btn_layout)
    
    def cargar_facturas(self):
        try:
            # Cerrar conexión existente si hay una
            if self.cursor:
                self.cursor.close()
            if self.conn:
                self.conn.close()
                
            # Crear nueva conexión
            self.conn = pymysql.connect(**self.db_config)
            self.cursor = self.conn.cursor()
            
            self.cursor.execute("""
                SELECT id_factura, id_cliente, fecha_factura, estado_factura, monto 
                FROM factura 
                ORDER BY id_factura ASC
            """)
            facturas = self.cursor.fetchall()
            
            self.tabla_facturas.setRowCount(len(facturas))
            for row, factura in enumerate(facturas):
                self.tabla_facturas.setItem(row, 0, QTableWidgetItem(str(factura['id_factura'])))
                self.tabla_facturas.setItem(row, 1, QTableWidgetItem(str(factura['id_cliente'])))
                self.tabla_facturas.setItem(row, 2, QTableWidgetItem(str(factura['fecha_factura'])))
                self.tabla_facturas.setItem(row, 3, QTableWidgetItem(factura['estado_factura']))
                self.tabla_facturas.setItem(row, 4, QTableWidgetItem(f"{float(factura['monto']):.2f}"))
                
                for col in range(5):
                    item = self.tabla_facturas.item(row, col)
                    if item:
                        item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    
        except pymysql.Error as err:
            QMessageBox.critical(self, "Error", f"Error al cargar facturas:\n{err}")
    
    def mostrar_grafico(self):
        """Nuevo método para mostrar el gráfico de productos vendidos"""
        try:
            self.grafico_window = ProductosVendidosWindow()
            self.grafico_window.show()
        except Exception as e:
            self.show_error(f"No se pudo abrir el gráfico: {e}")

    # Resto de los métodos permanecen igual...
    def mostrar_agregar_factura(self):
        try:
            self.agregar_factura_view = AgregarFacturaView(self.conn)
            self.agregar_factura_view.show()
            self.hide()
        except Exception as e:
            self.show_error(f"No se pudo abrir la ventana de agregar factura: {e}")

    def delete_factura(self):
        try:
            fila = self.tabla_facturas.currentRow()
            if fila < 0:
                QMessageBox.warning(self, "Advertencia", "Seleccione una factura para eliminar")
                return
            
            id_factura = int(self.tabla_facturas.item(fila, 0).text())
            
            # Crear ventana de eliminación con callback
            self.delete_window = EliminarFactura(
                id_factura=id_factura,
                callback_actualizar=self.actualizar_despues_eliminar
            )
            self.delete_window.show()
        
        except Exception as e:
            self.show_error(f"No se pudo abrir la ventana de eliminación: {e}")
        
    def volver_al_menu(self):
        if self.menu_principal:
            self.menu_principal.show()
        self.close() 

    def actualizar_despues_eliminar(self, eliminado_exitoso):
        """Callback para actualizar después de eliminar"""
        if eliminado_exitoso:
            self.cargar_facturas()
            QMessageBox.information(self, "Éxito", "Factura eliminada correctamente")

    def editar_factura(self):
        try:
            fila = self.tabla_facturas.currentRow()
            if fila < 0:
                QMessageBox.warning(self, "Advertencia", "Seleccione una factura para editar")
                return
            
            id_factura = int(self.tabla_facturas.item(fila, 0).text())
            
            # Crear ventana de edición
            self.editar_view = EditarFactura(self.conn, id_factura)
            self.editar_view.show()
        
        except Exception as e:
            self.show_error(f"No se pudo abrir la ventana de edición: {e}")
        
    def show_error(self, message):
        QMessageBox.critical(self, "Error", message)
    
    def closeEvent(self, event):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FacturasView()
    window.show()
    sys.exit(app.exec())