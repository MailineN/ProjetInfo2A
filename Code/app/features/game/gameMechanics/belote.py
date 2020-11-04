from abstractgame import AbstractGame
from cardObjects.deck import PileCard




class Belote(AbstractGame):
    
   def __init__(self, players=[], deck=None,victoryCondition = None, tourCondition = None, finished = false,listCards = []):
        super.__init__(
            players = list(players),    
            deck = deck,        
            victoryCondition = victoryCondition,
            tourCondition = tourCondition,
            finished = finished,
            listCards = listCards
        )
    
    def gameLoop(self):
        place_player = [team1[0],team2[0],team1[1],team2[1]]
        generateNewCustomDeck
    
    def toorLoop(self):
        pass
 
    
    def CreateTeams():
        team1=[]
        team2=[]
        print("Nous allons former les équipes")
        team1.append(input("Equipe 1 : Joueur 1 :"))
        team1.append(input("Equipe 1 : Joueur 2 :"))
        team2.append(input("Equipe 2 : Joueur 1 :"))
        team2.append(input("Equipe 2 : Joueur 2 :"))
        return (team1,team2)
        
    def CheckPlayerNumber(players):
        if len(players) != 4 :
            raise Error 
        


    point_atout = {"jack":20,"nein":14,"ace":11,"ten":10,"king":4,"queen":3,"eight":0,"seven":0}
    point_noatout = ["ace":11,"ten":10,"king":4,"queen":3,"jack":2,"nein":0,"eight":0,"seven":0]    
 




    def CountPoint():
      pass

