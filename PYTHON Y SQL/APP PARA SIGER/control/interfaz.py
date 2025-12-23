from PyQt6.QtWidgets import QLabel, QLineEdit, QPushButton
from PyQt6.QtGui import QFont, QColor, QPalette
from PyQt6.QtCore import Qt

# Clase para crear labels con formato
class LabelAjustable(QLabel):
    def __init__(self, texto="", fuente="Arial", tamaño=12, 
                 color_texto=None, estilo="normal", 
                 alineacion=Qt.AlignmentFlag.AlignLeft, 
                 color_fondo=None, padding=None, altura_fija=None):
        super().__init__()
        
        self.configurar(
            # recibe valor como "" (string)
            texto_label = texto, # guarda el texto retornará el label
            # Recibe valor como "" (string)
            fuente_label = fuente, # modifica la fuente del texto
            # Recibe valor como 1 (int)
            tamaño_fuente_label = tamaño, # cambia el tamaño del texto
            # Recibe valor como "" (string)
            color_texto_label = color_texto, # cambia el color del texto
            # Recibe valor como "" (string) en ingles
            estilo_texto_label = estilo, # cambia el estilo del texto
            # Recibe valor como Qt.AligmentFlag. 
            alineacion_label = alineacion, # cambia la alineación del texto, inicial es izquierda
            # Recibe valor como "" (string)
            color_fondo_label = color_fondo, # cambia el color del fondo del texto
            # Recibe valor como 1 (int) o (arriba, derecha, abajo, izquierda)
            padding_label = padding, # cambia el padding del texto
            # Recibe valor como 1 (int)
            altura_fija_label = altura_fija # cambia la altura de forma obligatoria al texto
        )

    # Permite crear un label simple sin ningún cambio
    def crear_simple(self, texto=""):
        return LabelAjustable(texto=texto)

    def configurar(self, texto_label="", fuente_label="Arial", tamaño_fuente_label=12,
                 color_texto_label=None, estilo_texto_label="normal",
                 alineacion_label=Qt.AlignmentFlag.AlignLeft,
                 color_fondo_label=None, padding_label=None, altura_fija_label=None):
        # Modifica texto básico
        self.setText(texto_label)
        
        # Modifica fuente
        font = QFont(fuente_label, tamaño_fuente_label)
        if estilo_texto_label.lower() == "bold": 
            font.setBold(True)
        elif estilo_texto_label.lower() == "italic":
            font.setItalic(True)
        elif estilo_texto_label.lower() == "underline":
            font.setUnderline(True)
        self.setFont(font)

        # Alineación
        self.setAlignment(alineacion_label)

        # Color de texto
        if color_texto_label:
            self.setStyleSheet(f"color: {color_texto_label};")
            paleta = self.palette()
            paleta.setColor(QPalette.ColorRole.WindowText, QColor(color_texto_label))
            self.setPalette(paleta)

        # Color de fondo
        if color_fondo_label:
            self.setAutoFillBackground(True)
            paleta = self.palette()
            paleta.setColor(QPalette.ColorRole.Window, QColor(color_fondo_label))
            self.setPalette(paleta)
            self.setStyleSheet(self.styleSheet() + f"background-color: {color_fondo_label};")

        # Padding
        if padding_label:
            self.establecer_padding(padding_label)

        # Altura fija
        if altura_fija_label:
            self.setFixedHeight(altura_fija_label)

    def establecer_color_texto(self, color):
        self.setStyleSheet(f"color: {color};")
        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.WindowText, QColor(color))
        self.setPalette(paleta)

    def establecer_color_fondo(self, color):
        self.setAutoFillBackground(True)
        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(paleta)
        stylesheet = self.styleSheet()
        if "background-color:" in stylesheet:
            stylesheet = stylesheet.split("background-color:")[0]
        self.setStyleSheet(stylesheet + f"background-color: {color};")

    def establecer_padding(self, padding):
        stylesheet = self.styleSheet()
        if "padding:" in stylesheet:
            stylesheet = stylesheet.split("padding:")[0]
            
        if isinstance(padding, int):
            padding_str = f"{padding}px"
        elif isinstance(padding, (list, tuple)):
            padding_str = " ".join(f"{p}px" for p in padding)
        else:
            padding_str = str(padding)
            
        self.setStyleSheet(stylesheet + f"padding: {padding_str};")

