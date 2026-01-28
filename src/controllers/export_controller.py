from src.views.export_view import ExportView
from src.service.export_service import ExportService
from src.repository.export_repository import ExportRepository
from src.database.db_manager import DBManager


class ExportController:
    def __init__(self, view: ExportView, db_manager: DBManager):
        self.view = view
        self.repo = ExportRepository(db_manager)
        self.service = ExportService(self.repo)

    def menu(self):
        opcion = None
        while opcion != 0:
            opcion = self.view.show_menu()
            if opcion == 1:
                path = self.view.ask_file_path('export_data.json')
                ok = self.service.export(path)
                self.view.show_message('Exportacion completada.' if ok else 'Fallo en la exportacion.')
            elif opcion == 2:
                path = self.view.ask_file_path('import_data.json')
                overwrite = self.view.confirm_overwrite()
                ok = self.service.import_(path, overwrite=overwrite)
                self.view.show_message('Importacion completada.' if ok else 'Fallo en la importacion.')
            elif opcion == 0:
                break
            else:
                self.view.show_message('Opcion no valida')
