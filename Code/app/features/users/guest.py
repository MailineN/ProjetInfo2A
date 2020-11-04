from app.menus.menu_interface import Ferme
from app.menus.menu_interface import MenuInterface
from .individu import Individu
from app.security.id import verif_init_id
from app.security.mdp import verif_init_mdp
from app.DAO.guestDao import GuestDAO
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
        username = verif_id(input("Entrez votre nom d'utilisateur")) #entrer le nom d'utilisateur + vérifier qu'il n'existe pas déjà
        motdepasse = input("Choisissez votre mot de passe")
        verifMotdepasse= input("Réécrivez votre mot de passe")
        motdepasse = verif_init_mdp(motdepasse, verifMotdepasse) #vérifie que les deux mdp sont les mêmes et renvoie le mdp

        #code pour hasher le mdp 
        m = hashlib.md5()
        m.update(motdepasse)
        hash_mdp = m.digest()

        #ajouter le compte à la base
        GuestDAO.addAccounttoData(username,hash_mdp)
        return("Votre compte a bien été créé")
    
    def connexion():
        """Permet à un utilisateur de se connecter """
        username = input("Entrez votre username")
        motdepasse = input("Entrez votre mot de passe")

        #code pour hasher le mdp
        m = hashlib.md5()
        m.update(motdepasse)
        hash_mdp = m.digest()

        #on demande à GuestDAO  de créer l'instance de l'objet
        GuestDAO.checkAccounttoData(username, hash_mdp)


    def initEmptyGame() :
        pass
    
    def joinGame():
        pass
    
    def displayFinishedGame():
        pass
    
