from abstractgame import AbstractGame
from cardObjects.deck import PileCard




class Belote(AbstractGame):
    
   def __init__(self, players=[], deck=None,victoryCondition = None, tourCondition = None, finished = false):
        super.__init__(
            players = list(players),    
            deck = deck,        
            victoryCondition = victoryCondition,
            tourCondition = tourCondition,
            finished = finished,
            listCards = "7S,7D,7C,7H,8S,8D,8C,8H,9S,9D,9C,9H,0S,\
            0D,0C,0H,JS,JD,JC,JH,QS,QD,QC,QH,KS,KD,KC,KH,AS,AD,AC,AH"
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

    def gameLoop(self):
        place_player = [team1[0],team2[0],team1[1],team2[1]]
        generateNewCustomDeck
        scoreTeam1 = 0
        scoreTeam2 = 0
        while (scoreTeam1 < 80) or (scoreTeam2 < 80):
            while not self.pick:
                deck = PileCard.generateNewCustomDeck(self.listCarteAuth)
                deck.shuffleDeck()
                # Distribution de carte
                for player in self.players:
                    player.drawCard(deck.drawDeck(deck.id, 3))
                for player in self.players:
                    player.drawCard(deck.drawDeck(deck.id, 2))
                # Tour d'appel
                carteAppel = deck.drawDeck(deck.id)
                for player in self.players:
                    rep = ""
                    while not (rep == "y" or rep == "Y" or rep == "n" or rep == "N"):
                        rep = input(
                            "La couleur proposée est {}, voulez vous prendre ? (Y/N) ".format(carteAppel.couleur))
                    if (rep == "y" or rep == "Y"):
                        self.atout = carteAppel.couleur
                        player.drawCard(carteAppel)
                        break
                if not self.pick:
                    for player in self.players:
                        rep = ""
                        while not (rep == "y" or rep == "Y" or rep == "n" or rep == "N"):
                            rep = input(
                                "Souhaitez vous appeler ? (Y/N) ")
                        if (rep.upper() == "Y"):
                            player.drawCard(carteAppel)
                            color = ""
                            while not (color == "S" or color == "H" or color == "C" or color == "D"):
                                color = input(
                                    "Quelle couleur souhaitez vous appeler ? (S/H/C/D) ")
                            if (rep == "S"):
                                self.atout = "SPADES"
                            elif (rep == "H"):
                                self.atout = "HEARTS"
                            elif (rep == "C"):
                                self.atout = "CLUBS"
                            else:
                                self.atout = "DIAMONDS"
                            break
                        break

            # Fin de la distribution
            for player in self.players:
                if player == self.pick:
                    player.drawCard(deck.drawDeck(deck.id, 2))
                else:
                    player.drawCard(deck.drawDeck(deck.id, 3))

            indexTour = 0
            while len(self.player[0].cards) > 0:
                score = Belote.tour(deck)
                self.playersTable = utils.listRotate(self.playersTable, 1)

                # TODO: Implémenter le comptage correct des scores
