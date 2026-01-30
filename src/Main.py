

from controllers.menu_controller import MenuController
from views.menu_view import MenuView
from database.db_manager import DBManager


def main():

    menu = MenuController(MenuView(), DBManager())

    menu.iniciar()


if __name__ == "__main__":
    main()
