from src.views.menu_view import MenuView
from src.database.db_manager import DBManager
from src.views.inventario_view import InventarioView
from src.controllers.inventario_controller import InventarioController
from src.repository.inventario_repository import InventarioRepository
from src.service.inventario_service import InventarioService
from src.views.cliente_view import ClienteView
from src.controllers.cliente_controller import ClienteController
from src.repository.cliente_repository import ClienteRepository
from src.service.cliente_service import ClienteService
from src.views.venta_view import VentaView
from src.controllers.venta_controller import VentaController
from src.repository.venta_repository import VentaRepository
from src.service.venta_service import VentaService
from src.controllers.export_controller import ExportController
from src.views.export_view import ExportView


class MenuController:

    def __init__(self, menu_view: MenuView, db_manager: DBManager):
        self.menu_view = menu_view
        self.db_manager = db_manager

    def iniciar(self):
        resultado = self.db_manager.initialize_database()
        print(resultado)

        # Inventario
        inventario_repository = InventarioRepository(self.db_manager)
        inventario_service = InventarioService(inventario_repository)
        inventario_controller = InventarioController(InventarioView(), inventario_service)

        # Clientes
        cliente_repository = ClienteRepository(self.db_manager)
        cliente_service = ClienteService(cliente_repository)
        cliente_controller = ClienteController(ClienteView(), cliente_service)

        # Ventas
        venta_repository = VentaRepository(self.db_manager)
        venta_service = VentaService(venta_repository, inventario_repository)
        venta_controller = VentaController(VentaView(), venta_service)


        opcion = None
        while opcion != 0:
            opcion = self.menu_view.show_main_menu()

            match opcion:
                case 1:
                    inventario_controller.menu_inventario()
                case 2:
                    venta_controller.menu_ventas()
                case 3:
                    cliente_controller.menu_clientes()
                case 4:
                    export_controller = ExportController(ExportView(), self.db_manager)
                    export_controller.menu()
                case 0:
                    print("Saliendo del sistema...")
                case _:
                    print("Opcion no valida")


    
