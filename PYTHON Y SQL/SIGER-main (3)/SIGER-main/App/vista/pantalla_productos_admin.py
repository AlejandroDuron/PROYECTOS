from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
    QTableWidget, QTableWidgetItem, QMessageBox, QInputDialog, QLabel,
    QHeaderView
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

from modelo.BD.bd_productos import ModeloProductos


class PantallaProductosAdmin(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.main_window = parent
        self.setWindowTitle("Productos")
        self.setFixedSize(1000, 600)
        self.setStyleSheet("background-color: white; color:black")
        
        self.modelo = ModeloProductos()
        self.interfaz()
        self.cargar_datos()

    def interfaz(self):
        try:
            self.main_layout = QVBoxLayout()
            
            # Título
            titulo = QLabel("Productos")
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
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(6)
        self.tabla.setHorizontalHeaderLabels([
            "ID", "Nombre", "Precio", "Descripción", "Proveedor", "Importador"
        ])
        self.tabla.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        
        # Para el formato:
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
        """) ## Los "::" son para la herencia.
        
        self.main_layout.addWidget(self.tabla)

    def setup_buttons(self):
        button_layout = QHBoxLayout()
        
        buttons = [
            ("Ingresar Producto", self.agregar_producto),
            ("Eliminar Producto", self.eliminar_producto),
            ("Editar Producto", self.editar_producto),
            ("Ver Tabla Completa", self.cargar_datos),
            ("Volver", self.volver_menu)
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
            button_layout.addWidget(btn)
            
        self.main_layout.addLayout(button_layout)

    def cargar_datos(self):
        try:
            productos = self.modelo.obtener_productos()
            self.tabla.setRowCount(0)  # Limpiar tabla
            
            if not productos:
                QMessageBox.information(self, "Información", "No hay productos registrados")
                return
                
            # Configurar columnas (solo una vez)
            if self.tabla.columnCount() == 0:
                self.tabla.setColumnCount(6)
                self.tabla.setHorizontalHeaderLabels([
                    "ID", "Nombre", "Precio", "Descripción", "Proveedor", "Importador"
                ])
            
            self.tabla.setRowCount(len(productos))
            
            for fila, producto in enumerate(productos):
                self.tabla.setItem(fila, 0, QTableWidgetItem(str(producto['id_producto'])))
                self.tabla.setItem(fila, 1, QTableWidgetItem(producto['nombre_producto']))
                self.tabla.setItem(fila, 2, QTableWidgetItem(str(producto['precio'])))
                self.tabla.setItem(fila, 3, QTableWidgetItem(producto['descripcion']))
                self.tabla.setItem(fila, 4, QTableWidgetItem(producto['nombre_proveedor']))
                self.tabla.setItem(fila, 5, QTableWidgetItem(producto['nombre_importador']))
                
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudieron cargar los productos: {str(e)}")

    def eliminar_producto(self):
        fila = self.tabla.currentRow()
        if fila < 0:
            QMessageBox.warning(self, "Error", "Seleccione una fila para eliminar.")
            return
        
        try:
            # Verifica que no estemos en la fila de encabezados
            if fila >= self.tabla.rowCount() or fila < 0:
                return
                
            id_item = self.tabla.item(fila, 0)
            if not id_item:  # Verifica que el item exista
                QMessageBox.warning(self, "Error", "No se encontró el producto seleccionado.")
                return
                
            id_producto = int(id_item.text())
            confirmacion = QMessageBox.question(
                self, 
                "Confirmar eliminación",
                f"¿Está seguro que desea eliminar el producto con ID {id_producto}?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )
            
            if confirmacion == QMessageBox.StandardButton.Yes:
                self.modelo.eliminar_producto(id_producto)
                self.cargar_datos()
                
        except ValueError:
            QMessageBox.critical(self, "Error", "El ID del producto no es válido.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Ocurrió un error al eliminar: {str(e)}")

    def agregar_producto(self):
        nombre, ok1 = QInputDialog.getText(self, "Nombre", "Nombre del producto:")
        if not ok1: return
        precio, ok2 = QInputDialog.getDouble(self, "Precio", "Precio del producto:")
        if not ok2: return
        descripcion, ok3 = QInputDialog.getText(self, "Descripción", "Descripción:")
        if not ok3: return
        id_prov, ok4 = QInputDialog.getInt(self, "ID proveedor", "ID del proveedor:")
        if not ok4: return
        id_imp, ok5 = QInputDialog.getInt(self, "ID importador", "ID del importador:")
        if not ok5: return

        self.modelo.insertar_producto(nombre, precio, descripcion, id_prov, id_imp)
        self.cargar_datos()

    def editar_producto(self):
        fila = self.tabla.currentRow()
        if fila < 0:
            QMessageBox.warning(self, "Error", "Seleccione un producto.")
            return

        id_producto = int(self.tabla.item(fila, 0).text())
        nombre = self.tabla.item(fila, 1).text()
        precio = float(self.tabla.item(fila, 2).text())
        descripcion = self.tabla.item(fila, 3).text()

        nuevo_nombre, _ = QInputDialog.getText(self, "Editar Nombre", "Nuevo nombre:", text=nombre)
        nuevo_precio, _ = QInputDialog.getDouble(self, "Editar Precio", "Nuevo precio:", value=precio)
        nueva_desc, _ = QInputDialog.getText(self, "Editar Descripción", "Nueva descripción:", text=descripcion)
        nuevo_prov, _ = QInputDialog.getInt(self, "Editar ID Proveedor", "Nuevo ID proveedor:")
        nuevo_imp, _ = QInputDialog.getInt(self, "Editar ID Importador", "Nuevo ID importador:")

        self.modelo.editar_producto(id_producto, nuevo_nombre, nuevo_precio, nueva_desc, nuevo_prov, nuevo_imp)
        self.cargar_datos()

    def volver_menu(self):
        if self.main_window: 
            self.main_window.show()
        self.close()


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
    app = QApplication([])
    
    # Para el formato de los Message:
    app.setStyleSheet("""
        QMessageBox {
            background-color: white;
            font-family: Arial;
            font-size: 12px;
        }
        QMessageBox QLabel {
            color: black;
            font-weight: bold;
        }
    """)
    
    ventana = PantallaProductosAdmin()
    ventana.show()
    app.exec()