# pip install PyQt6
# pip install PyQt6 pymysql
import sys
pass
# Ahora las importaciones deben funcionar correctamente
from control.ModeloControlador import BotonPulsableModificable, cajaDeTextoModificable, LabelAjustable
from menu import CircleMenu
from PyQt6.QtWidgets import (
    QApplication, QWidget,
    QPushButton, QVBoxLayout,
    QMessageBox, QLineEdit
)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon
from pathlib import Path
import pymysql
from pymysql import Error
import sys
from menu import CircleMenu

class primerapantalla_log_in(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de registro e ingreso de datos")
        self.setFixedSize(1000, 600)
        self.setStyleSheet("background-color: white; color: black;") # Para fondo blanco con letras negras
        self.Base_para_trabajar()

    def Base_para_trabajar(self):
         # Encabezado
        encabezado = LabelAjustable(
            texto="Sistema de registro e ingreso de datos", 
            tamaño=10, 
            color_fondo="#4a90e2", 
            color_texto="white", 
            padding=8,
            alineacion=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter, 
            altura_fija=35
        )
        # Para el título
        title1 = LabelAjustable(
            texto="SIGER", 
            fuente="Arial", 
            tamaño=20, 
            estilo="bold", 
            alineacion=Qt.AlignmentFlag.AlignCenter
        )

        # Para el subtítulo
        subtitulo = LabelAjustable(
            texto="Sistema de Generación y Calidad de Energía, S.A. de C.V.", 
            alineacion=Qt.AlignmentFlag.AlignCenter, 
            fuente="Arial", 
            tamaño=10
        )
         # Campos de usuario y contraseña
        # Usuario
        user_label1 = LabelAjustable(
            texto = "Usuario", 
            tamaño = 9, 
            alineacion=Qt.AlignmentFlag.AlignCenter
        )
        self.user_input1 = cajaDeTextoModificable(
            altura = 30, 
            ancho = 350, 
            ejemplo_texto = "Ejemplo: admin", 
            borde_ancho = 2, 
            borde_color = "#4a90e2", 
            radio=5, 
            padding=5, 
            alineacion_texto_caja="center", 
            altura_fija=30
        )
        
        #Contraseña
        pass_label = LabelAjustable(
            "Contraseña", 
            tamaño=9, 
            alineacion=Qt.AlignmentFlag.AlignCenter
        )
        
        self.pass_input = cajaDeTextoModificable(
            invisible=True, 
            altura=30, 
            ancho=350, 
            borde_ancho=2, 
            borde_color="#4a90e2", 
            radio=5, 
            padding=5, 
            alineacion_texto_caja="left"
        )
# Botón para mostrar contraseña
        # Ruta del archivo:
        ruta = Path(__file__).parent.parent
        ojo_icono = str(ruta / "App" / "icons" / "ojo.png")

        self.ojo = QPushButton(self.pass_input)
        self.ojo.setIcon(QIcon(str(ojo_icono)))
        self.ojo.setIconSize(QSize(27, 27))
        self.ojo.setStyleSheet("margin-left: 313px;")
        self.ojo.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        
        self.ojo.clicked.connect(self.verContrasenna)
        self.password_visible = False

        # Botón de login
        btn_login = BotonPulsableModificable(
            texto="   Iniciar sesión   ", 
            fuente='Arial', 
            tamaño_fuente=12, 
            altura=35, 
            radio=12, 
            color_base="#4a90e2", 
            color_texto="white", 
            estilo_fuente="bold", 
            color_hover="#3a80d2", 
            color_presionado="#2a70c2", 
            color_borde="#4a90e2"
        )
        btn_login.clicked.connect(self.funcionamiento_LogIn)

        # Diseño del layout
        layout = QVBoxLayout()
        layout.addWidget(encabezado)
        layout.addSpacing(100)
        layout.addWidget(title1)
        layout.addWidget(subtitulo)
        layout.addSpacing(20)
        layout.addWidget(user_label1)
        layout.addWidget(self.user_input1, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(pass_label)
        layout.addWidget(self.pass_input, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addSpacing(20)
        layout.addWidget(btn_login, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addStretch()
        self.setLayout(layout)

    # Para ver la contraseña
    def verContrasenna(self):
        if self.password_visible:
            self.pass_input.setEchoMode(QLineEdit.EchoMode.Password)
        else:
            self.pass_input.setEchoMode(QLineEdit.EchoMode.Normal)
        self.password_visible = not self.password_visible


    # Para la autenticación de los usuarios:
    def conectarBasedeDatos(self):
        try:
            self.Conectardatos = pymysql.connect(
                host='localhost',
                database='siger',
                user='root',
                password='1234',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
            return self.Conectardatos
        except Error as e:
            QMessageBox.critical(
                self,
                "Error de conexión",
                f"No se pudo conectar a MySQL:\n{str(e)}"
            )
            return None
        
    def funcionamiento_LogIn(self):
        user = self.user_input1.text()
        password = self.pass_input.text()

        try:
            conector = self.conectarBasedeDatos()
            if conector is None:
                return
            
            with conector.cursor() as cursor:
                # Consulta modificada para comparar texto plano
                query = """SELECT u.username, r.role_name 
                        FROM users u 
                        JOIN roles r ON u.role_id = r.id 
                        WHERE username = %s AND password_hash = %s"""
                cursor.execute(query, (user, password))
                resultado = cursor.fetchone()
                
                if resultado:
                    QMessageBox.information(
                        self, 
                        "Acceso concedido", 
                        f"Bienvenido {resultado['username']}\nRol: {resultado['role_name']}"
                    )
                    self.abrir_menu_principal(resultado ["username"], resultado["role_name"])
                    # Aquí puedes abrir la ventana principal según el rol
                else:
                    QMessageBox.warning(self, "Error", "Usuario o contraseña incorrectos")
                    self.pass_input.clear()

        except Error as e:
            QMessageBox.critical(
                self, 
                "Error en la Base de Datos", 
                f"Error al verificar credenciales:\n{str(e)}"
            )
        finally:
            if conector and conector.open:
                conector.close()
    def abrir_menu_principal(self, username, rol):
        self.hide()
        self.menu_principal = CircleMenu(username, rol)
        self.menu_principal.show()
                

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = primerapantalla_log_in()
    window.show()
    sys.exit(app.exec())