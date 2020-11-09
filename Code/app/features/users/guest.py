from app.menus.menu_interface import Ferme
from app.menus.menu_interface import MenuInterface
from app.features.users.individu import Individu
from app.security.id import verif_init_id
from app.security.mdp import verif_init_mdp
from app.dao.guestDao import GuestDAO
from app.features.users.guestView import GuestView
import hashlib


class Guest(Individu):

    """ classe invité, pouvant jouer au jeu sans se connecter """

    def __init__(self):
        # l'id d'un guest est genéré quand il souhaite jouer et non au lancement
        self.identifiant = "id"
        # Et on définit que pour l'instant c'est un guest, on modifie l'attribut quand il se connecte
        self.userType = "Guest"

    @staticmethod

    def createAccount():
        # entrer le nom d'utilisateur + vérifier qu'il n'existe pas déjà
        (username,motdepasse, verifMotdepasse) = GuestView.displayCreateAccount()
        username=verif_init_id(username)
        # vérifie que les deux mdp sont les mêmes et renvoie le mdp
        motdepasse = verif_init_mdp(motdepasse, verifMotdepasse)


        # code pour hasher le mdp
        m = hashlib.md5()
        m.update(motdepasse)
        hash_mdp = m.digest()

        # ajouter le compte à la base
        GuestDAO.addAccounttoData(username, hash_mdp)

    def connexion():
        """Permet à un utilisateur de se connecter """
        (username, motdepasse) = GuestView.displayConnexion()

        # code pour hasher le mdp
        m = hashlib.md5()
        m.update(motdepasse)
        hash_mdp = m.digest()

        # on demande à GuestDAO  de créer l'instance de l'objet
        GuestDAO.checkAccounttoData(username, hash_mdp)

    def initEmptyGame():
        """initialise un jeu vide """ ###comment récupérer le choix du jeu avec les menus ?
        GuestDAO.addGame(jeu)


    def joinGame(): 
        """ Rejoindre un groupe pour jouer à une partie qui n'a aps encore commencé"""
        # A AJOUTER ICI !!!!!!!!!!!!!!!!!!!!!  comment récupérer le choix du jeu avec les menus ?
        GuestDAO.printReadytoStartGames(jeu)
        idGame = GuestView.displayChoixPartie()
        GuestDAO.addPlayerToGame(idGame)
        
