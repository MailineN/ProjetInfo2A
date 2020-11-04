from app.security.id import verif_init_id
from app.security.mdp import verif_init_mdp
from app.DAO.guestDao import guestDAO
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
            PlayerUsername = verif_id(input("Entrez le nom d'utilisateur")) 
            PlayerMotdepasse = input("Choisissez le mot de passe")
            verifMotdepasse= input("Réécrivez le mot de passe")
            motdepasse = verif_init_mdp(motdepasse, verifMotdepasse) #voir que le mdp est bon
            #hashage du mdp choisi
            m = hashlib.md5()
            m.update(PlayerMotdepasse)
            hash_mdp = m.digest()

        elif userType == "Admin":
            #création du compte d'un admin
            AdminUsername = verif_id(input("Entrez le nom d'utilisateur")) 
            AdminMotdepasse = input("Choisissez le mot de passe")
            verifMotdepasse= input("Réécrivez le mot de passe")
            motdepasse = verif_init_mdp(motdepasse, verifMotdepasse) #voir que le mdp est bon
            #hashage du mdp choisi
            m = hashlib.md5()
            m.update(AdminMotdepasse)
            hash_mdp = m.digest()

        #ajouter le nouveau compte à la base
        GuestDAO.addAccounttoData(username,hash_mdp)
        return("Le compte a bien été créé")

        
        pass
    

    def deletePlayerAccount():

"""moitié ds la DAO moitié ici"""

        
        pass
    
    def seePlayerAccount():
        
        "utiliser la fct de admin dao"

        pass
