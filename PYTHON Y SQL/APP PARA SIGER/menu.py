from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QFrame,
    QPushButton, QGraphicsDropShadowEffect, QMainWindow
)
from PyQt6.QtCore import Qt, QSize
from control.controlador_modelo import LabelAjustable, BotonPulsableModificable
from PyQt6.QtGui import QFont, QPixmap, QIcon, QColor
import sys
from pathlib import Path

from vista.pantalla_Importadores import ImportadoresWindow
from vista.pantalla_productos_admin import PantallaProductosAdmin
from vista.pantalla_compras import FacturasView
from control.controlador_cliente import ControladorCliente
from control.PyQt6_admin_user_seguimientomantenimiento import ControladorMantenimientos

class CircleMenu(QWidget):
    def __init__(self, username=None, rol=None):
        super().__init__()
        self.setWindowTitle("Menú Principal")
        self.setFixedSize(1000, 600)
        self.setStyleSheet("background-color: white; color: black;")

        # Layout vertical:
        main_layout = QVBoxLayout()
        main_layout.setSpacing(0)
        
        # Franjas arriba:
        celeste1 = QFrame()
        celeste1.setStyleSheet("""background-color: #4a90e2; height: 30px;
                              max-width: 300px;
                              border-top-right-radius: 15px;
                              border-bottom-right-radius: 15px;
                              margin-right: auto;""")
        celeste1.setFixedHeight(30)
        
        azul1 = QFrame()
        azul1.setStyleSheet("""background-color: #1d4070; height: 30px;
                              max-width: 200px;
                              border-top-right-radius: 15px;
                              border-bottom-right-radius: 15px;
                              margin-right: auto;""")
        azul1.setFixedHeight(30)

        main_layout.addWidget(celeste1)
        main_layout.addWidget(azul1)

        # Título
        title_container = QVBoxLayout()
        title = QLabel("Menú")
        title.setFont(QFont("Arial", 20, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        title_container.addWidget(title)
        main_layout.addLayout(title_container)
        main_layout.addSpacing(60)

        # Para obtener la ruta del archivo:
        ruta = Path(__file__).parent.parent
        
        # Botones
        botones_info = [
            ("Clientes", str(ruta / "App" / "icons" / "clientes.png")),
            ("Productos", str(ruta / "App" / "icons" / "productos.png")),
            ("Compras", str(ruta / "App" / "icons" / "compras.png")),
            ("Proveedores", str(ruta / "App" / "icons" / "proveedores.png")),
            ("Mantenimiento", str(ruta / "App" / "icons" / "importadores.png")),
        ]

        grid = QHBoxLayout()
        grid.setSpacing(40)

        for nombre, icono_path in botones_info:
            btn_layout = QVBoxLayout()
            btn_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)

            btn = BotonPulsableModificable(
                texto="", 
                altura=150,
                ancho=150,
                radio=75,
                color_base="#357ABD",
                color_hover="#2A4F7A",
                color_presionado="#1F1F1F",
                color_borde="#2A4F7A",
                color_texto="#FFFFFF",
                estilo_fuente="bold"
            )

            
            btn.setIcon(QIcon(icono_path))
            btn.setIconSize(QSize(240, 240))

            shadow = QGraphicsDropShadowEffect()
            shadow.setBlurRadius(8)
            shadow.setColor(QColor(0, 0, 0, 120))
            shadow.setOffset(2, 4)
            btn.setGraphicsEffect(shadow)

            # Conectar solo el botón de Importadores
            if nombre == "Proveedores":
                btn.clicked.connect(self.abrir_ventana_importadores)
            elif nombre == "Productos":
                btn.clicked.connect(self.abrir_ventana_productos)
            elif nombre == "Compras":
                btn.clicked.connect(self.abrir_ventana_compras)
            elif nombre == "Clientes":
                btn.clicked.connect(self.abrir_ventana_clientes)
            elif nombre == "Mantenimiento":
                btn.clicked.connect(self.abrir_ventana_mantenimiento)
            else:
                btn.clicked.connect(lambda _, n=nombre: print(f"Botón '{n}' clickeado"))

            text_buttons = LabelAjustable(
                texto=nombre.upper(),
                fuente="Arial",
                tamaño=10,
                estilo="bold",
                alineacion=Qt.AlignmentFlag.AlignCenter
            )
            text_buttons.setStyleSheet("color: black; margin-top: 3px; background: none; ")

            btn_layout.addWidget(btn)
            btn_layout.addWidget(text_buttons)
            grid.addLayout(btn_layout)

        main_layout.addLayout(grid)
        main_layout.addSpacing(90)

        # Franjas abajo
        celeste2 = QFrame()
        celeste2.setStyleSheet("""background-color: #4a90e2; height: 30px;
                              min-width: 300px;
                              border-top-left-radius: 15px;
                              border-bottom-left-radius: 15px;
                              margin-left: auto;""")
        celeste2.setFixedHeight(30)
        
        azul2 = QFrame()
        azul2.setStyleSheet("""background-color: #1d4070; height: 30px;
                              min-width: 200px;
                              border-top-left-radius: 15px;
                              border-bottom-left-radius: 15px;
                              margin-left: auto;""")
        azul2.setFixedHeight(30)

        main_layout.addWidget(azul2, alignment=Qt.AlignmentFlag.AlignRight)
        main_layout.addWidget(celeste2, alignment=Qt.AlignmentFlag.AlignRight)
        self.setLayout(main_layout)

    def abrir_ventana_importadores(self):
        self.ventana_importadores = ImportadoresWindow()
        self.ventana_importadores.show()
    def abrir_ventana_productos(self):
        self.ventana_productos = PantallaProductosAdmin()
        self.ventana_productos.show()
    def abrir_ventana_compras(self):
        self.ventana_compras = FacturasView() 
        self.ventana_compras.show()
    def abrir_ventana_clientes(self):
        self.ventana_clientes = ControladorCliente()
        self.ventana_clientes.vista_principal.show()
    def abrir_ventana_mantenimiento(self):
        try:
            self.ventana_mantenimiento = ControladorMantenimientos()
        except Exception as e:
            from PyQt6.QtWidgets import QMessageBox
            QMessageBox.critical(self, "Error", f"No se pudo abrir mantenimientos:\n{str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = CircleMenu()
    win.show()
    sys.exit(app.exec())
