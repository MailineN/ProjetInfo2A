from guest import Guest


class PlayerGroup :

    def __init__(self, players = list[Guest]) :
    
        self.players = players
        self.nbplayers = len(self.players)
        self.id = ""
        for player in players :
            self.id += " " + player.id

    def addPlayer(self, Guest) :
        self.players.append(Guest)
        self.id += " " + Guest.id
    
    def removePlayer(self, Guest) :
        ide = Guest.identifiant
        newplayers = []
        newid = ""
        for i in range(self.nbplayers) :
            player = self.players[i]
            if not(ide == player.identifiant) :
                newplayers.append(player)
                newid += " " + player.id
        self.players = newplayers
        self.id = newid

