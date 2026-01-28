from src.database.db_manager import DBManager
from src.utils import json_io


class ExportRepository:
    def __init__(self, db_manager: DBManager):
        self.db_manager = db_manager

    def export_all(self, file_path: str) -> bool:
        return json_io.export_to_json(self.db_manager, file_path)

    def import_all(self, file_path: str, overwrite: bool = False) -> bool:
        return json_io.import_from_json(self.db_manager, file_path, overwrite=overwrite)
