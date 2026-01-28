from src.utils.utils import Utils


class DataView:
    def show_menu(self) -> int:
        print("\n--- EXPORTAR / IMPORTAR (JSON) ---")
        print("1. Exportar datos a JSON")
        print("2. Importar datos desde JSON")
        print("0. Volver")
        return Utils.get_int("Seleccione una opcion: ")

    def ask_file_path(self, default: str = 'data.json') -> str:
        path = input(f"Ruta del archivo (default: {default}): ").strip()
        return path if path else default

    def confirm_overwrite(self) -> bool:
        return Utils.confirmar_accion("Desea sobrescribir los datos actuales?")

    def show_message(self, msg: str) -> None:
        print(msg)
