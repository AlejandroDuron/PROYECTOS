#pip install matplotlib
import sys
import pymysql
import matplotlib.pyplot as plt
from control.controlador_modelo import LabelAjustable, BotonPulsableModificable
import numpy as np
from PyQt6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QWidget, 
                            QComboBox, QMessageBox)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class ProductosVendidosWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Configuración de la ventana
        self.setWindowTitle("Productos Más Vendidos")
        self.setGeometry(100, 100, 900, 700)
        
        # Widget central y layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Título
        self.title_label = LabelAjustable(texto="Análisis de Productos Más Vendidos", tamaño= 18, estilo= "bold")
        
        # Controles
        self.controls_widget = QWidget()
        controls_layout = QVBoxLayout(self.controls_widget)
        
        # Selector de cantidad de productos a mostrar
        self.top_label = LabelAjustable(texto="Mostrar top")
        self.top_combo = QComboBox()
        self.top_combo.addItems(["3", "5", "10", "Todos"])
        self.top_combo.setCurrentIndex(1)  # Selecciona 5 por defecto
        
        # Botón para actualizar gráfico
        self.update_btn = BotonPulsableModificable(texto="Actualizar gráfico", color_base=None)
        self.update_btn.clicked.connect(self.actualizar_grafico)
        
        # Agregar controles al layout
        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.title_label)
        controls_layout.addWidget(self.top_label)
        controls_layout.addWidget(self.top_combo)
        controls_layout.addWidget(self.update_btn)
        layout.addWidget(self.controls_widget)
        
        # Gráfico
        self.figure = Figure(figsize=(10, 6), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)
        
        # Mostrar gráfico inicial
        self.actualizar_grafico()
    
    def obtener_datos_productos(self, limit=5):
        """Obtiene los datos de productos más vendidos de la base de datos"""
        try:
            connection = pymysql.connect(
                host='localhost',
                user='root',  # Cambiar por tus credenciales
                password='1234',  # Cambiar por tus credenciales
                database='siger'
            )
            
            with connection.cursor() as cursor:
                if limit == 0:  # 'Todos'
                    sql = """
                    SELECT 
                        p.nombre_producto,
                        SUM(df.cantidad) AS total_vendido
                    FROM 
                        productos p
                    JOIN 
                        detalle_factura df ON p.id_producto = df.id_producto
                    GROUP BY 
                        p.id_producto, p.nombre_producto
                    ORDER BY 
                        total_vendido DESC
                    """
                else:
                    sql = """
                    SELECT 
                        p.nombre_producto,
                        SUM(df.cantidad) AS total_vendido
                    FROM 
                        productos p
                    JOIN 
                        detalle_factura df ON p.id_producto = df.id_producto
                    GROUP BY 
                        p.id_producto, p.nombre_producto
                    ORDER BY 
                        total_vendido DESC
                    LIMIT %s
                    """
                
                cursor.execute(sql, (limit,) if limit != 0 else None)
                resultados = cursor.fetchall()
                
                if resultados:
                    productos = [item[0] for item in resultados]
                    ventas = [int(item[1]) for item in resultados]
                    return productos, ventas
                else:
                    return None, None
                    
        except pymysql.Error as e:
            QMessageBox.critical(self, "Error de base de datos", 
                                f"Error al obtener datos:\n{str(e)}")
            return None, None
        finally:
            if 'connection' in locals() and connection:
                connection.close()
    
    def actualizar_grafico(self):
        """Actualiza el gráfico con los datos más recientes"""
        # Obtener el límite seleccionado
        top_text = self.top_combo.currentText()
        limit = 0 if top_text == "Todos" else int(top_text)
        
        # Obtener datos
        productos, ventas = self.obtener_datos_productos(limit)
        
        if not productos or not ventas:
            QMessageBox.information(self, "Información", 
                                  "No hay datos de ventas disponibles.")
            return
        
        # Limpiar figura anterior
        self.figure.clear()
        
        # Crear gráfico de barras
        ax = self.figure.add_subplot(111)
        
        # Configurar colores (puedes personalizarlos)
        colors = plt.cm.viridis(np.linspace(0, 1, len(productos)))
        
        # Crear barras
        y_pos = np.arange(len(productos))
        bars = ax.bar(y_pos, ventas, align='center', alpha=0.7, color=colors)
        
        # Añadir etiquetas con los valores exactos
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                    f'{int(height)}',
                    ha='center', va='bottom')
        
        # Configurar ejes y título
        ax.set_xticks(y_pos)
        ax.set_xticklabels(productos, rotation=45, ha='right')
        ax.set_ylabel('Unidades Vendidas')
        ax.set_title(f'Top {len(productos)} Productos Más Vendidos')
        
        # Ajustar layout
        self.figure.tight_layout()
        
        # Actualizar canvas
        self.canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProductosVendidosWindow()
    window.show()
    sys.exit(app.exec())