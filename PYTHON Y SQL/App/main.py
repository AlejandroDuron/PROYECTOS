""" Desarrollo de la aplicación para la empresa SIGER """
# Grupo KASTLE
# Integrantes:
#   Kathleen Abigail Argueta Gómez
#   Alejandro Javier Durón Rodríguez
#   Kevin Elías Luna Palacios
#   Lorena Esmeralda Mejía Ramos
#   Sheyla Alexandra Sarmiento Aragón

# Importaciones:
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, 
    QWidget, QLabel, QVBoxLayout, QStackedWidget
)
from PyQt6.QtCore import QTimer, QPropertyAnimation, QEasingCurve
from PyQt6.QtGui import QColor, QPalette
from control.login_principal import primerapantalla_log_in


class SplashScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cargando SIGER...")
        self.setFixedSize(700, 600)
        
        # Fondo con color personalizado
        self.setStyleSheet("""
            background-color: white;
            color: #4a90e2;
        """)
        
        layout = QVBoxLayout()
        self.label = QLabel("""Bienvenido al Sistema de
ingreso de datos de SIGER""")
        self.label.setStyleSheet("font-size: 40px; font-weight: bold; ")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)
        self.setLayout(layout)
        
        # Animación de fade out
        self.animation = QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(1000)  
        self.animation.setStartValue(1.0)
        self.animation.setEndValue(0.0)
        self.animation.setEasingCurve(QEasingCurve.Type.OutCubic)
        self.animation.finished.connect(self.close)
        
        # Iniciar secuencia: esperar 3 segundos animación
        QTimer.singleShot(3000, self.start_animation)
    
    def start_animation(self):
        self.animation.start()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de ingreso de datos de SIGER")
        self.setFixedSize(700, 600)
        
        # Contenedor principal con animación de entrada
        self.contenedor = QWidget()
        self.setCentralWidget(self.contenedor)
        
        # Configurar animación de entrada
        self.setWindowOpacity(0)  # Inicialmente transparente
        self.animation = QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(800)
        self.animation.setStartValue(0.0)
        self.animation.setEndValue(1.0)
        self.animation.setEasingCurve(QEasingCurve.Type.InOutQuad)

    def show(self):
        super().show()
        self.animation.start()

if __name__ == "__main__":
    app = QApplication([])
    
    # Mostrar splash screen
    splash = SplashScreen()
    splash.show()

    login_window = primerapantalla_log_in() 
    
    splash.destroyed.connect(login_window.show) # Para ver el login
    
    app.exec()