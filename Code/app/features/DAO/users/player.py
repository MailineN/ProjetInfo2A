from .guest import Guest
class Player(Guest):
    
    def __init__(self, identifiant):
        
        Guest.__init__(self, identifiant, 'Player')

    
    def loadGame(self):
        pass
    
    def changePassword(self):
        pass
    
    def seeScores(self) :
        pass
    
    def continuePreviousGame(self) :
        pass
    

   