from src.models.cliente import Cliente
from src.views.cliente_view import ClienteView
from src.service.cliente_service import ClienteService
from src.utils.utils import Utils

class ClienteController:
    def __init__(self, cliente_view: ClienteView, cliente_service: ClienteService):
        self.cliente_view = cliente_view
        self.cliente_service = cliente_service

    def menu_clientes(self):
        opcion = -1
        while opcion != 0:
            opcion = self.cliente_view.mostrar_menu()
            match opcion:
                case 1:
                    self.anadir_cliente()
                case 2:
                    self.modificar_cliente()
                case 3:
                    self.eliminar_cliente()
                case 4:
                    self.mostrar_clientes()
                case 0:
                    self.cliente_view.mostrar_mensaje("Volviendo al menú principal...")
                case _:
                    self.cliente_view.mostrar_mensaje("Opción no válida.")

    def anadir_cliente(self):
        datos = self.cliente_view.solicitar_datos_cliente()
        cliente = Cliente(
            id=0,
            nombre=datos["nombre"],
            email=datos["email"],
            saldo=datos["saldo"]
        )
        if self.cliente_service.agregar_cliente(cliente):
            self.cliente_view.mostrar_mensaje("Cliente añadido correctamente.")
        else:
            self.cliente_view.mostrar_mensaje("Error al añadir al cliente.")

    def modificar_cliente(self):
        id_cliente = self.cliente_view.solicitar_id_cliente()
        cliente_existente = self.cliente_service.obtener_cliente(id_cliente)
        
        if not cliente_existente:
            self.cliente_view.mostrar_mensaje("Cliente no encontrado.")
        else:
            self.cliente_view.mostrar_mensaje("Datos actuales del cliente:")
            self.cliente_view.mostrar_cliente(cliente_existente)
            
            if Utils.confirmar_accion("¿Desea modificar este cliente?"):
                datos = self.cliente_view.solicitar_datos_cliente()
                # Mantener ID
                cliente_modificado = Cliente(
                    id=id_cliente,
                    nombre=datos["nombre"],
                    email=datos["email"],
                    saldo=datos["saldo"]
                )
                
                if self.cliente_service.modificar_cliente(cliente_modificado):
                    self.cliente_view.mostrar_mensaje("Cliente modificado correctamente.")
                else:
                    self.cliente_view.mostrar_mensaje("Error al modificar el cliente.")

    def eliminar_cliente(self):
        id_cliente = self.cliente_view.solicitar_id_cliente()
        cliente_existente = self.cliente_service.obtener_cliente(id_cliente)

        if not cliente_existente:
            self.cliente_view.mostrar_mensaje("Cliente no encontrado.")
        else:
            self.cliente_view.mostrar_cliente(cliente_existente)
            if Utils.confirmar_accion("¿Está seguro de que desea eliminar este cliente?"):
                if self.cliente_service.eliminar_cliente(id_cliente):
                    self.cliente_view.mostrar_mensaje("Cliente eliminado correctamente.")
                else:
                    self.cliente_view.mostrar_mensaje("Error al eliminar el cliente.")

    def mostrar_clientes(self):
        clientes = self.cliente_service.listar_clientes()
        self.cliente_view.mostrar_lista_clientes(clientes)
