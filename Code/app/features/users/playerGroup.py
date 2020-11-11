import uuid
from app.features.users.guest import Guest


class PlayerGroup :

    def __init__(self, players = list[Guest]) :
        self.players = players
        self.nbplayers = len(self.players)
        self.id = ""
        for player in self.players :
            self.id += player.identifiant + " "
        self.id = self.id[:len(self.id)-1]

    def addPlayer(self, Guest) :
        self.players.append(Guest)
    
    def removePlayer(self, Guest) :
        ide = Guest.identifiant
        newplayers = []
        newid = ""
        for i in range(self.nbplayers) :
            player = self.players[i]
            if not(ide == player.identifiant) :
                newplayers.append(player)
                newid += player.identifiant + " "
        self.players = newplayers
        self.id = newid[:len(newid)-1]
        