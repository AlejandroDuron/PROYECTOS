# controlador_cliente.py
import sys
from PyQt6.QtWidgets import QApplication, QMessageBox
from modelo.modelo_cliente import ModeloCliente
from vista.vista_pantalla_principal import PantallaPrincipal
from vista.vista_cliente import VistaCliente

class ControladorCliente:
    def __init__(self):
        # No crear nueva QApplication aquí
        self.modelo = ModeloCliente()
        self.vista_principal = PantallaPrincipal(self.modelo)
        self.vista_registro = VistaCliente()

        # Configurar conexiones
        self.configurar_eventos()
        
        # Estado inicial
        self.vista_registro.hide()
        self.vista_principal.show()

        # Configuración inicial de la interfaz
        self.configurar_eventos()
        self.vista_registro.hide()
        self.vista_principal.show()

    # Configuración de eventos y señales
    def configurar_eventos(self):
        self.vista_principal.boton_agregar.clicked.connect(self.mostrar_registro)
        self.vista_principal.boton_editar.clicked.connect(self.mostrar_edicion)
        self.vista_principal.boton_eliminar.clicked.connect(self.eliminar_cliente)
        self.vista_registro.boton_guardar.clicked.connect(self.registrar_cliente)

    # Métodos para manejo del formulario de registro
    def mostrar_registro(self):
        self.vista_registro.limpiar_campos()
        self.vista_registro.show()

    def registrar_cliente(self):
        datos = self.vista_registro.obtener_datos()
        
        # Validación de campos obligatorios
        if not all(datos.values()):
            self.vista_registro.mostrar_mensaje("Error", "Complete todos los campos", "error")
            return
            
        # Registro en base de datos
        if self.modelo.insertar_cliente(**datos):
            self.vista_registro.mostrar_mensaje("Éxito", "Cliente registrado")
            self.vista_registro.hide()
            self.vista_principal.actualizar_lista()
        else:
            self.vista_registro.mostrar_mensaje("Error", "Error al registrar", "error")

    # Métodos para edición de clientes
    def mostrar_edicion(self):
        cliente = self.obtener_cliente_seleccionado()
        if not cliente:
            return
            
        self.preparar_formulario_edicion(cliente)
        self.vista_registro.show()

    def preparar_formulario_edicion(self, cliente):
        self.vista_registro.limpiar_campos()
        self.cargar_datos_cliente(cliente)
        self.reconectar_boton_guardar()

    def cargar_datos_cliente(self, cliente):
        self.vista_registro.inputs['Nombre'].setText(cliente['nombre'])
        self.vista_registro.inputs['Dirección'].setText(cliente['direccion'])
        self.vista_registro.inputs['Teléfono'].setText(cliente['telefono'])
        self.vista_registro.inputs['Email'].setText(cliente['email'])
        self.email_original = cliente['email']

    def reconectar_boton_guardar(self):
        try:
            self.vista_registro.boton_guardar.clicked.disconnect()
        except TypeError:
            pass
        self.vista_registro.boton_guardar.clicked.connect(self.actualizar_cliente)

    def actualizar_cliente(self):
        datos = self.vista_registro.obtener_datos()
        
        if self.modelo.actualizar_cliente(self.email_original, datos):
            self.vista_registro.mostrar_mensaje("Éxito", "Cliente actualizado")
            self.vista_registro.hide()
            self.vista_principal.actualizar_lista()
        else:
            self.vista_registro.mostrar_mensaje("Error", "Error al actualizar", "error")

    # Métodos para eliminación de clientes
    def eliminar_cliente(self):
        cliente = self.obtener_cliente_seleccionado()
        if not cliente:
            return
            
        if self.confirmar_eliminacion(cliente):
            self.ejecutar_eliminacion(cliente)

    def confirmar_eliminacion(self, cliente):
        confirmacion = QMessageBox.question(
            self.vista_principal, 
            "Confirmar",
            f"¿Eliminar a {cliente['nombre']}?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        return confirmacion == QMessageBox.StandardButton.Yes

    def ejecutar_eliminacion(self, cliente):
        if self.modelo.eliminar_cliente(cliente['email']):
            self.vista_principal.actualizar_lista()
            QMessageBox.information(self.vista_principal, "Éxito", "Cliente eliminado")
        else:
            QMessageBox.critical(self.vista_principal, "Error", "No se pudo eliminar")

    # Métodos auxiliares
    def obtener_cliente_seleccionado(self):
        if not hasattr(self.vista_principal, 'cliente_seleccionado'):
            QMessageBox.warning(self.vista_principal, "Advertencia", "Seleccione un cliente")
            return None
        return self.vista_principal.cliente_seleccionado