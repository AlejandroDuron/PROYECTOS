from datetime import datetime
from modelo.BD.bd_admin_user_seguimientomantenimiento import ModeloBD
from vista.Vista_admin_user_seguimientomantenimiento import VistaMantenimientos
from vista.DialogoEditarMantenimiento import DialogoEditarMantenimiento
from PyQt6.QtWidgets import QMessageBox

class ControladorMantenimientos:
    def __init__(self, username=None, rol=None):
        self.username = username
        self.rol = rol
        self.modelo = ModeloBD()
        self.vista_principal = None
        self.iniciar()
    
    def iniciar(self):
        try:
            mantenimientos = self.modelo.obtener_mantenimientos()
            
            if not mantenimientos:
                QMessageBox.information(
                    None, 
                    "Información", 
                    "No hay registros de mantenimientos disponibles"
                )
                return
            
            self.vista_principal = VistaMantenimientos(
                mantenimientos=mantenimientos,
                controlador=self
            )
            self.vista_principal.show()
            
        except Exception as e:
            QMessageBox.critical(
                None, 
                "Error", 
                f"No se pudo cargar la información de mantenimientos:\n{str(e)}"
            )
    
    def editar_mantenimiento(self, id_mantenimiento):
        try:
            # Obtener los datos actuales del mantenimiento
            mantenimiento = self.modelo.obtener_mantenimiento_por_id(id_mantenimiento)
            
            if not mantenimiento:
                QMessageBox.warning(self.vista_principal, "Error", "No se encontró el mantenimiento")
                return
            
            # Crear y mostrar diálogo de edición
            dialog = DialogoEditarMantenimiento(
                self.vista_principal,
                id_mantenimiento,
                mantenimiento['id_cliente'],
                mantenimiento['fecha_programada'],
                mantenimiento['encargado'],
                mantenimiento['completado']
            )
            
            if dialog.exec():
                # Obtener los nuevos valores del diálogo
                nuevos_valores = dialog.obtener_valores()
                
                # Actualizar en la base de datos
                if self.modelo.actualizar_mantenimiento(
                    id_mantenimiento,
                    nuevos_valores['fecha_programada'],
                    nuevos_valores['encargado'],
                    nuevos_valores['completado']
                ):
                    QMessageBox.information(
                        self.vista_principal,
                        "Éxito",
                        "Mantenimiento actualizado correctamente"
                    )
                    self.actualizar_vista()
                else:
                    QMessageBox.warning(
                        self.vista_principal,
                        "Error",
                        "No se pudo actualizar el mantenimiento"
                    )
                    
        except Exception as e:
            QMessageBox.critical(
                self.vista_principal,
                "Error",
                f"No se pudo editar el mantenimiento:\n{str(e)}"
            )
    def eliminar_mantenimiento(self, id_mantenimiento):
        try:
            confirm = QMessageBox.question(
                self.vista_principal,
                "Confirmar Eliminación",
                "¿Está seguro que desea eliminar este registro de mantenimiento?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )
            
            if confirm == QMessageBox.StandardButton.Yes:
                # Implement delete functionality here
                success = self.modelo.eliminar_mantenimiento(id_mantenimiento)
                
                if success:
                    QMessageBox.information(
                        self.vista_principal,
                        "Éxito",
                        "Mantenimiento eliminado correctamente"
                    )
                    # Refresh the view
                    self.iniciar()
                else:
                    QMessageBox.warning(
                        self.vista_principal,
                        "Advertencia",
                        "No se pudo eliminar el mantenimiento"
                    )
        except Exception as e:
            QMessageBox.critical(
                self.vista_principal,
                "Error",
                f"No se pudo eliminar el mantenimiento:\n{str(e)}"
            )
    
    def actualizar_vista(self):
        """Refresh the view with updated data"""
        self.iniciar()
