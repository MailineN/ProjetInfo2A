from app.security.id import verif_init_id
from app.security.mdp import verif_init_mdp
from app.DAO.guestDao import guestDAO
from app.DAO.adminDAO import adminDAO
from app.users.adminView import adminView
import hashlib

class Admin(Player):
  
    def __init__(self):
        
        super
        
        Player.__init__(self, identifiant, "Admin") #il hérite de l'attribut userType

    def createUserAccount():
       """ fct à changer par rapport à la view ou on la laisse comme ca??? je me base sur le guest qui reste comme ca pr la création mais la view?? """ 
        #demander si on veut créer un joueur ou un admin
        userType = adminView.displayUsertype()
        if userType == "Player":
            #création du compte d'un joueur
            (username, mdp, verifMdp) = adminView.displayCreateUserAccount()
            #vérification que le pseudo n'existe pas déjà
            username=verif_init_id(username)
            #vérification que les deux mdp sont les mêmes et renvoie le mdp
            mdp = verif_init_mdp(mdp, verifmdp)
            #hashage du mdp choisi
            m = hashlib.md5()
            m.update(mdp)
            hash_mdp = m.digest()
            # ajouter le compte à la base
            GuestDAO.addAccounttoData(username, hash_mdp)
            return("Votre compte a bien été créé")

        elif userType == "Admin":
            #création du compte d'un admin
            (username, mdp, verifMdp) = adminView.displayCreateUserAccount()
            #vérification que le pseudo n'existe pas déjà
            username=verif_init_id(username)
            #vérification que les deux mdp sont les mêmes et renvoie le mdp
            mdp = verif_init_mdp(mdp, verifmdp)
            #hashage du mdp choisi
            m = hashlib.md5()
            m.update(mdp)
            hash_mdp = m.digest()            
            #ajouter le nouveau compte à la base en appelant la fonction de guestDAO
            GuestDAO.addAccounttoData(username,mdp)
            return("Le compte a bien été créé")

    def deleteUserAccount():
        #la view va aller demander à l'utilisateur quel compte il veut supprimer à partir de son username
        adminView.displayDeleteUserAccount(username)           
        #la fonction de adminDAO va aller supprimer ce compte dans la base
        adminDAO.deleteUserAccount(username)
        return("Le compte a bien été supprimé") 
    
    def seeUserAccount():
        #la view va aller demander à l'utilisateur quel compte il veut consulter à partir de son username
        adminView.displaySeeUserAccount(username)
        #la fonction de adminDAO va aller récupérer ces informations dans la base (et les retourner ? ou il faut que je fasse un return ici?)
        adminDAO.getAllUserData(username)


