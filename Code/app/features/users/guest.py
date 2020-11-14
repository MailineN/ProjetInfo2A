
from app.features.users.individu import Individu
from app.security.id import verif_init_id
from app.security.mdp import verif_init_mdp
from app.features.DAO.guestDAO import GuestDAO
from app.features.users.guestView import GuestView
import hashlib
from app.features.DAO.gameDAO import GameDAO
from app.features.game.gameMechanics.belote import Belote
from app.menus.menu_interface import MenuInterface


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
            (motdepasse, verifMotdepasse) = GuestView.displayVerifMdp()

        # code pour hasher le mdp
        hash_mdp = hashlib.sha256(motdepasse.encode()).hexdigest()

        print(hash_mdp)
        # ajouter le compte à la base
        GuestDAO.addAccounttoData(username, hash_mdp)
        input("Votre compte a bien été crée \n Appuyez sur Entrer pour continuer ")
        return MenuInterface(previous_menu)

    @staticmethod
    def connexionJeu(listPlayers):
        """Permet à un utilisateur de se connecter ou de rejoindre un jeu sans se connecter"""
        if GuestView.displayChoixPartie():
            id_users = Guest.connexion()
            listPlayers.append(id_users)
        else:
            # Si le joueur ne souhaite pas se connecter, on lui assigne un identifiant temporaire
            listPlayers.append('invité'+str(len(listPlayers)))
        return(listPlayers)

    # Les fonctions d'initialisation de jeu ont étés ajoutés à GameService :)
    # T'inquiete pas pour les menus c'est prévu

    @staticmethod
    def connexion():
        id_users = None
        while id_users is None:
            (username, motdepasse) = GuestView.displayConnexion()

            # code pour hasher le mdp
            hash_mdp = hashlib.sha256(motdepasse.encode()).hexdigest()
            print(hash_mdp)
            # on demande à GuestDAO  de créer l'instance de l'objet
            id_users = GuestDAO.checkAccounttoData(username, hash_mdp)
            if len(id_users) > 0:
                input("Vous êtes connectés ! ")
            else:
                input("Echec de la connexion ")
        return id_users


class GameService:

    def __init__(self):
        pass

    @staticmethod
    def startGame(nomJeu, idJeu, PlayerGroup):
        if nomJeu == 'Belote':
            return(Belote(idJeu, PlayerGroup, False).gameLoop(idJeu))

    @staticmethod
    def initListPlayers(jeu):
        listPlayers = []
        if jeu == 'Belote':
            while not Belote.checkPlayerNumber(listPlayers):
                listPlayers = Guest.connexionJeu(listPlayers)
        return(listPlayers)

    @staticmethod
    def initEmptyGame(nomJeu, previous_menu):
        """initialise un jeu vide du jeu sélectionné avec une liste de joueur complete """
        listPlayers = GameService.initListPlayers(nomJeu)
        listString = ' '.join(map(str, listPlayers))
        # Convertit la liste de joueur [1,2,3] en string '1 2 3'
        id_Jeu = GameDAO.addGame(nomJeu, listString)
        GameService.startGame(nomJeu, id_Jeu, listPlayers)
        return MenuInterface(previous_menu)
