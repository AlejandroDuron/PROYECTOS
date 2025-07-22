from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem
from App.BD.bd_productos import ModeloProductos

class PantallaProductosUser(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Productos - Usuario")
        self.setFixedSize(900, 500)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.tabla = QTableWidget()
        layout.addWidget(self.tabla)

        self.modelo = ModeloProductos()
        self.cargar_datos()

    def cargar_datos(self):
        datos = self.modelo.obtener_productos()
        self.tabla.setColumnCount(6)
        self.tabla.setHorizontalHeaderLabels(["Código", "Nombre", "Precio / cu", "Descripción", "Proveedor", "Importador"])
        self.tabla.setRowCount(len(datos))

        for fila, producto in enumerate(datos):
            for col, valor in enumerate(producto):
                self.tabla.setItem(fila, col, QTableWidgetItem(str(valor)))

if __name__ == "__main__":
    app = QApplication([])
    ventana = PantallaProductosUser()
    ventana.show()
    app.exec()