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
        


    point_atout = {"JACK":20,"9":14,"ACE":11,"10":10,"KING":4,"QUENN":3,"8":0,"7":0}
    point_noatout = {"ACE":11,"10":10,"KING":4,"QUENN":3,"JACK":2,"9":0,"8":0,"7":0}    
 




    def CountPoint():
      pass