##########################################################################################
# Clase para crear cajas de texto con formato
class cajaDeTextoModificable(QLineEdit):
    def __init__(self, altura = None, ancho = None, invisible = False, alineacion = Qt.AlignmentFlag.AlignLeft):
        super().__init__()
    
        self.configurar(
            altura_caja = altura,        # Altura fija del QLineEdit (píxeles)
            ancho_caja = ancho,          # Ancho fijo del QLineEdit (píxeles)
            invisible_caja = invisible,  # Si es True, muestra texto como contraseña (oculto)
            alineacion_caja = alineacion # Alineación del texto (Qt.AlignmentFlag)
        )

    def configurar(self, altura_caja = None, ancho_caja = None, invisible_caja = False, alineacion_caja = Qt.AlignmentFlag.AlignLeft):

        if invisible_caja:
            self.setEchoMode(QLineEdit.EchoMode.Password)
        
        self.setAlignment(alineacion_caja)

        if altura_caja:
            self.setFixedHeight(altura_caja)
        if ancho_caja:
            self.setFixedWidth(ancho_caja)

    def limpiar_caja(self):
        self.clear()

##########################################################################################

# Clase para crear botones con formato
class BotonPulsableModificable(QPushButton):
    def __init__(self, texto="", altura=None, ancho=None, radio=None, color_texto="black", color_base="lightblue", color_hover="blue", color_presionado="green", color_borde="black", tooltip="",  fuente="Arial", tamaño_fuente=10, estilo_fuente="normal"):
        super().__init__()
        
        # Configuración inicial con valores por defecto
        self.configurar(
            texto_boton = texto,            # Texto que mostrará el botón
            altura_boton = altura,          # Altura fija (píxeles)
            ancho_boton = ancho,            # Ancho fijo (píxeles)
            radio_boton = radio,            # Border radius (int o lista con 4 valores)
            color_texto_boton = color_texto, # Color del texto
            color_base_boton = color_base,   # Color normal del botón
            color_hover_boton = color_hover, # Color cuando el mouse pasa encima
            color_presionado_boton = color_presionado, # Color al hacer clic
            color_borde_boton = color_borde, # Color del borde
            tooltip_boton = tooltip,        # Texto emergente al pasar el mouse
            fuente_boton = fuente,          # Familia tipográfica
            tamaño_fuente_boton = tamaño_fuente, # Tamaño de fuente
            estilo_fuente_boton = estilo_fuente # Estilo: "normal", "bold", "italic" o combinaciones
        )

    def configurar(self, texto_boton="", altura_boton=None, ancho_boton=None, radio_boton=None, color_texto_boton="black", color_base_boton="lightblue", color_hover_boton="blue", color_presionado_boton="green", color_borde_boton="black", tooltip_boton="", fuente_boton="Arial", tamaño_fuente_boton=10, estilo_fuente_boton="normal"):
        
        # Modifica texto
        self.setText(texto_boton)
        
        # Modifica fuente
        font = QFont(fuente_boton, tamaño_fuente_boton)
        if "bold" in estilo_fuente_boton.lower():
            font.setBold(True)
        if "italic" in estilo_fuente_boton.lower():
            font.setItalic(True)
        self.setFont(font)
        
        # Configurar tooltip (información relacionada con el botón)
        if tooltip_boton:
            self.setToolTip(tooltip_boton)
        
        # Modifica las dimensiones
        if altura_boton:
            self.setFixedHeight(altura_boton)
        if ancho_boton:
            self.setFixedWidth(ancho_boton)
        
        # Construir botones en estilo CSS
        estilo = f"""
            QPushButton {{
                background-color: {color_base_boton};
                color: {color_texto_boton};
                border: 1px solid {color_borde_boton};
                font-family: '{fuente_boton}';
                font-size: {tamaño_fuente_boton}px;
                padding: 5px;
        """
        
        # Añadir un borde redondeado si se especifica
        if radio_boton:
            estilo += f"border-radius: {radio_boton}px;"
        
        estilo += """
            }
            QPushButton:hover {
                background-color: """ + color_hover_boton + """;
            }
            QPushButton:pressed {
                background-color: """ + color_presionado_boton + """;
            }
        """
        
        # Aplicar el estilo
        self.setStyleSheet(estilo)
