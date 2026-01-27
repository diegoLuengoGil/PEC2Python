from src.controllers.menu_controller import MenuController
from src.views.menu_view import MenuView
from src.database.db_manager import DBManager


def main():

    menu = MenuController(MenuView(), DBManager())

    menu.iniciar()


if __name__ == "__main__":
    main()
