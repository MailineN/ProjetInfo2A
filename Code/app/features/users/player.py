from app.features.users.guest import Guest
from app.features.DAO.playerDAO import PlayerDAO
from app.features.users.playerView import PlayerView
from app.features.DAO.gameDAO import GameDAO 
import hashlib

class Player(Guest):

    def __init__(self, identifiant, handList):
        super.__init__(self, identifiant, 'Player', handList)

    def loadGame(self, jeu, idGame):  # jeu est le nom du jeu que veut charger l'utilisateur
        # code à intégrer pour savoir quel game il veut (par ex, si il veut récup
        # les codes de la belote, quelle partie veut-il ?? On récup idGame et on l'utilise
        # comme argument)
        PlayerDAO.fetchGame(idGame)

    def changePassword(self):
        """ Changer le mot de passe d'un utilisateur """
        (motdepasse, new_mdp) = PlayerView.displayChangePassword

        m = hashlib.md5()
        m.update(motdepasse)
        hash_mdp = m.digest()
        m.update(new_mdp)
        new_hash_mdp = m.digest

        # laisser faire la classe playerDAO
        PlayerDAO.updatePassword(hash_mdp, new_hash_mdp)

    def seeScores(self):
        """Affiche les scores en appellant la fonction correspondante dans la DAO"""
        return(PlayerDAO.getAccountData(self))
