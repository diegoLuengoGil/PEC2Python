from src.database.db_manager import DBManager
from src.models.producto import Producto
from src.views.inventario_view import InventarioView


class InventarioController:
    def __init__(self, db_manager: DBManager, inventario_view: InventarioView):
        self.db_manager = db_manager
        self.inventario_view = inventario_view

    def menu_inventario(self):
        opcion = self.inventario_view.mostrar_menu()
        while opcion != 0:
            match opcion:
                case 1:
                    self.anadir_articulo()
                case 2:
                    self.modificar_articulo()
                case 3:
                    self.eliminar_articulo()
                case 4:
                    self.mostrar_inventario()
                case _:
                    print("Opcion no valida") #p

    def anadir_articulo(self):
        pass

    def modificar_articulo(self):
        pass

    def eliminar_articulo(self):
        pass

    def mostrar_inventario(self):
        pass    

    def obtener_articulo(self) -> Producto:
        pass
