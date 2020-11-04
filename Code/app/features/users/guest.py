from app.menus.menu_interface import Ferme
from app.menus.menu_interface import MenuInterface
from .individu import Individu
from app.security.verif_id import verif_id
from app.security.verif_mdp import verif_mdp
import hashlib

class Guest(Individu) :
    
    """ classe invité, pouvant jouer au jeu sans se connecter """
    
    def __init__(self):
        self.identifiant = "id" # Désolée d'y avoir touché, mais l'id d'un guest est genéré quand il souhaite jouer et non au lancement
        self.userType = "Guest" #Et on définit que pour l'instant c'est un guest, on modifie l'attribut quand il se connecte 
    
    @staticmethod 
    def play() :   
        pass
    
    def createAccount():
        identifiant = verif_id(input("Entrez votre identifiant")) #entrer l'id + vérifier qu'il n'existe pas déjà
        motdepasse = input("Choisissez votre mot de passe")
        verifMotdepasse= input("Réécrivez votre mot de passe")
        motdepasse = verif_mdp(motdepasse, verifMotdepasse) #vérifie que les deux mdp sont les mêmes et renvoie le mdp

        #code pour hasher le mdp 
        m = hashlib.md5()
        m.update(motdepasse)
        hash_mdp = m.digest()

        
    
    def connexion():
        pass
    
    def initEmptyGame() :
        pass
    
    def joinGame():
        pass
    
    def displayFinishedGame():
        pass
    
