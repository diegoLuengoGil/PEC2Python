from src.utils.utils import Utils


class MenuView:

    def show_main_menu(self) -> int:
        """Muestra las opciones del menu."""
        print("\n--- GESTION DE INVENTARIO ---")
        print("1. Gestion de inventario")
        print("2. Gestion de ventas")
        print("3. Gestion de clientes")
        print("4. Exportar/Importar datos (JSON)")
        print("0. Exit")

        opcion = Utils.get_int("Seleccione una opcion: ")
        return opcion

