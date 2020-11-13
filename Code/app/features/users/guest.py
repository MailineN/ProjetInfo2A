from app.menus.menu_interface import Ferme
from app.menus.menu_interface import MenuInterface
from app.features.users.individu import Individu
from app.security.id import verif_init_id
from app.security.mdp import verif_init_mdp
from app.features.DAO.guestDAO import GuestDAO
from app.features.users.guestView import GuestView
import hashlib


class Guest(Individu):

    """ classe invité, pouvant jouer au jeu sans se connecter """

    def __init__(self, identifiant=None, handList=[]):
        # l'id d'un guest est genéré quand il souhaite jouer et non au lancement
        self.identifiant = identifiant
        # Et on définit que pour l'instant c'est un guest, on modifie l'attribut quand il se connecte
        self.userType = 'Guest'
        self.handList = handList

    @staticmethod
    def createAccount(previous_menu):
        # entrer le nom d'utilisateur + vérifier qu'il n'existe pas déjà
        (username, motdepasse, verifMotdepasse) = GuestView.displayCreateAccount()
        while not verif_init_id(username):
            username = GuestView.displayVerifId()
        # vérifie que les deux mdp sont les mêmes et renvoie le mdp
        while not verif_init_mdp(motdepasse, verifMotdepasse):
            (mdp, vmdp) = GuestView.displayVerifMdp()

        # code pour hasher le mdp
        m = hashlib.md5()
        m.update(motdepasse)
        hash_mdp = m.digest()

        # ajouter le compte à la base
        GuestDAO.addAccounttoData(username, hash_mdp)
        print("Votre compte a bien été crée \n Appuyez sur Entrer pour continuer")
        return MenuInterface(previous_menu)

    def connexion(listPlayers):
        """Permet à un utilisateur de se connecter """
        (username, motdepasse) = GuestView.displayConnexion()

        # code pour hasher le mdp
        m = hashlib.md5()
        m.update(motdepasse)
        hash_mdp = m.digest()

        # on demande à GuestDAO  de créer l'instance de l'objet
        id_users = GuestDAO.checkAccounttoData(username, hash_mdp)
        listPlayers.append(id_users)
        return(listPlayers)

    def initEmptyGame():
        """initialise un jeu vide """  # comment récupérer le choix du jeu avec les menus ?
        GuestDAO.addGame(jeu)

    def joinGame():
        """ Rejoindre un groupe pour jouer à une partie qui n'a aps encore commencé"""
        # A AJOUTER ICI !!!!!!!!!!!!!!!!!!!!!  comment récupérer le choix du jeu avec les menus ?
        GuestDAO.printReadytoStartGames(jeu)
        idGame = GuestView.displayChoixPartie()
        GuestDAO.addPlayerToGame(idGame)
