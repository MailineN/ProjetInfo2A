from app.menus.menu_interface import Ferme
from app.menus.menu_interface import MenuInterface
from .individu import Individu
from app.security.id import verif_init_id
from app.security.mdp import verif_init_mdp
from app.DAO.adminDAO import adminDAO
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

    def createPlayerAccount():
        
        #création du compte
        username = verif_id(input("Entrez votre nom d'utilisateur")) 
        motdepasse = input("Choisissez votre mot de passe")
        verifMotdepasse= input("Réécrivez votre mot de passe")
        motdepasse = verif_init_mdp(motdepasse, verifMotdepasse) #voir que le mdp est bon


        #hashage du mdp
        m = hashlib.md5()
        m.update(motdepasse)
        hash_mdp = m.digest()


        #ajouter le nouveau compte à la base
        GuestDAO.addAccounttoData(username,hash_mdp)
        return("Le compte a bien été créé")

        
        pass
    

    def deletePlayerAccount():

        
        
        pass
    
    def seePlayerAccount():
        
        pass
