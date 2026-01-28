from src.repository.data_repository import DataRepository


class DataService:
    """Servicio para exportar e importar datos."""
    def __init__(self, data_repository: DataRepository):
        self.data_repository = data_repository

    def export_data(self, path: str) -> bool:
        """Exporta todos los datos a un archivo JSON."""
        return self.data_repository.export_all(path)

    def import_data(self, path: str, overwrite: bool = False) -> bool:
        """Importa todos los datos desde un archivo JSON."""
        return self.data_repository.import_all(path, overwrite)
