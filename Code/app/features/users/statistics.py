class Statistics :

    def __init__(self,playerid) :
        self.numberVictory = 0
        self.playerid = playerid
    
    def update(self) :
        self.numberVictory += 1