from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QFormLayout,
    QComboBox, QSpinBox, QLineEdit, QDateEdit,
    QTableWidget, QTableWidgetItem, QPushButton,
    QLabel, QMessageBox, QHeaderView
)
from PyQt6.QtCore import Qt, QDate
from PyQt6.QtGui import QFont
import pymysql

class EditarFactura(QWidget):
    def __init__(self, db_connection, id_factura):
        super().__init__()
        
        # Validación robusta del ID de factura
        try:
            self.id_factura = int(id_factura)
            if self.id_factura <= 0:
                raise ValueError("ID debe ser positivo")
        except (ValueError, TypeError):
            QMessageBox.critical(None, "Error", "ID de factura inválido. Debe ser un número positivo.")
            self.close()
            return
            
        self.conn = db_connection
        try:
            self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        except pymysql.Error as e:
            QMessageBox.critical(None, "Error", f"No se pudo establecer conexión con la base de datos:\n{str(e)}")
            self.close()
            return
        
        self.setWindowTitle(f"Editar Factura #{self.id_factura}")
        self.setGeometry(150, 150, 900, 600)
        
        self.init_ui()
        self.cargar_clientes()
        self.cargar_tipos()
        self.cargar_datos_factura()
    
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
        
        # Formulario para agregar/modificar detalles
        form_detalle = QFormLayout()
        
        # Selector de tipo (Producto/Servicio)
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
        self.btn_eliminar_detalle = QPushButton("Eliminar Seleccionado")
        self.btn_eliminar_detalle.clicked.connect(self.eliminar_detalle)
        
        form_detalle.addRow("Tipo:", self.tipo_combo)
        form_detalle.addRow("Item:", self.item_combo)
        form_detalle.addRow("Precio Unitario:", self.precio_unitario)
        form_detalle.addRow("Cantidad:", self.cantidad_spin)
        
        btn_detalle_layout = QHBoxLayout()
        btn_detalle_layout.addWidget(self.btn_agregar_detalle)
        btn_detalle_layout.addWidget(self.btn_eliminar_detalle)
        form_detalle.addRow(btn_detalle_layout)
        
        layout.addLayout(form_detalle)
        
        # Totales y cálculos fiscales
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
        self.btn_guardar = QPushButton("Guardar Cambios")
        self.btn_guardar.clicked.connect(self.guardar_cambios)
        self.btn_limpiar = QPushButton("Restablecer")
        self.btn_limpiar.clicked.connect(self.cargar_datos_factura)
        self.btn_volver = QPushButton("Volver")
        self.btn_volver.clicked.connect(self.close)
        
        btn_layout.addWidget(self.btn_guardar)
        btn_layout.addWidget(self.btn_limpiar)
        btn_layout.addWidget(self.btn_volver)
        layout.addLayout(btn_layout)
        
        # Conectar señales
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
            QMessageBox.critical(self, "Error", f"Error al cargar clientes:\n{str(err)}")
    
    def cargar_tipos(self):
        """Carga el selector de tipo (Producto/Servicio)"""
        self.tipo_combo.clear()
        self.tipo_combo.addItems(["Producto", "Servicio"])
    
    def cambiar_tipo(self):
        """Cambia entre cargar productos o servicios según la selección"""
        tipo = self.tipo_combo.currentText()
        if tipo == "Producto":
            self.cargar_productos()
        else:
            self.cargar_servicios()
    
    def cargar_servicios(self):
        """Carga los servicios profesionales desde la base de datos"""
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
                    userData=(servicio['id_servicio'], float(servicio['precio']))
                )
            
            if servicios:
                self.actualizar_precio()
        except pymysql.Error as err:
            QMessageBox.critical(self, "Error", f"Error al cargar servicios:\n{str(err)}")
    
    def cargar_productos(self):
        """Carga los productos desde la base de datos"""
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
                    userData=(producto['id_producto'], float(producto['precio']))
                )
            
            if productos:
                self.actualizar_precio()
        except pymysql.Error as err:
            QMessageBox.critical(self, "Error", f"Error al cargar productos:\n{str(err)}")
    
    def cargar_datos_factura(self):
        try:
            # Limpiar tabla antes de cargar nuevos datos
            self.detalles_table.setRowCount(0)
            
            # Verificar primero si la factura existe
            self.cursor.execute("SELECT COUNT(*) as count FROM factura WHERE id_factura = %s", (self.id_factura,))
            result = self.cursor.fetchone()
            
            if not result or result['count'] == 0:
                QMessageBox.critical(self, "Error", f"No se encontró la factura con ID {self.id_factura}")
                self.close()
                return
            
            # Obtener datos de la cabecera de la factura
            self.cursor.execute("""
                SELECT id_cliente, fecha_factura, estado_factura, monto 
                FROM factura 
                WHERE id_factura = %s
            """, (self.id_factura,))
            factura = self.cursor.fetchone()
            
            if not factura:
                QMessageBox.critical(self, "Error", "No se pudieron obtener los datos de la factura")
                self.close()
                return
            
            # Establecer valores en los controles
            cliente_encontrado = False
            for i in range(self.cliente_combo.count()):
                if self.cliente_combo.itemData(i) == factura['id_cliente']:
                    self.cliente_combo.setCurrentIndex(i)
                    cliente_encontrado = True
                    break
            
            if not cliente_encontrado:
                QMessageBox.warning(self, "Advertencia", "El cliente asociado a esta factura no existe")
            
            self.fecha_input.setDate(QDate.fromString(str(factura['fecha_factura']), "yyyy-MM-dd"))
            
            index = self.estado_combo.findText(factura['estado_factura'])
            if index >= 0:
                self.estado_combo.setCurrentIndex(index)
            
            # Cargar detalles de productos de la factura
            self.cursor.execute("""
                SELECT df.id_producto, p.nombre_producto, df.cantidad, 
                       (df.subtotal/df.cantidad) as precio_unitario, df.subtotal
                FROM detalle_factura df
                JOIN productos p ON df.id_producto = p.id_producto
                WHERE df.id_factura = %s
            """, (self.id_factura,))
            detalles_productos = self.cursor.fetchall()
            
            for detalle in detalles_productos:
                row = self.detalles_table.rowCount()
                self.detalles_table.insertRow(row)
                
                self.detalles_table.setItem(row, 0, QTableWidgetItem("Producto"))
                self.detalles_table.setItem(row, 1, QTableWidgetItem(str(detalle['id_producto'])))
                self.detalles_table.setItem(row, 2, QTableWidgetItem(detalle['nombre_producto']))
                self.detalles_table.setItem(row, 3, QTableWidgetItem(f"{float(detalle['precio_unitario']):.2f}"))
                self.detalles_table.setItem(row, 4, QTableWidgetItem(str(detalle['cantidad'])))
                self.detalles_table.setItem(row, 5, QTableWidgetItem(f"{float(detalle['subtotal']):.2f}"))
            
            # Cargar detalles de servicios de la factura (si existe la tabla)
            try:
                self.cursor.execute("""
                    SELECT ds.id_servicio, sp.nombre_servicio, ds.cantidad, 
                           (ds.subtotal/ds.cantidad) as precio_unitario, ds.subtotal
                    FROM detalle_servicio ds
                    JOIN servicios_profesionales sp ON ds.id_servicio = sp.id_servicio
                    WHERE ds.id_factura = %s
                """, (self.id_factura,))
                detalles_servicios = self.cursor.fetchall()
                
                for detalle in detalles_servicios:
                    row = self.detalles_table.rowCount()
                    self.detalles_table.insertRow(row)
                    
                    self.detalles_table.setItem(row, 0, QTableWidgetItem("Servicio"))
                    self.detalles_table.setItem(row, 1, QTableWidgetItem(str(detalle['id_servicio'])))
                    self.detalles_table.setItem(row, 2, QTableWidgetItem(detalle['nombre_servicio']))
                    self.detalles_table.setItem(row, 3, QTableWidgetItem(f"{float(detalle['precio_unitario']):.2f}"))
                    self.detalles_table.setItem(row, 4, QTableWidgetItem(str(detalle['cantidad'])))
                    self.detalles_table.setItem(row, 5, QTableWidgetItem(f"{float(detalle['subtotal']):.2f}"))
            except pymysql.Error:
                # La tabla detalle_servicio no existe aún, se creará al guardar
                pass
            
            self.actualizar_total()
            
            # Cargar deducción fiscal si existe
            self.cursor.execute("""
                SELECT monto_deduccion 
                FROM deduccion_fiscal 
                WHERE id_factura = %s
            """, (self.id_factura,))
            deduccion = self.cursor.fetchone()
            
            if deduccion:
                self.deduccion_label.setText(f"Deducción Fiscal: ${float(deduccion['monto_deduccion']):.2f}")
            
        except pymysql.Error as err:
            QMessageBox.critical(self, "Error", f"Error al cargar factura:\n{str(err)}")
            self.close()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error inesperado:\n{str(e)}")
            self.close()
    
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
            QMessageBox.critical(self, "Error", f"Error al agregar detalle:\n{str(e)}")
    
    def eliminar_detalle(self):
        selected = self.detalles_table.selectedItems()
        if not selected:
            QMessageBox.warning(self, "Advertencia", "Seleccione un item para eliminar")
            return
            
        row = selected[0].row()
        self.detalles_table.removeRow(row)
        self.actualizar_total()
    
    def actualizar_total(self):
        total = 0.0
        for row in range(self.detalles_table.rowCount()):
            subtotal_text = self.detalles_table.item(row, 5).text()
            total += float(subtotal_text)
            
        self.total_label.setText(f"Total: ${total:.2f}")
        
        # Calcular IVA (13%)
        iva = total * 0.13
        self.iva_label.setText(f"IVA (13%): ${iva:.2f}")
        
        # Calcular Deducción Fiscal (Total + IVA)
        deduccion_fiscal = total + iva
        self.deduccion_label.setText(f"Deducción Fiscal: ${deduccion_fiscal:.2f}")
    
    def guardar_cambios(self):
        try:
            # Validar datos antes de guardar
            if not self.validar_datos():
                return
                
            with self.conn.cursor() as cursor:
                # Obtener los valores actualizados de los campos de edición
                id_cliente = self.cliente_combo.currentData()
                fecha_factura = self.fecha_input.date().toString("yyyy-MM-dd")
                estado_factura = self.estado_combo.currentText()
                
                # Calcular el monto total de los detalles
                total = 0.0
                for row in range(self.detalles_table.rowCount()):
                    subtotal_text = self.detalles_table.item(row, 5).text()
                    total += float(subtotal_text)
                
                # Actualizar la factura en la base de datos
                cursor.execute("""
                    UPDATE factura 
                    SET id_cliente = %s, 
                        fecha_factura = %s,
                        estado_factura = %s,
                        monto = %s
                    WHERE id_factura = %s
                """, (id_cliente, fecha_factura, estado_factura, total, self.id_factura))
                
                # Eliminar los detalles antiguos
                cursor.execute("DELETE FROM detalle_factura WHERE id_factura = %s", (self.id_factura,))
                
                # Crear tabla detalle_servicio si no existe
                cursor.execute("""
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
                
                # Eliminar los servicios antiguos
                cursor.execute("DELETE FROM detalle_servicio WHERE id_factura = %s", (self.id_factura,))
                
                # Insertar los nuevos detalles
                for row in range(self.detalles_table.rowCount()):
                    tipo = self.detalles_table.item(row, 0).text()
                    id_item = int(self.detalles_table.item(row, 1).text())
                    cantidad = int(self.detalles_table.item(row, 4).text())
                    subtotal = float(self.detalles_table.item(row, 5).text())
                    
                    if tipo == "Producto":
                        cursor.execute("""
                            INSERT INTO detalle_factura 
                            (id_factura, id_producto, cantidad, subtotal)
                            VALUES (%s, %s, %s, %s)
                        """, (self.id_factura, id_item, cantidad, subtotal))
                    else:
                        cursor.execute("""
                            INSERT INTO detalle_servicio 
                            (id_factura, id_servicio, cantidad, subtotal)
                            VALUES (%s, %s, %s, %s)
                        """, (self.id_factura, id_item, cantidad, subtotal))
                
                # Actualizar deducción fiscal
                deduccion_fiscal = total * 1.13  # Total + IVA
                cursor.execute("""
                    INSERT INTO deduccion_fiscal 
                    (id_factura, id_cliente, monto_deduccion)
                    VALUES (%s, %s, %s)
                    ON DUPLICATE KEY UPDATE 
                        id_cliente = VALUES(id_cliente),
                        monto_deduccion = VALUES(monto_deduccion)
                """, (self.id_factura, id_cliente, deduccion_fiscal))
                
                self.conn.commit()
                
                QMessageBox.information(self, "Éxito", "Factura actualizada correctamente")
                self.close()
                
        except pymysql.Error as err:
            QMessageBox.critical(self, "Error", f"Error de base de datos:\n{str(err)}")
            self.conn.rollback()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error inesperado:\n{str(e)}")
            self.conn.rollback()
        
    def validar_datos(self):
        if self.cliente_combo.currentIndex() < 0:
            QMessageBox.warning(self, "Validación", "Seleccione un cliente")
            return False
            
        if self.detalles_table.rowCount() == 0:
            QMessageBox.warning(self, "Validación", "La factura debe tener al menos un item")
            return False
            
        return True