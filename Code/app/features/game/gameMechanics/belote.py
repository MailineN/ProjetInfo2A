from abstractgame import AbstractGame
from cardObjects.cards import Color, Rank, Card 



class Belote(AbstractGame, Color, Rank, Card):
    
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
        pass
    
    def toorLoop(self):
        pass
 

    Atout = []
    
    def CreateTeams():
        team1=[]
        team2=[]
        print("Nous allons former les équipes")
        team1.append(input("Equipe 1 : Joueur 1 :"))
        team1.append(input("Equipe 1 : Joueur 2 :"))
        team2.append(input("Equipe 2 : Joueur 1 :"))
        team2.append(input("Equipe 2 : Joueur 2 :"))
     
    def CheckPlayerNumber(players):
        if len(players) < 4 :
            print("Il n'y a pas assez de joueurs")
        elif len(players) > 4 :
            print("Il y a trop de joueurs")
        else:
            print("Nous allons bientôt composer les équipes")
        
    point_atout = {"jack":20,"nein":14,"ace":11,"ten":10,"king":4,"queen":3,"eight":0,"seven":0}
 
 
    point_noatout = ["ace":11,"ten":10,"king":4,"queen":3,"jack":2,"nein":0,"eight":0,"seven":0]    
 
    def CountPoint():
        score1=0
        score2=0