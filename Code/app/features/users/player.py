from app.features.users.guest import Guest
from app.features.DAO.playerDAO import PlayerDAO
from app.features.users.playerView import PlayerView

import hashlib

class Player(Guest):

    def __init__(self, identifiant, handList):
        super.__init__(self, identifiant, 'Player', handList)

   

    def changePassword():
        """ Changer le mot de passe d'un utilisateur """
        (motdepasse, new_mdp) = PlayerView.displayChangePassword()

        newhash_mdp = hashlib.sha256(new_mdp.encode()).hexdigest()
        hash_mdp = hashlib.sha256(motdepasse.encode()).hexdigest()
        # laisser faire la classe playerDAO
        PlayerDAO.updatePassword(hash_mdp, newhash_mdp)

    def seeScores():
        """Affiche les scores en appellant la fonction correspondante dans la DAO"""
        return(PlayerDAO.getAccountData())
