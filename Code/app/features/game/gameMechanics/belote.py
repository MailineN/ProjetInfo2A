from abstractgame import AbstractGame
from cardObjects.deck import PileCard
from .beloteView import *


class Belote(AbstractGame):

    def __init__(self, players=[], deck=None, victoryCondition=None, tourCondition=None, finished=false):
        super.__init__(
            players=list(players),
            deck=deck,
            victoryCondition=victoryCondition,
            tourCondition=tourCondition,
            finished=finished,
            listCards="7S,7D,7C,7H,8S,8D,8C,8H,9S,9D,9C,9H,0S,\
            0D,0C,0H,JS,JD,JC,JH,QS,QD,QC,QH,KS,KD,KC,KH,AS,AD,AC,AH"
        )

    def toorLoop(self):
        pass

    def CreateTeams():
        team1 = []
        team2 = []
        print("Nous allons former les équipes")
        team1.append(input("Equipe 1 : Joueur 1 :"))
        team1.append(input("Equipe 1 : Joueur 2 :"))
        team2.append(input("Equipe 2 : Joueur 1 :"))
        team2.append(input("Equipe 2 : Joueur 2 :"))
        return (team1, team2)

    def CheckPlayerNumber(players):
        try:
            nbjoueur = len(players)
            if nbjoueur == 4:
                print("Le nombre de joueur est bon")

        except:
            print("Le nombre de joueurs n'est pas bon")

    point_atout = {"JACK": 20, "9": 14, "ACE": 11,
                   "10": 10, "KING": 4, "QUEEN": 3, "8": 0, "7": 0}
    point_noatout = {"ACE": 11, "10": 10, "KING": 4,
                     "QUEEN": 3, "JACK": 2, "9": 0, "8": 0, "7": 0}

    def countPoint(plis, atout):
        count = 0
        gagnant: int
        listPoint = []  # index du gagnant dans la tourne actuelle
        coupe = False
        premiereCouleur = plis[0].couleur
        for card in plis:
            if card.couleur == atout:
                listPoint.append(point_atout[card.valeur])
                if card.couleur != premiereCouleur:
                    coupe = True
                    gagnant = len(listPoint)-1
                    # TODO: gérér le cas de plusieurs coupes
            else:
                listPoint.append(point_noatout[card.valeur])
        if not coupe:
            gagnant = listPoint.index(max(listPoint))
        count = sum(listPoint)
        return(count, gagnant)

    def gameLoop(self):
        (team1, team2) = CreateTeams()
        place_player = [team1[0], team2[0], team1[1], team2[1]]
        scoreTeam1 = 0
        scoreTeam2 = 0
        BeloteView.displayNewGame(team1, team2)
        while (scoreTeam1 < 80) or (scoreTeam2 < 80):
            pick = false
            atout = None
            teamPrenant = None
            while not pick:
                deck = PileCard.generateNewCustomDeck(self.listCarteAuth)
                deck.shuffleDeck()
                # Distribution de carte
                for player in place_player:
                    player.drawCard(deck.drawDeck(deck.id, 3))
                for player in place_player:
                    player.drawCard(deck.drawDeck(deck.id, 2))
                # Tour d'appel
                carteAppel = deck.drawDeck(deck.id)
                for i in range(len(place_player)):
                    appel = BeloteView.displayTourAppel(
                        place_player[i].handList, carteAppel)
                    if appel:
                        if i % 2 == 0:
                            teamPrenant = "Team 1"
                        else:
                            teamPrenant = "Team 2"
                        atout = carteAppel.couleur
                        place_player[i].drawCard(carteAppel)
                        pick = True
                    break
                if not pick:
                    for player in self.players:
                        appel = BeloteView.displayTourAppel2(
                            place_player[i].handList)
                        if appel[0]:
                            if i % 2 == 0:
                                teamPrenant = "Team 1"
                            else:
                                teamPrenant = "Team 2"
                            joueurPrenant = player
                            atout = appel[1]
                            place_player[i].drawCard(carteAppel)
                            pick = True
                        break
                    break
                if not pick:
                    BeloteView.displayRedistrib

        BeloteView.displayAtoutPris(teamPrenant, atout)

        # Fin de la distribution
