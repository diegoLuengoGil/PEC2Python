from views.venta_view import VentaView
from service.venta_service import VentaService
from views.cliente_view import ClienteView
from service.cliente_service import ClienteService
from views.inventario_view import InventarioView
from service.inventario_service import InventarioService

class VentaController:
    """Controlador para gestionar operaciones relacionadas con ventas."""
    def __init__(self, venta_view: VentaView, venta_service: VentaService, 
                 cliente_view: ClienteView, cliente_service: ClienteService,
                 inventario_view: InventarioView, inventario_service: InventarioService):
        self.venta_view = venta_view
        self.venta_service = venta_service
        self.cliente_view = cliente_view
        self.cliente_service = cliente_service
        self.inventario_view = inventario_view
        self.inventario_service = inventario_service

    def menu_ventas(self):
        """Muestra el menú de ventas y maneja las opciones."""
        opcion = -1
        while opcion != 0:
            opcion = self.venta_view.mostrar_menu()
            match opcion:
                case 1:
                    self.nueva_venta()
                case 2:
                    self.mostrar_historial()
                case 3:
                    self.mostrar_detalle()
                case 0:
                    self.venta_view.mostrar_mensaje("Volviendo al menú principal...")
                case _:
                    self.venta_view.mostrar_mensaje("Opción no válida.")

    def nueva_venta(self):
        """Crea una nueva venta."""
        self.cliente_view.mostrar_lista_clientes(self.cliente_service.listar_clientes())
        self.inventario_view.mostrar_lista_productos(self.inventario_service.listar_productos())
        cliente_id = self.venta_view.solicitar_cliente_id()
        items = self.venta_view.solicitar_items_venta()
        if items:
            print("Procesando venta...")
            self.venta_service.crear_venta(cliente_id, items)

    def mostrar_historial(self):
        """Muestra el historial de ventas."""
        ventas = self.venta_service.listar_ventas()
        self.venta_view.mostrar_lista_ventas(ventas)

    def mostrar_detalle(self):
        """Muestra el detalle de una venta."""
        id_venta = self.venta_view.solicitar_id_venta()
        venta = self.venta_service.obtener_venta(id_venta)
        if venta:
            self.venta_view.mostrar_detalle_venta(venta)
        else:
            self.venta_view.mostrar_mensaje("Venta no encontrada.")
