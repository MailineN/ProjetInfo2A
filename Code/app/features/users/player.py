from .guest import Guest
from app.features.DAO.playerDAO import getAccountData
from app.features.users.playerView import PlayerView

class Player(Guest):
    
    def __init__(self, identifiant):
        
        Guest.__init__(self, identifiant, 'Player')

    
    def loadGame(self):
        pass
    
    def changePassword(self):
        """ Changer le mot de passe d'un utilisateur """
       (motdepasse,new_mdp)= PlayerView.displayChangePassword()

        m = hashlib.md5()
        m.update(motdepasse)
        hash_mdp = m.digest()
        m.update(new_mdp)
        new_hash_mdp = m.digest

        #laisser faire la classe playerDAO
        PlayerDAO.updatePassword(hash_mdp, new_hash_mdp)
    
    def seeScores(self) :
        """Affiche les scores en appellant la fonction correspondante dans la DAO"""
        return(getAccountData(self))
    
    def continuePreviousGame(self) :
        pass
    

   