from app.features.game.gameMechanics.abstractGame import AbstractGame
from app.features.game.cardObjects.deck import PileCard
from app.features.game.gameMechanics.beloteView import BeloteView
from app.features.game.cardObjects.handPile import Pile
import random


class Belote(AbstractGame):

    def __init__(self, idGame=None, players=[], finished=False):
        super().__init__(
            players=players,
            finished=finished,
            idGame=idGame
        )
        self.listCards = "7S,7D,7C,7H,8S,8D,8C,8H,9S,9D,9C,9H,0S,\
            0D,0C,0H,JS,JD,JC,JH,QS,QD,QC,QH,KS,KD,KC,KH,AS,AD,AC,AH"

        self.point_atout = {"JACK": 20, "9": 14, "ACE": 11,
                            "10": 10, "KING": 4, "QUEEN": 3, "8": 0, "7": 0}
        self.point_noatout = {"ACE": 11, "10": 10, "KING": 4,
                              "QUEEN": 3, "JACK": 2, "9": 0, "8": 0, "7": 0}

    def CreateTeams(players):  # répartition aléatoire des joueurs
        repartion = random.sample(players, 4)
        team1 = [repartion[0], repartion[1]]
        team2 = [repartion[2], repartion[3]]
        return (team1, team2)

    @staticmethod
    def checkPlayerNumber(players):
        nbjoueur = len(players)
        if nbjoueur == 4:
            print("Le nombre de joueur est bon")
            return True
        else:
            print("Le nombre de joueurs n'est pas bon")
            return False

    def countPoint(self, plis, atout):
        """Fonction de comptage des points après chaque plis et détermine le gagant du pli

        Args:
            plis : Liste des cartes du pli
            atout : Couleur d'atout
        """
        count = 0
        gagnant: int
        listPoint = []  # index du gagnant dans la tourne actuelle
        coupe = False
        premiereCouleur = plis[0].couleur[0]
        valeurCoupe = -1
        for card in plis:
            if card.couleur[0] == atout:
                listPoint.append(self.point_atout[card.valeur[0]])
                if card.couleur[0] != premiereCouleur:
                    coupe = True
                    if max(self.point_atout[card.valeur[0]], valeurCoupe) > valeurCoupe:
                        valeurCoupe = max(
                            self.point_atout[card.valeur[0]], valeurCoupe)
                        gagnant = len(listPoint) - 1
            else:
                listPoint.append(self.point_noatout[card.valeur[0]])
        if not coupe:
            gagnant = listPoint.index(max(listPoint))
        count = sum(listPoint)
        return(count, gagnant)

    def a_lacouleur(joueur, color):  # fonction qui vérifie si on a de la couleur demandée
        for i in range(len(joueur.handList)):
            if joueur.handList[i].couleur[0] == color:
                return True
        return False

    def a_de_latout(joueur, atout):  # fonction qui vérifie si on a de l'atout
        for i in range(len(joueur.handList)):
            if joueur.handList[i].couleur[0] == atout:
                return True
        return False

    # fonction qui vérifie si on peut monter à l'atout
    def monteratout(self, joueur, vcarte, atout):
        for i in range(len(joueur.handList)):
            if joueur.handList[i].couleur[0] == atout and (self.point_atout[joueur.handList[i].valeur[0]]) > vcarte:
                return True
        return False

    # vérifie si deux joueurs sont dans la même équipe
    def monpote(joueur, master, equipe1, equipe2):
        if joueur in equipe1 and master in equipe1:
            return True
        elif joueur in equipe2 and master in equipe2:
            return True
        else:
            return False

    def gameLoop(self, idGame, players):
        """
        Déroulement d'une partie de belote 
        Condition de victoire : Avoir plus de 80 points avec son équipe 
        Initialisation : Chaque joueur commence avec 5 cartes, selon leur mains, ils peuvent appeler 
        une couleur, d'abord celle de la carte retournée puis celle de leur choix 
        Si aucune équipe appelle, le jeu est reinitialisé
        """
        (team1, team2) = Belote.CreateTeams(players)
        place_player = [team1[0], team2[0], team1[1], team2[1]]
        scoreTeam1 = 0
        scoreTeam2 = 0
        BeloteView.displayNewGame(team1, team2)
        while (scoreTeam1 < 80) or (scoreTeam2 < 80):
            pick = False
            atout = None
            teamPrenant = None
            while not pick:
                deck = PileCard.generateNewCustomDeck(self.listCards)
                deck.shuffleDeck()
                # Distribution de carte
                for player in place_player:
                    player.handList = deck.drawDeck(3)
                for player in place_player:
                    player.handList += deck.drawDeck(2)
                # Tour d'appel
                carteAppel = deck.drawDeck(1)[0]
                appel = False
                for i in range(len(place_player)):
                    appel = BeloteView.displayTourAppel(
                        place_player[i].handList, carteAppel)
                    if appel:
                        if i % 2 == 0:
                            teamPrenant = "Team 1"
                        else:
                            teamPrenant = "Team 2"
                        atout = carteAppel.couleur[0]
                        place_player[i].handList.append(carteAppel)
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
                            place_player[i].handList.append(carteAppel)
                            pick = True
                            break
                if not pick:
                    BeloteView.displayRedistrib

            BeloteView.displayAtoutPris(teamPrenant, atout)

            # Fin de la distribution

            # initialise un premier joueur
            maitre = place_player[0]
            for i in range(7):
                maitre, plis = Belote.tourLoop(Belote(),maitre, idGame, atout, team1, team2)
                score, gagnant = Belote.countPoint(plis, atout)
                if maitre in team1:
                    scoreTeam1 += score
                else:
                    scoreTeam2 += score
                BeloteView.displayFinTour(maitre, plis.card_list)

            maitre, plis = Belote.tourLoop(Belote(),maitre, idGame, atout, team1, team2)
            score, gagnant = Belote.countPoint(plis, atout)

            if maitre in team1:
                scoreTeam1 += score
                scoreTeam1 += 10
            else:
                scoreTeam2 += score
                scoreTeam2 += 10

        # Fin de partie
        BeloteView.displayFinPartie([scoreTeam1, scoreTeam2])
        sauvegarde = BeloteView.displaySauvegarderJeu(self.players)
        for i in range(4):
            if sauvegarde[i]:
                if self.players[i] in team1:
                    score = scoreTeam1
                else:
                    score = scoreTeam2
                Belote.save(player, score)
        return None

    def tourLoop(self, maitre, idGame, atout, team1, team2):
        idPile = Pile.newPile(idGame)
        plis = Pile(idGame, idPile, card_list=[])
        ordre = []
        place_player = [team1[0], team2[0], team1[1], team2[1]]
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
        cartejoue = BeloteView.displayPoser(ordre[0].handList)
        plis.poser(cartejoue,maitre)
        couleurask = plis.card_list[0].couleur[0]
        # On retire la carte jouée de la main du joueur
        # JOUE A L'ATOUT
        if couleurask == atout:
            cartemaitre = (self.point_atout[str(plis.card_list[0].valeur[0])])
            pointsplis = cartemaitre
            for i in range(1, 4):
                card = BeloteView.displayPoser(ordre[i].handList)
                if Belote.a_de_latout(ordre[i], atout):
                    while Belote.monteratout(Belote(), ordre[i], cartemaitre, atout) and (self.point_atout[str(card.valeur[0])]) < cartemaitre:
                        print("Vous devez monter")
                        card = BeloteView.displayPoser(ordre[i].handList)
                    if (self.point_atout[str(card.valeur[0])]) > cartemaitre:
                        cartemaitre = (self.point_atout[str(card.valeur[0])])
                        maitre = ordre[i]
                        plis.poser(card, ordre[i])
                        pointsplis += (
                            self.point_atout[str(card.valeur[0])])
                    else :
                        plis.poser(card, ordre[i])
                        pointsplis += (
                            self.point_atout[str(card.valeur[0])])
                else:
                    
                    plis.poser(card, ordre[i])
                    pointsplis += (self.point_noatout[str(card.valeur[0])])

        # JOUE A UNE AUTRE COULEUR
        else:
            coupe = 0
            cartemaitre = (self.point_noatout[str(plis.card_list[0].valeur[0])])
            pointsplis = cartemaitre
            for i in range(1, 4):
                card = None
                # Mon coéquipier est maître
                if Belote.monpote(ordre[i], maitre, team1, team2):
                    # Peut jouer à la couleur
                    if Belote.a_lacouleur(ordre[i], couleurask):
                        while card.couleur != couleurask:
                            print("Il faut jouer à la couleur demandée")
                            card = BeloteView.displayPoser(ordre[i].handList)

                        plis.poser(card, ordre[i])
                        pointsplis += (
                            self.point_noatout[str(card.valeur[0])])
                        if coupe == 0 and (self.point_noatout[str(card.valeur[0])]) > cartemaitre:
                            cartemaitre = (
                                self.point_noatout[str(card.valeur[0])])
                            maitre = ordre[i]
                    elif card.couleur == atout:  # Il coupe
                        coupe += 1
                        cartemaitre = (self.point_atout[str(card.valeur[0])])
                        maitre = ordre[i]
                        plis.poser(card, ordre[i])
                        pointsplis += cartemaitre

                    else:  # N'a pas la couleur, peut pisser
                        plis.poser(card, ordre[i])
                        pointsplis += (
                            self.point_noatout[str(card.valeur[0])])

                else:  # Mon coéquipier n'est pas maître
                    # Doit jouer à la même couleur
                    if Belote.a_lacouleur(ordre[i], couleurask) and card.couleur[0] != couleurask:
                        while card.couleur[0] != couleurask:
                            print("Il faut jouer à la couleur demandée")
                            card = BeloteView.displayPoser(ordre[i].handList)
                        # Devient maitre
                        if (self.point_noatout[str(card.valeur[0])]) > cartemaitre and coupe == 0:
                            plis.poser(card, ordre[i])
                            cartemaitre = (
                                self.point_noatout[str(card.valeur[0])])
                            maitre = ordre[i]
                            pointsplis += (
                                self.point_noatout[str(card.valeur[0])])

                        else:
                            pointsplis += (
                                self.point_noatout[str(card.valeur[0])])

                            plis.poser(card, ordre[i])
                    # Doit couper
                    elif Belote.a_de_latout(ordre[i], atout) and card.couleur[0] != atout:
                        if coupe == 0:
                            while card.couleur[0] != atout:
                                print("Il faut couper")
                                card = BeloteView.displayPoser(
                                    ordre[i].handList)
                            coupe += 1
                            maitre = ordre[i]
                            cartemaitre = (
                                self.point_atout[str(card.valeur[0])])
                            plis.poser(card, ordre[i])

                        elif coupe != 0:
                            while Belote.monteratout(ordre[i], cartemaitre, atout) and (self.point_atout[str(card.valeur[0])]) < cartemaitre:
                                print("Il faut surcouper")
                                card = BeloteView.displayPoser(
                                    ordre[i].handList)
                            if (self.point_atout[str(card.valeur[0])]) > cartemaitre:
                                cartemaitre = (
                                    self.point_atout[str(card.valeur[0])])

                                plis.poser(card, ordre[i])

                    else:  # n'a pas la couleur ni de l'atout
                        pointsplis += (
                            self.point_noatout[str(card.valeur[0])])
                        plis.poser(card, ordre[i])
        return maitre, plis

    def saveFinishedGame():
        GameDAO.saveGame(game)

    def saveScore(player, score):
        pass
