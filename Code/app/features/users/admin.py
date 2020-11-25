""" Classe Administrateur

Regroupement des methodes permetant à l'administrateur de gérer la base de donnée 
utilisateur et des jeux. 

"""
from app.security.id import verif_init_id
from app.security.mdp import verif_init_mdp
from app.features.DAO.guestDAO import GuestDAO
from app.features.DAO.adminDAO import AdminDAO
from app.features.users.adminView import AdminView
from app.features.users.guestView import GuestView
import hashlib
from app.features.users.player import Player
from app.menus.menu_interface import MenuInterface


class Admin(Player):

    def __init__(self, identifiant=None, handList=[]):
        """ Initialisation d'un objet Admin qui reprend les fonctionalités 
        des Players avec des autorisations supplémentaires en pratique, un administrateur ne sera 
        jamais instancié au cours d'une partie

        Args : 
            identifiant : str : Pseudo de l'administrateur
            handList : list : Main de l'administrateur, vide en pratique
            userType : str : Permet de vérifier le statut de l'administrateur lors 
                lancement de fonctionalités propres
            connecte : bool : Vérifie si l'administrateur est connecté lors du lancement des
                fonctions propres
        """
        super().__init__(identifiant, handList)
        self.userType = 'Admin'
        self.connecte = False

    def createAdminAccount(self, previous_menu):
        """ Fonction permetant à l'administrateur de créer un nouveau compte administrateur
            Reprend les mêmes methodes que celles des guests
        Args : 
            previous_menu : Menu précédent dans lequel l'utilisateur est renvoyé à la fin de la fonction
        """
        if not self.connecte:
            input("Vous n'êtes pas connecté ")
        else:
            (username, motdepasse, verifMotdepasse) = GuestView.displayCreateAccount()
            while not verif_init_id(username):
                username = GuestView.displayVerifId()
            # vérifie que les deux mdp sont les mêmes et renvoie le mdp
            while not verif_init_mdp(motdepasse, verifMotdepasse):
                (motdepasse, verifMotdepasse) = GuestView.displayVerifMdp()

            # code pour hasher le mdp
            hash_mdp = hashlib.sha256(motdepasse.encode()).hexdigest()
            # ajouter le compte à la base
            GuestDAO.addAccounttoData(username, hash_mdp, True)

        return MenuInterface(previous_menu)

    def deleteUserAccount(self, previous_menu):
        """ Fonction permetant à l'administrateur de supprimer un compte utilisateur
            à partir de son pseudo
        Args : 
            previous_menu : Menu précédent dans lequel l'utilisateur est renvoyé à la fin de la fonction
        """
        if not self.connecte:
            input("Vous n'êtes pas connecté ")
        else:
            # la view va aller demander à l'utilisateur quel compte il veut supprimer à partir de son username
            username = AdminView.displayDeleteUserAccount()
            # la fonction de adminDAO va aller supprimer ce compte dans la base
            AdminDAO.deleteUserAccount(username)
            input("Le compte a bien été supprimé \n Appuyez sur Entrer pour continuer ")
        return MenuInterface(previous_menu)

    def seeUserData(self, previous_menu):
        """ Fonction permetant à l'administrateur de visualiser l'ensemble des
            comptes utilisateurs
        Args : 
            previous_menu : Menu précédent dans lequel l'utilisateur est renvoyé à la fin de la fonction
        """
        if not self.connecte:
            input("Vous n'êtes pas connecté ")
        else:
            users = AdminDAO.getAllUserData()
            for user in users:
                print("• Nom : "+user[1]+" || Administrateur : " +
                      str(user[3]) + " || Scores : " + str(user[5]) + "\n")
            input(" \n Affichage terminé ")
        return MenuInterface(previous_menu)

    def seeGameData(self, previous_menu):
        """ Fonction permetant à l'administrateur de visualiser l'ensemble des
            parties de jeu, terminées ou non
        Args : 
            previous_menu : Menu précédent dans lequel l'utilisateur est renvoyé à la fin de la fonction
        """
        if not self.connecte:
            input("Vous n'êtes pas connecté ")
        else:
            games = AdminDAO.getAllGameData()
            for game in games:
                print("• Nom du Jeu : "+game[1]+"|| Joueurs : " +
                      str(game[2]) + "|| Scores : " + str(game[3]) + "\n")

            input(" \n Affichage terminé ")
        return MenuInterface(previous_menu)

    def resetDatabase(self, previous_menu):
        """ Fonction permetant à l'administrateur de réinitialiser la base de données
            en conservant uniquement les comptes utilisateurs
        Args : 
            previous_menu : Menu précédent dans lequel l'utilisateur est renvoyé à la fin de la fonction
        """
        if not self.connecte:
            input("Vous n'êtes pas connecté ")
        else:
            confirm = AdminView.displayResetDataBase()
            if confirm == 'SUPPRIMER':
                AdminDAO.initDatabase()
                users = AdminDAO.getAllUserData()
                for user in users:
                    print("• Nom : "+user[1]+", Administrateur : " +
                          str(user[3]) + ", Scores : " + str(user[5]) + "\n")
                input(" \n Suppression terminée ")
            else:
                input("La suppression n'a pas abouti ")
        return MenuInterface(previous_menu)

    def connexion(self):
        """ Fonction de connexion propre à l'administrateur
        """
        (username, motdepasse) = GuestView.displayConnexion()

        # code pour hasher le mdp
        hash_mdp = hashlib.sha256(motdepasse.encode()).hexdigest()
        # on demande à GuestDAO  de créer l'instance de l'objet
        admin = AdminDAO.checkAccounttoData(username, hash_mdp)
        if admin:
            input("Vous êtes connecté en tant qu'admin ! ")
            self.connecte = True
        else:
            input("Vous ne possédez pas les droits d'administrateur ")
        return admin
