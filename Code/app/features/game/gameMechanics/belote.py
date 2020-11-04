from abstractgame import AbstractGame
from cardObjects.deck import PileCard
from .beloteView import *


class Belote(AbstractGame):

    def __init__(self, players=[], finished=false):
        super.__init__(
            players=list(players),
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
        """Fonction de comptage des points après chaque plis et détermine le gagant du pli

        Args:
            plis : Liste des cartes du pli
            atout : Couleur d'atout
        """
        count = 0
        gagnant: int
        listPoint = []  # index du gagnant dans la tourne actuelle
        coupe = False
        premiereCouleur = plis[0].couleur
        valeurCoupe = -1
        for card in plis:
            if card.couleur == atout:
                listPoint.append(point_atout[card.valeur])
                if card.couleur != premiereCouleur:
                    coupe = True
                    if max(point_atout[card.valeur], valeurCoupe) > valeurCoupe:
                        valeurCoupe = max(
                            point_atout[card.valeur], valeurCoupe)
                        gagnant = len(listPoint) - 1
            else:
                listPoint.append(point_noatout[card.valeur])
        if not coupe:
            gagnant = listPoint.index(max(listPoint))
        count = sum(listPoint)
        return(count, gagnant)

    def gameLoop(self):
        """
        Déroulement d'une partie de belote 
        Condition de victoire : Avoir plus de 80 points avec son équipe 
        Initialisation : Chaque joueur commence avec 5 cartes, selon leur mains, ils peuvent appeler 
        une couleur, d'abord celle de la carte retournée puis celle de leur choix 
        Si aucune équipe appelle, le jeu est reinitialisé
        """
        (team1, team2) = CreateTeams()
        place_player = [team1[0], team2[0], team1[1], team2[1]]
        scoreTeam1 = 0
        scoreTeam2 = 0
        BeloteView.displayNewGame(team1, team2)
        while (scoreTeam1 < 80) or (scoreTeam2 < 80):
            pick = False
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
                            atout = appel[1]
                            place_player[i].drawCard(carteAppel)
                            pick = True
                        break
                    break
                if not pick:
                    BeloteView.displayRedistrib

        BeloteView.displayAtoutPris(teamPrenant, atout)

        # Fin de la distribution

    def tourLoop(self):
        plis = []
        ordre = []
        maitre =
        if maitre == place_player[0]:
            ordre = place_player
        elif maitre == place_player[1]:
            ordre = [place_player[1], place_player[2],
                     place_player[3], place_player[0]]
        elif maitre == place_player[2]:
            ordre = [place_player[2], place_player[3],
                     place_player[0], place_player[1]]
        elif maitre == place_player[3]:
            ordre == [place_player[3], place_player[0],
                      place_player[1], place_player[2]]
        plis.append(ordre[0].poser(carte))
        couleurask = plis[0].couleur

        # JOUE A L'ATOUT
        if couleurask == atout:
            cartemaitre = float(point_atout["plis[0].valeur"])
            pointsplis = cartemaitre
            for i in range(1, 4):
                card = ordre[i].poser(carte)
                if a_de_latout(ordre[i]):
                    while monteratout(ordre[i], cartemaitre) == True and float(point_atout["card.valeur"]) < cartemaitre:
                        print("Vous devez monter")
                        card = ordre[i].poser(carte)
                    if float(point_atout["card.valeur"]) > cartemaitre:
                        cartemaitre = float(point_atout["card.valeur"])
                        maitre = ordre[i]
                        plis.append(card)
                        pointsplis += float(point_noatout["card.valeur"])
                else:
                    plis.append(card)
                    pointsplis += float(point_noatout["card.valeur"])

        # JOUE A UNE AUTRE COULEUR
        else:
            cartemaitre = float(point_noatout["plis[0].valeur"])
            pointsplis = cartemaitre
            for i in range(1, 4):
                card = ordre[i].poser(carte)
                if monpote(ordre[i], maitre):  # Mon coéquipier est maître
                    if card.couleur == atout:
                        cartemaitre = float(point_atout["card.valeur"])
                        maitre = ordre[i]
                        plis.append(card)
                        pointsplis += cartemaitre
                    elif card.couleur != couleurask and card.couleur != atout:
                        plis.append(card)
                        pointsplis += float(point_noatout["card.valeur"])
                    elif card.couleur == couleurask:
                        plis.append(card)
                        pointsplis += float(point_noatout["card.valeur"])
                        if float(point_noatout["card.valeur"]) > cartemaitre:
                            cartemaitre = float(point_noatout["card.valeur"])
                            maitre = ordre[i]
                else:  # Mon coéquipier n'est pas maître
                    while a_lacouleur(ordre[i]) == True and card.couleur != couleurask:
                        print("Il faut jouer à la couleur demandée")
                        card = ordre[i].poser(carte)

                    elif a_de_latout(ordre[i]) == True and card.couleur != atout:
                        print("Il faut couper")
                        card = ordre[i].poser(carte)

    def a_lacouleur(joueur):  # fonction qui vérifie si on a de la couleur demandée
        for i in range(len(joueur.handList)):
            if joueur.handList[i].couleur == couleurask:
                return True
        return(False)

    def a_de_latout(joueur):  # fonction qui vérifie si on a de l'atout
        for i in range(len(joueur.handList)):
            if joueur.handList[i].couleur == atout:
                return True

    def monteratout(joueur, vcarte):  # fonction qui vérifie si on peut monter à l'atout
        valeur = 0
        for i in range(len(joueur.handList)):
            if joueur.handList[i].couleur == atout and float(point_atout[joueur.handList[i].valeur]) > vcart:
                return True

    def monpote(joueur, master):  # vérifie si deux joueurs sont dans la même équipe
        if joueur in team1 and master in team1:
            return True
        elif joueur in team2 and master in team2:
            return True
        else:
            return False
