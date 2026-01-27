from src.views.venta_view import VentaView
from src.service.venta_service import VentaService

class VentaController:
    def __init__(self, venta_view: VentaView, venta_service: VentaService):
        self.venta_view = venta_view
        self.venta_service = venta_service

    def menu_ventas(self):
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
        items = self.venta_view.solicitar_items_venta()
        if items:
            print("Procesando venta...")
            self.venta_service.crear_venta(items)

    def mostrar_historial(self):
        ventas = self.venta_service.listar_ventas()
        self.venta_view.mostrar_lista_ventas(ventas)

    def mostrar_detalle(self):
        id_venta = self.venta_view.solicitar_id_venta()
        venta = self.venta_service.obtener_venta(id_venta)
        if venta:
            self.venta_view.mostrar_detalle_venta(venta)
        else:
            self.venta_view.mostrar_mensaje("Venta no encontrada.")
