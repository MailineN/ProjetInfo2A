import uuid
from app.features.users.guest import Guest


class PlayerGroup :

    def __init__(self, idend = None, players = list[Guest]) :
        self.id = idend
        self.players = players
        self.nbplayers = len(self.players)

    def addPlayer(self, Guest) :
        self.players.append(Guest)
    
    def removePlayer(self, Guest) :
        ide = Guest.identifiant
        newplayers = []
        for i in range(self.nbplayers) :
            player = self.players[i]
            if not(ide == player.identifiant) :
                newplayers.append(player)
        self.players = newplayers