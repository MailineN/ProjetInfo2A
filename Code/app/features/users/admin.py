from app.security.id import verif_init_id
from app.security.mdp import verif_init_mdp
from app.features.DAO.guestDAO import GuestDAO
from app.features.DAO.adminDAO import AdminDAO
from app.features.users.adminView import AdminView
import hashlib
from app.features.users.player import Player
from app.menus.menu_interface import MenuInterface

class Admin(Player):

    def __init__(self):

        super().__init__(identifiant = "Admin",
        handList = []
        )


    def createUserAccount(previous_menu):
        """ fct à changer par rapport à la view ou on la laisse comme ca??? je me base sur le guest qui reste comme ca pr la création mais la view?? """
        # demander si on veut créer un joueur ou un admin
        userType = AdminView.displayUsertype()
        if userType == "Player":
            # création du compte d'un joueur
            (username, mdp, verifMdp) = AdminView.displayCreateUserAccount()
            # vérification que le pseudo n'existe pas déjà
            while not verif_init_id(username):
                username = AdminView.displayVerifId()
            # vérification que les deux mdp sont les mêmes et renvoie le mdp
            while not verif_init_mdp(mdp, verifMdp):
                (mdp, verifMdp) = AdminView.displayVerifMdp()

            # hashage du mdp choisi
            m = hashlib.md5()
            m.update(mdp)
            hash_mdp = m.digest()
            # ajouter le compte à la base
            GuestDAO.addAccounttoData(username, hash_mdp)
            print("Le compte a bien été crée \n Appuyez sur Entrer pour continuer")
            return MenuInterface(previous_menu)

        elif userType == "Admin":
            # création du compte d'un admin
            (username, mdp, verifMdp) = AdminView.displayCreateUserAccount()
            # vérification que le pseudo n'existe pas déjà
            username = verif_init_id(username)
            # vérification que les deux mdp sont les mêmes et renvoie le mdp
            mdp = verif_init_mdp(mdp, verifMdp)
            # hashage du mdp choisi
            m = hashlib.md5()
            m.update(mdp)
            hash_mdp = m.digest()
            # ajouter le nouveau compte à la base en appelant la fonction de guestDAO
            AdminDAO.addAdminAccounttoData(username, hash_mdp)
            print("Le compte a bien été crée \n Appuyez sur Entrer pour continuer")
            return MenuInterface(previous_menu)

    def deleteUserAccount(previous_menu):
         # la view va aller demander à l'utilisateur quel compte il veut supprimer à partir de son username
        username = AdminView.displayDeleteUserAccount()
        # la fonction de adminDAO va aller supprimer ce compte dans la base
        AdminDAO.deleteUserAccount(username)
        print("Le compte a bien été supprimé \n Appuyez sur Entrer pour continuer")
        return MenuInterface(previous_menu)

    def seeUserAccount():
        # la view va aller demander à l'utilisateur quel compte il veut consulter à partir de son username
        username = AdminView.displaySeeUserAccount()
        # la fonction de adminDAO va aller récupérer ces informations dans la base (et les retourner ? ou il faut que je fasse un return ici?)
        AdminDAO.getAllUserData(username)
