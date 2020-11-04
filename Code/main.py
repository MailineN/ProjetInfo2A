from app.menus import main_menu
from app.menus import menu_data


if __name__ == '__main__':
    menus = main_menu.Main_menu()
    menus.Bienvenue()
    menus.new_menu(menu_data.menu[0])
    menus.Au_revoir()
