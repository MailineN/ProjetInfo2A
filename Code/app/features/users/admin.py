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
        super().__init__(identifiant, handList)
        self.userType = 'Admin'
        self.connecte = False

    def createAdminAccount(self, previous_menu):
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
        if not self.connecte:
            input("Vous n'êtes pas connecté ")
        else:
            users = AdminDAO.getAllUserData()
            for user in users:
                print("• Nom : "+user[1]+", Administrateur : " +
                      str(user[3]) + ", Scores : " + str(user[5]) + "\n")
            input(" \n Affichage terminé ")
        return MenuInterface(previous_menu)

    def seeGameData(self, previous_menu):
        if not self.connecte:
            input("Vous n'êtes pas connecté ")
        else:
            games = AdminDAO.getAllGameData()
            print(games)

            input(" \n Affichage terminé ")
        return MenuInterface(previous_menu)

    def resetDatabase(self, previous_menu):
        if not self.connecte:
            input("Vous n'êtes pas connecté ")
        else:
            games = AdminDAO.getAllGameData()
            print(games)
            input(" \n Affichage terminé ")
        return MenuInterface(previous_menu)

    def connexion(self):
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
