from app.menus.menu_interface import Ferme
from app.menus.menu_interface import MenuInterface
from .individu import Individu
from app.security.id import verif_init_id
from app.security.mdp import verif_init_mdp
from app.DAO.guestDao import GuestDAO
from guestView import GuestView
import hashlib


class Guest(Individu):

    """ classe invité, pouvant jouer au jeu sans se connecter """

    def __init__(self):
        # l'id d'un guest est genéré quand il souhaite jouer et non au lancement
        self.identifiant = "id"
        # Et on définit que pour l'instant c'est un guest, on modifie l'attribut quand il se connecte
        self.userType = "Guest"

    @staticmethod
    def play():
        pass

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
        return("Votre compte a bien été créé")

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

        GameService.initJeu(TRUE)

    def joinGame():
        
        GameService.initJeu(FALSE)

    def displayFinishedGame():
        pass
