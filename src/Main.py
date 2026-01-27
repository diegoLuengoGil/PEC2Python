import sys
import os

# Add the project root directory to the python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from src.controllers.menu_controller import MenuController
from src.views.menu_view import MenuView
from src.database.db_manager import DBManager


def main():

    menu = MenuController(MenuView(), DBManager())

    menu.iniciar()


if __name__ == "__main__":
    main()
