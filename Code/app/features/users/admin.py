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

        #ajouter le nouveau compte à la base
        GuestDAO.addAccounttoData(username,hash_mdp)
        return("Le compte a bien été créé")

        
        pass
    

    def deleteUserAccount():
       """utiliser la fct "displayDeleteUserAccount" de admin view pr parler à l'utilisateur
          utiliser la fct "deleteUserAccount" de admin dao pr supprimer le compte dans la base de données"""
        adminView.displayDeleteUserAccount()        
        adminDAO.deleteUserAccount(username)
         
        
        pass
    
    def seeUserAccount():
        """utiliser la fct "displaySeeUserAccount" de admin view pr parler à l'utilisateur
        utiliser la fct "getAllUserData" de admin dao pr avoir accès aux informations de l'utlisateur"""
        adminView.displaySeeUserAccount()
        adminDAO.getAllUserData(username)

        pass
