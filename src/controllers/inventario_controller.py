from src.models.producto import Producto
from src.views.inventario_view import InventarioView
from src.service.inventario_service import InventarioService
from src.utils.utils import Utils


class InventarioController:
    def __init__(self, inventario_view: InventarioView, inventario_service: InventarioService):
        self.inventario_view = inventario_view
        self.inventario_service = inventario_service

    def menu_inventario(self):
        opcion = -1
        while opcion != 0:
            opcion = self.inventario_view.mostrar_menu()
            match opcion:
                case 1:
                    self.anadir_articulo()
                case 2:
                    self.modificar_articulo()
                case 3:
                    self.eliminar_articulo()
                case 4:
                    self.mostrar_inventario()
                case 0:
                    self.inventario_view.mostrar_mensaje("Volviendo al menú principal...")
                case _:
                    self.inventario_view.mostrar_mensaje("Opción no válida, por favor intente de nuevo.")

    def anadir_articulo(self):
        datos = self.inventario_view.solicitar_datos_producto()
        producto = Producto(
            id=0, # El ID se genera en la base de datos
            nombre=datos["nombre"],
            descripcion=datos["descripcion"],
            precio=datos["precio"],
            stock=datos["stock"],
            categoria=datos["categoria"]
        )
        if self.inventario_service.agregar_producto(producto):
            self.inventario_view.mostrar_mensaje("Producto añadido correctamente.")
        else:
            self.inventario_view.mostrar_mensaje("Error al añadir el producto.")

    def modificar_articulo(self):
        id_producto = self.inventario_view.solicitar_id_producto()
        producto_existente = self.inventario_service.obtener_producto(id_producto)
        
        if not producto_existente:
            self.inventario_view.mostrar_mensaje("Producto no encontrado.")
        else:
            self.inventario_view.mostrar_mensaje("Datos actuales del producto:")
            self.inventario_view.mostrar_producto(producto_existente)
            
            if Utils.confirmar_accion("¿Desea modificar este producto?"):
                datos = self.inventario_view.solicitar_datos_producto()
                # Mantenemos el ID original
                producto_modificado = Producto(
                    id=id_producto,
                    nombre=datos["nombre"],
                    descripcion=datos["descripcion"],
                    precio=datos["precio"],
                    stock=datos["stock"],
                    categoria=datos["categoria"]
                )
                
                if self.inventario_service.modificar_producto(producto_modificado):
                    self.inventario_view.mostrar_mensaje("Producto modificado correctamente.")
                else:
                    self.inventario_view.mostrar_mensaje("Error al modificar el producto.")

    def eliminar_articulo(self):
        id_producto = self.inventario_view.solicitar_id_producto()
        producto_existente = self.inventario_service.obtener_producto(id_producto)

        if not producto_existente:
            self.inventario_view.mostrar_mensaje("Producto no encontrado.")
        else:
            self.inventario_view.mostrar_producto(producto_existente)
            if Utils.confirmar_accion("¿Está seguro de que desea eliminar este producto?"):
                if self.inventario_service.eliminar_producto(id_producto):
                    self.inventario_view.mostrar_mensaje("Producto eliminado correctamente.")
                else:
                    self.inventario_view.mostrar_mensaje("Error al eliminar el producto.")

    def mostrar_inventario(self):
        productos = self.inventario_service.listar_productos()
        self.inventario_view.mostrar_lista_productos(productos)
