from app.menus.menu_interface import Ferme
from app.menus.menu_interface import MenuInterface
from .individu import Individu

class Guest(Individu) :
    
    """ classe invité, pouvant jouer au jeu sans se connecter """
    
    def __init__(self):
        self.identifiant = "id" # Désolée d'y avoir touché, mais l'id d'un guest est genéré quand il souhaite jouer et non au lancement
        self.userType = "Guest" #Et on définit que pour l'instant c'est un guest, on modifie l'attribut quand il se connecte 
    
    @staticmethod 
    def play() : 
        pass
    
    def chooseGame():
        "Coucou a la personne qui va coder ça, cette fonction est inutile, on va mettre le choix du jeu dans les menus directement"
        "Idem pour la fonction quitter qui est dans Individu du coup je l'ai enlevé"
        pass
    
    def createAccount():
        pass
    
    def connexion():
        pass
    
    def initEmptyGame() :
        pass
    
    def joinGame():
        pass
    
    def displayFinishedGame():
        pass
    
