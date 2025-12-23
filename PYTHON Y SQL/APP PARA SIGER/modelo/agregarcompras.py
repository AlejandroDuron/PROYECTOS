from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QFormLayout,
    QComboBox, QSpinBox, QLineEdit, QDateEdit,
    QTableWidget, QTableWidgetItem, QPushButton,
    QLabel, QMessageBox, QHeaderView
)
from PyQt6.QtCore import Qt, QDate
from PyQt6.QtGui import QFont
import pymysql

class AgregarFacturaView(QWidget):
    def __init__(self, db_connection):
        super().__init__()
        self.conn = db_connection
        self.cursor = self.conn.cursor()
        
        self.setWindowTitle("Agregar Nueva Factura")
        self.setGeometry(150, 150, 900, 600)
        
        self.init_ui()
        self.cargar_clientes()
        self.cargar_tipos()
        self.cargar_productos()
    
    def init_ui(self):
        layout = QVBoxLayout(self)
        
        # Formulario de cabecera
        form_header = QFormLayout()
        
        self.cliente_combo = QComboBox()
        self.fecha_input = QDateEdit(QDate.currentDate())
        self.fecha_input.setCalendarPopup(True)
        self.estado_combo = QComboBox()
        self.estado_combo.addItems(["Pendiente", "Pagada", "Cancelada"])
        
        form_header.addRow("Cliente:", self.cliente_combo)
        form_header.addRow("Fecha Factura:", self.fecha_input)
        form_header.addRow("Estado:", self.estado_combo)
        
        layout.addLayout(form_header)
        
        # Detalles de factura
        self.detalles_label = QLabel("Detalles de Factura:")
        self.detalles_label.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        layout.addWidget(self.detalles_label)
        
        self.detalles_table = QTableWidget()
        self.detalles_table.setColumnCount(6)
        self.detalles_table.setHorizontalHeaderLabels([
            "Tipo", "ID", "Descripción", "Precio Unitario", "Cantidad", "Subtotal"
        ])
        self.detalles_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        layout.addWidget(self.detalles_table)
        
        # Formulario para agregar detalles
        form_detalle = QFormLayout()
        
        self.tipo_combo = QComboBox()
        self.tipo_combo.addItems(["Producto", "Servicio"])
        self.tipo_combo.currentIndexChanged.connect(self.cambiar_tipo)
        
        self.item_combo = QComboBox()
        self.precio_unitario = QLineEdit()
        self.precio_unitario.setReadOnly(True)
        self.cantidad_spin = QSpinBox()
        self.cantidad_spin.setMinimum(1)
        self.cantidad_spin.setMaximum(9999)
        self.btn_agregar_detalle = QPushButton("Agregar Item")
        self.btn_agregar_detalle.clicked.connect(self.agregar_detalle)
        
        form_detalle.addRow("Tipo:", self.tipo_combo)
        form_detalle.addRow("Item:", self.item_combo)
        form_detalle.addRow("Precio Unitario:", self.precio_unitario)
        form_detalle.addRow("Cantidad:", self.cantidad_spin)
        form_detalle.addRow(self.btn_agregar_detalle)
        
        layout.addLayout(form_detalle)
        
        # Totales
        self.total_label = QLabel("Total: $0.00")
        self.total_label.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        layout.addWidget(self.total_label)
        
        self.iva_label = QLabel("IVA (13%): $0.00")
        self.iva_label.setFont(QFont("Arial", 10))
        layout.addWidget(self.iva_label)
        
        self.deduccion_label = QLabel("Deducción Fiscal: $0.00")
        self.deduccion_label.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        layout.addWidget(self.deduccion_label)
        
        # Botones
        btn_layout = QHBoxLayout()
        self.btn_guardar = QPushButton("Guardar Factura")
        self.btn_guardar.clicked.connect(self.guardar_factura)
        self.btn_limpiar = QPushButton("Limpiar")
        self.btn_limpiar.clicked.connect(self.limpiar_formulario)
        self.btn_volver = QPushButton("Volver")
        self.btn_volver.clicked.connect(self.volver_a_facturas)
        
        btn_layout.addWidget(self.btn_guardar)
        btn_layout.addWidget(self.btn_limpiar)
        btn_layout.addWidget(self.btn_volver)
        layout.addLayout(btn_layout)
        
        self.item_combo.currentIndexChanged.connect(self.actualizar_precio)
    
    def cargar_clientes(self):
        try:
            self.cursor.execute("SELECT id_cliente, nombre FROM clientes ORDER BY id_cliente")
            clientes = self.cursor.fetchall()
            
            self.cliente_combo.clear()
            for cliente in clientes:
                self.cliente_combo.addItem(
                    f"{cliente['id_cliente']} - {cliente['nombre']}",
                    userData=cliente['id_cliente']
                )
        except pymysql.Error as err:
            QMessageBox.critical(self, "Error", f"Error al cargar clientes:\n{err}")

    def cargar_tipos(self):
        self.tipo_combo.clear()
        self.tipo_combo.addItems(["Producto", "Servicio"])
    
    def cambiar_tipo(self):
        tipo = self.tipo_combo.currentText()
        if tipo == "Producto":
            self.cargar_productos()
        else:
            self.cargar_servicios()
    
    def cargar_servicios(self):
        try:
            self.cursor.execute("""
                SELECT id_servicio, nombre_servicio, precio 
                FROM servicios_profesionales 
                ORDER BY id_servicio
            """)
            servicios = self.cursor.fetchall()
            
            self.item_combo.clear()
            for servicio in servicios:
                self.item_combo.addItem(
                    f"{servicio['id_servicio']} - {servicio['nombre_servicio']}",
                    userData=(servicio['id_servicio'], servicio['precio'])
                )
            
            if servicios:
                self.actualizar_precio()
        except pymysql.Error as err:
            QMessageBox.critical(self, "Error", f"Error al cargar servicios:\n{err}")
    
    def cargar_productos(self):
        try:
            self.cursor.execute("""
                SELECT id_producto, nombre_producto, precio 
                FROM productos 
                ORDER BY id_producto
            """)
            productos = self.cursor.fetchall()
            
            self.item_combo.clear()
            for producto in productos:
                self.item_combo.addItem(
                    f"{producto['id_producto']} - {producto['nombre_producto']}",
                    userData=(producto['id_producto'], producto['precio'])
                )
            
            if productos:
                self.actualizar_precio()
        except pymysql.Error as err:
            QMessageBox.critical(self, "Error", f"Error al cargar productos:\n{err}")
    
    def actualizar_precio(self):
        if self.item_combo.currentIndex() >= 0:
            _, precio = self.item_combo.currentData()
            self.precio_unitario.setText(f"{precio:.2f}")
    
    def agregar_detalle(self):
        if self.item_combo.currentIndex() < 0:
            QMessageBox.warning(self, "Advertencia", "Seleccione un item")
            return
            
        try:
            tipo = self.tipo_combo.currentText()
            id_item, precio = self.item_combo.currentData()
            descripcion = self.item_combo.currentText().split(" - ")[1]
            cantidad = self.cantidad_spin.value()
            subtotal = cantidad * precio
            
            # Verificar si el item ya existe
            for row in range(self.detalles_table.rowCount()):
                if (self.detalles_table.item(row, 0).text() == tipo and 
                    self.detalles_table.item(row, 1).text() == str(id_item)):
                    # Actualizar cantidad existente
                    nueva_cantidad = int(self.detalles_table.item(row, 4).text()) + cantidad
                    nuevo_subtotal = float(self.detalles_table.item(row, 5).text()) + subtotal
                    
                    self.detalles_table.setItem(row, 4, QTableWidgetItem(str(nueva_cantidad)))
                    self.detalles_table.setItem(row, 5, QTableWidgetItem(f"{nuevo_subtotal:.2f}"))
                    self.actualizar_total()
                    return
            
            # Agregar nuevo item
            row = self.detalles_table.rowCount()
            self.detalles_table.insertRow(row)
            
            self.detalles_table.setItem(row, 0, QTableWidgetItem(tipo))
            self.detalles_table.setItem(row, 1, QTableWidgetItem(str(id_item)))
            self.detalles_table.setItem(row, 2, QTableWidgetItem(descripcion))
            self.detalles_table.setItem(row, 3, QTableWidgetItem(f"{precio:.2f}"))
            self.detalles_table.setItem(row, 4, QTableWidgetItem(str(cantidad)))
            self.detalles_table.setItem(row, 5, QTableWidgetItem(f"{subtotal:.2f}"))
            
            self.actualizar_total()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al agregar detalle:\n{e}")
    
    def actualizar_total(self):
        total = sum(
            float(self.detalles_table.item(row, 5).text()) 
            for row in range(self.detalles_table.rowCount())
        )
        self.total_label.setText(f"Total: ${total:.2f}")
        iva = total * 0.13
        self.iva_label.setText(f"IVA (13%): ${iva:.2f}")
        deduccion_fiscal = total + iva
        self.deduccion_label.setText(f"Deducción Fiscal: ${deduccion_fiscal:.2f}")
    
    def limpiar_formulario(self):
        self.cliente_combo.setCurrentIndex(0)
        self.fecha_input.setDate(QDate.currentDate())
        self.estado_combo.setCurrentIndex(0)
        self.detalles_table.setRowCount(0)
        self.total_label.setText("Total: $0.00")
        self.iva_label.setText("IVA (13%): $0.00")
        self.deduccion_label.setText("Deducción Fiscal: $0.00")
        if self.item_combo.count() > 0:
            self.item_combo.setCurrentIndex(0)
        self.cantidad_spin.setValue(1)
    
    def validar_datos(self):
        if self.cliente_combo.currentIndex() < 0:
            QMessageBox.warning(self, "Validación", "Seleccione un cliente")
            return False
            
        if self.detalles_table.rowCount() == 0:
            QMessageBox.warning(self, "Validación", "Agregue al menos un item")
            return False
            
        return True
    
    def guardar_factura(self):
        if not self.validar_datos():
            return
            
        try:
            # Obtener datos del formulario
            id_cliente = self.cliente_combo.currentData()
            fecha = self.fecha_input.date().toString("yyyy-MM-dd")
            estado = self.estado_combo.currentText()
            total = float(self.total_label.text().split("$")[1])
            iva = total * 0.13
            deduccion_fiscal = total + iva
            
            # Guardar cabecera en factura
            self.cursor.execute("""
                INSERT INTO factura (id_cliente, fecha_factura, estado_factura, monto)
                VALUES (%s, %s, %s, %s)
            """, (id_cliente, fecha, estado, total))
            id_factura = self.cursor.lastrowid
            
            # Crear tabla detalle_servicio si no existe
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS detalle_servicio (
                    id_detalle_servicio INT AUTO_INCREMENT PRIMARY KEY,
                    id_factura INT NOT NULL,
                    id_servicio INT NOT NULL,
                    cantidad INT NOT NULL,
                    subtotal DECIMAL(10,2) NOT NULL,
                    FOREIGN KEY (id_factura) REFERENCES factura(id_factura) ON DELETE CASCADE,
                    FOREIGN KEY (id_servicio) REFERENCES servicios_profesionales(id_servicio)
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci
            """)
            
            # Guardar detalles
            for row in range(self.detalles_table.rowCount()):
                tipo = self.detalles_table.item(row, 0).text()
                id_item = int(self.detalles_table.item(row, 1).text())
                cantidad = int(self.detalles_table.item(row, 4).text())
                subtotal = float(self.detalles_table.item(row, 5).text())
                
                if tipo == "Producto":
                    self.cursor.execute("""
                        INSERT INTO detalle_factura 
                        (id_factura, id_producto, cantidad, subtotal)
                        VALUES (%s, %s, %s, %s)
                    """, (id_factura, id_item, cantidad, subtotal))
                else:
                    self.cursor.execute("""
                        INSERT INTO detalle_servicio 
                        (id_factura, id_servicio, cantidad, subtotal)
                        VALUES (%s, %s, %s, %s)
                    """, (id_factura, id_item, cantidad, subtotal))
            
            # Guardar deducción fiscal
            self.cursor.execute("""
                INSERT INTO deduccion_fiscal 
                (id_factura, id_cliente, monto_deduccion)
                VALUES (%s, %s, %s)
            """, (id_factura, id_cliente, deduccion_fiscal))
            
            self.conn.commit()
            QMessageBox.information(
                self, "Éxito", 
                f"Factura guardada correctamente\n"
                f"Total: ${total:.2f}\n"
                f"IVA (13%): ${iva:.2f}\n"
                f"Deducción Fiscal: ${deduccion_fiscal:.2f}"
            )
            self.limpiar_formulario()
        except pymysql.Error as err:
            self.conn.rollback()
            QMessageBox.critical(self, "Error", f"Error al guardar factura:\n{err}")
        except Exception as e:
            self.conn.rollback()
            QMessageBox.critical(self, "Error", f"Error inesperado:\n{e}")
    
    def volver_a_facturas(self):
        from vista.pantalla_compras import FacturasView
        self.facturas_view = FacturasView()
        self.facturas_view.show()
        self.close()