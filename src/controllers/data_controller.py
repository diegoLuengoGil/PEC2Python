from views.data_view import DataView
from service.data_service import DataService
from repository.data_repository import DataRepository
from database.db_manager import DBManager


class DataController:
    """Controlador para gestionar operaciones relacionadas con datos."""
    def __init__(self, data_view: DataView, db_manager: DBManager):
        self.data_view = data_view
        self.data_repo = DataRepository(db_manager)
        self.data_service = DataService(self.data_repo)

    def menu(self):
        """Muestra el menú de exportación/importación y maneja las opciones."""
        opcion = None
        while opcion != 0:
            opcion = self.data_view.show_menu()
            if opcion == 1:
                path = 'export_data.json'
                ok = self.data_service.export_data(path)
                self.data_view.show_message('Exportacion completada.' if ok else 'Fallo en la exportacion.')
            elif opcion == 2:
                path = 'export_data.json'
                overwrite = self.data_view.confirm_overwrite()
                ok = self.data_service.import_data(path, overwrite=overwrite)
                self.data_view.show_message('Importacion completada.' if ok else 'Fallo en la importacion.')
            elif opcion == 0:
                break
            else:
                self.data_view.show_message('Opcion no valida')
