from app.security.id import verif_init_id
from app.security.mdp import verif_init_mdp
from app.DAO.guestDao import guestDAO
from app.DAO.adminDAO import adminDAO
import hashlib

class Admin(Player):
    
    """
    trois méthodes
    
    createPlayerAccount()
    deletePlayerAccount()
    seePlayerAccount()
    
    """
    
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

"""moitié ds la DAO moitié ici"""
        adminDAO.getAllUserData(username) 
        
        pass
    
    def seeUserAccount():
        
        "utiliser la fct de admin dao"

        pass
