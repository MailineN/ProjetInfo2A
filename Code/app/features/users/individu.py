from app.menus.menu_interface import Ferme
from app.menus.menu_interface import Menu_Interface

class Individu:     
    def __init__(self):
        self.type = "individu"
        self.previous_menu_ini = {}
    # Permet à tout individu de quitter 
    def quitter(self,previous_menu): 
        """ Fonction permettant de quitter l'application
        Arguments:
            previous_menu {list} -- menu précédent l'appel de la fonction
        Returns:
            Ouvert(previous_menu) -- Renvoie le menu précédent
            Ferme() -- Quitte l'application
        """        
        print("{:^63}\n".format("\nVoulez vous quitter cette application ? (Y/N)"))
        check = input("Choix : ")
        if check in ["Y","y"] : 
            return Ferme()
        else : 
            return Menu_Interface(previous_menu)