from .guest import Guest
class Player(Guest):
    
    def __init__(self, identifiant):
        
        Guest.__init__(self, identifiant, 'Player')

    
    def loadGame(self):
        pass
    
    def changePassword(self):
        """ Changer le mot de passe d'un utilisateur """
        motdepasse = input("Entrez votre mot de passe actuel")
        new_mdp = input("Entrez votre nouveau mot de passe")

        m = hashlib.md5()
        m.update(motdepasse)
        hash_mdp = m.digest()
        m.update(new_mdp)
        new_hash_mdp = m.digest

        #laisser faire la classe playerDAO
        PlayerDAO.updatePassword(hash_mdp, new_hash_mdp)

        pass
    
    def seeScores(self) :
        pass
    
    def continuePreviousGame(self) :
        pass
    

   