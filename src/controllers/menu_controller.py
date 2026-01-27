from src.views.menu_view import MenuView
from src.database.db_manager import DBManager
from src.views.inventario_view import InventarioView
from src.controllers.inventario_controller import InventarioController


class MenuController:

    def __init__(self, menu_view: MenuView, db_manager: DBManager):
        self.menu_view = menu_view
        self.db_manager = db_manager

    def iniciar(self):
        self.db_manager.initialize_database()

        inventario_controller = InventarioController(self.db_manager, InventarioView())


        while opcion != 0:
            opcion = self.menu_view.show_main_menu()

            match opcion:
                case 1:
                    self.menu_view.show_inventario()
                case 2:
                    self.menu_view.show_clientes()
                case 3:
                    self.menu_view.show_ventas()
                case 4:
                    self.menu_view.show_ventas()
                case _:
                    print("Opcion no valida")

    
