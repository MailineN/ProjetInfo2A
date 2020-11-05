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
        userType = input("voulez vous créer un Joueur ou un Admin ?") #faire un truc pr que tout passe selon si ils mettent des maj et tout 

        if userType == "Player":
            #création du compte d'un joueur
            username = verif_id(input("Entrez le nom d'utilisateur")) 
            mdp = input("Choisissez le mot de passe")
            verifmdp= input("Réécrivez le mot de passe")
            mdp = verif_init_mdp(mdp, verifmdp) #voir que le mdp est bon
            #hashage du mdp choisi
            m = hashlib.md5()
            m.update(mdp)
            hash_mdp = m.digest()

        elif userType == "Admin":
            #création du compte d'un admin
            username = verif_id(input("Entrez le nom d'utilisateur")) 
            mdp = input("Choisissez le mot de passe")
            verifmdp= input("Réécrivez le mot de passe")
            mdp = verif_init_mdp(mdp, verifmdp) #voir que le mdp est bon
            #hashage du mdp choisi
            m = hashlib.md5()
            m.update(mdp)
            hash_mdp = m.digest()

        #ajouter le nouveau compte à la base en appelant la fonction de guestDAO
        GuestDAO.addAccounttoData(username,mdp)
        return("Le compte a bien été créé")

    def deleteUserAccount():
        #la view va aller demander à l'utilisateur quel compte il veut supprimer à partir de son username
        adminView.displayDeleteUserAccount(username,mdp)           
        #la fonction de adminDAO va aller supprimer ce compte dans la base
        adminDAO.deleteUserAccount(username,mdp)
        return("Le compte a bien été supprimé") 
    
    def seeUserAccount():
        #la view va aller demander à l'utilisateur quel compte il veut consulter à partir de son username
        adminView.displaySeeUserAccount(username,mdp)
        #la fonction de adminDAO va aller récupérer ces informations dans la base (et les retourner ? ou il faut que je fasse un return ici?)
        adminDAO.getAllUserData(username,mdp)


