from src.repository.export_repository import ExportRepository


class ExportService:
    def __init__(self, export_repository: ExportRepository):
        self.export_repository = export_repository

    def export(self, path: str) -> bool:
        return self.export_repository.export_all(path)

    def import_(self, path: str, overwrite: bool = False) -> bool:
        return self.export_repository.import_all(path, overwrite=overwrite)
