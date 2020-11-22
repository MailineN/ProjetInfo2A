""" Classe Guest, gérant l'ensemble des actions possibles avant de commencer 
    une partie de jeu ou une connexion
"""
from app.features.users.individu import Individu
from app.security.id import verif_init_id
from app.security.mdp import verif_init_mdp
from app.features.DAO.guestDAO import GuestDAO
from app.features.users.guestView import GuestView
import hashlib
from app.menus.menu_interface import MenuInterface


class Guest(Individu):

    def __init__(self, identifiant=None, handList=[]):
        """ Le Guest est initialisé avec un identifiant et une main servant lors 


        Args:
            identifiant (str, optional): Defaults to None.
            handList (list, optional): Liste des cartes de la main du joueur. Defaults to [].
        """
        # l'id d'un guest est genéré quand il souhaite jouer et non au lancement
        self.identifiant = identifiant
        # Et on définit que pour l'instant c'est un guest, on modifie l'attribut quand il se connecte
        self.userType = 'Guest'
        self.handList = handList

    @staticmethod
    def createAccount(previous_menu):
        """ Fonction permettant à l'invité de se créer un compte
            et de l'enregistrer dans la base des données
        """
        # entrer le nom d'utilisateur + vérifier qu'il n'existe pas déjà
        (username, motdepasse, verifMotdepasse) = GuestView.displayCreateAccount()
        while not verif_init_id(username):
            username = GuestView.displayVerifId()
        # vérifie que les deux mdp sont les mêmes et renvoie le mdp
        while not verif_init_mdp(motdepasse, verifMotdepasse):
            (motdepasse, verifMotdepasse) = GuestView.displayVerifMdp()

        # code pour hasher le mdp
        hash_mdp = hashlib.sha256(motdepasse.encode()).hexdigest()
        # ajouter le compte à la base
        GuestDAO.addAccounttoData(username, hash_mdp)
        input("Votre compte a bien été crée \n Appuyez sur Entrer pour continuer ")
        return MenuInterface(previous_menu)

    @staticmethod
    def connexionJeu(listPlayers):
        """Permet à un utilisateur de se connecter ou de rejoindre un jeu sans se connecter"""
        
        if GuestView.displayChoixPartie():
            id_users = Guest.connexion()
            if len(id_users) > 0 and id_users[0]['username'] not in listPlayers:
                listPlayers.append(id_users[0]['username'])
            if id_users[0]['username'] in listPlayers:
                input("Vous êtes déjà connecté au sein de la partie ")
        else:
            
            # Si le joueur ne souhaite pas se connecter, on lui assigne un identifiant temporaire
            listPlayers.append('invité'+str(len(listPlayers)))
        return(listPlayers)

    # Les fonctions d'initialisation de jeu ont étés ajoutés à GameService :)
    # T'inquiete pas pour les menus c'est prévu

    @staticmethod
    def connexion():
        """ Fonction permettant à l'invité de se connecter
            Fonction générique reprise lors de la connexion au 
            jeu ou pour effectuer des actions
        """
        id_users = []
        (username, motdepasse) = GuestView.displayConnexion()

        # code pour hasher le mdp
        hash_mdp = hashlib.sha256(motdepasse.encode()).hexdigest()
        print(hash_mdp)
        # on demande à GuestDAO  de créer l'instance de l'objet
        id_users = GuestDAO.checkAccounttoData(username, hash_mdp)
        if len(id_users) > 0:
            input("Vous êtes connecté ! ")
        else:
            input("Echec de la connexion ")
        return id_users
