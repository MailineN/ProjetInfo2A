from app.features.game.gameMechanics.abstractGame import AbstractGame
from app.features.game.cardObjects.deck import PileCard
from app.features.game.gameMechanics.beloteView import BeloteView
from app.features.game.cardObjects.handPile import Hand, Pile
from app.features.DAO.gameDAO import GameDAO
import random


class Belote(AbstractGame):

    def __init__(self, idGame=None, players=[], finished=False, team1=[], team2=[], scoreTeam1=0, scoreTeam2=0, save=False):
        super().__init__(
            players=players,
            finished=finished,
            idGame=idGame,
            save=save
        )
        self.team1 = team1
        self.team2 = team2
        self.scoreTeam1 = scoreTeam1
        self.scoreTeam2 = scoreTeam2

        if len(self.team1) == 0:
            (self.team1, self.team2) = Belote.CreateTeams(self.players)

        self.listCards = "7S,7D,7C,7H,8S,8D,8C,8H,9S,9D,9C,9H,0S,0D,0C,0H,JS,JD,JC,JH,QS,QD,QC,QH,KS,KD,KC,KH,AS,AD,AC,AH"

        self.point_atout = {"JACK": 20, "9": 14, "ACE": 11,
                            "10": 10, "KING": 4, "QUEEN": 3, "8": 0, "7": 0}
        self.point_noatout = {"ACE": 11, "10": 10, "KING": 4,
                              "QUEEN": 3, "JACK": 2, "9": 0, "8": 0, "7": 0}

        self.point_atoutbob = {"JACK": 20, "9": 14, "ACE": 11,
                            "10": 10, "KING": 4, "QUEEN": 3, "8": 2, "7": 1}
        self.point_noatoutbob = {"ACE": 11, "10": 10, "KING": 5,
                              "QUEEN": 4, "JACK": 3, "9": 2, "8": 1, "7": 0}
    @staticmethod
    def CreateTeams(players):
        """ Crée aléatoirement les équipes

        Args:
            players : Liste des joueurs
        """
        repartion = random.sample(players, 4)
        team1 = [repartion[0], repartion[1]]
        team2 = [repartion[2], repartion[3]]
        return (team1, team2)

    @staticmethod
    def checkPlayerNumber(players):
        """ Vérifie qu'il y a bien 4 joueurs

        Args:
            players : Liste des joueurs
        """
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
        premiereCouleur = plis.card_list[0].couleur[0]
        valeurCoupe = -1
        for card in plis.card_list:
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

    @staticmethod
    def a_lacouleur(joueur, color):
        """ Vérifie si le joueur possède la couleur demandée

        Args:
            joueur : Joueur souhaitant poser
            vcarte : carte qu'il souhaite poser
            atout (str): Atout demmandé

        Returns:
            Bool
        """
        for i in range(len(joueur.handList)):
            if joueur.handList[i].couleur[0] == color:
                return True
        return False

    @staticmethod
    def a_de_latout(joueur, atout):
        """ Vérifie si le joueur possède de l'atout

        Args:
            joueur : Joueur souhaitant poser
            atout (str): Atout demmandé

        Returns:
            Bool
        """  # fonction qui vérifie si on a de l'atout
        for i in range(len(joueur.handList)):
            if joueur.handList[i].couleur[0] == atout:
                return True
        return False

    # fonction qui vérifie si on peut monter à l'atout
    def monteratout(self, joueur, vcarte, atout):
        """ Vérifie si le joueur peut monter à l'atout

        Args:
            joueur : Joueur souhaitant poser
            vcarte : carte qu'il souhaite poser
            atout (str): Atout demmandé

        Returns:
            Bool
        """
        for i in range(len(joueur.handList)):
            if joueur.handList[i].couleur[0] == atout and (self.point_atoutbob[joueur.handList[i].valeur[0]]) > vcarte:
                return True
        return False

    @staticmethod
    def monpote(joueur, master, equipe1, equipe2):
        """ Vérifie que le maitre du plis appartient à 
        la même équipe que le joueur s'apprétant a poser

        Args:
            joueur : Joueur souhaitant poser
            master : Maitre de la partie
            equipe1 : Joueurs de l'équipe 1
            equipe2 : Joueurs de l'équipe 2
        Returns:
            Bool 
        """
        if joueur in equipe1 and master in equipe1:
            return True
        elif joueur in equipe2 and master in equipe2:
            return True
        else:
            return False

    def gameLoop(self, idGame, maitre=None, atout=None):
        """
        Déroulement d'une partie de belote 
        Condition de victoire : Avoir plus de 80 points avec son équipe 
        Initialisation : Chaque joueur commence avec 5 cartes, selon leur mains, ils peuvent appeler 
        une couleur, d'abord celle de la carte retournée puis celle de leur choix 
        Si aucune équipe appelle, le jeu est reinitialisé
        """
        while (self.scoreTeam1 < 160) or (self.scoreTeam2 < 160):
            if maitre is not None:

                tour = len(maitre.handList)
                for i in range(tour-1):
                    maitre, plis = self.tourLoop(
                        maitre, idGame, atout, self.team1, self.team2)
                    score, gagnant = self.countPoint(plis, atout)
                    if maitre in self.team1:
                        self.scoreTeam1 += score
                    else:
                        self.scoreTeam2 += score

                    save = BeloteView.displayFinTour(maitre, plis.card_list)
                    if save == 'Non' and self.save:
                        self.saveMiddleGame(
                            self.team1, self.team2, self.scoreTeam1, self.scoreTeam2, atout, maitre)
                        return None
                    if save == 'Non' and not self.save:
                        input("Vous ne pouvez pas sauvegarder une partie invitée ")
                maitre, plis = self.tourLoop(
                    maitre, idGame, atout, self.team1, self.team2)
                score, gagnant = self.countPoint(plis, atout)

                if maitre in self.team1:
                    self.scoreTeam1 += score
                    self.scoreTeam1 += 10
                    maitre = None  
                else:
                    self.scoreTeam2 += score
                    self.scoreTeam2 += 10
                    maitre = None  
                if teamPrenant == 'Team 1':
                    if self.scoreTeam1 >= 82 :
                        print("Les preneurs gagnent les points")
                    else :
                        self.scoreTeam2 += self.scoreTeam1
                        self.scoreTeam1 -= self.scoreTeam1
                elif teamPrenant == 'Team 2':
                    if self.scoreTeam1 >= 82 :
                        print("Les preneurs gagnent les points")
                    else :
                        self.scoreTeam1 += self.scoreTeam2
                        self.scoreTeam2 -= self.scoreTeam2
            else:
                place_player = [self.team1[0], self.team2[0],
                                self.team1[1], self.team2[1]]
                BeloteView.displayNewGame(self.team1, self.team2)

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
                            place_player[i], carteAppel)
                        if appel:
                            if i % 2 == 0:
                                teamPrenant = "Team 1"
                            else:
                                teamPrenant = "Team 2"
                            atout = carteAppel.couleur[0]
                            place_player[i].handList.append(carteAppel)
                            preneur = i
                            pick = True
                            break
                    if not pick:
                        for player in place_player:
                            appel = BeloteView.displayTourAppel2(
                                place_player[i])
                            if appel[0]:
                                if i % 2 == 0:
                                    self.teamPrenant = "Team 1"
                                else:
                                    self.teamPrenant = "Team 2"
                                atout = appel[1]
                                place_player[i].handList.append(carteAppel)
                                preneur = i
                                pick = True
                                break

                    if not pick:
                        BeloteView.displayRedistrib

                for i in range(len(place_player)):
                    if i == preneur:
                        place_player[i].handList += deck.drawDeck(2)
                    else:
                        place_player[i].handList += deck.drawDeck(3)
                BeloteView.displayAtoutPris(teamPrenant, atout)

                # Fin de la distribution

                # initialise un premier joueur
                maitre = place_player[0]

        # Fin de partie
        BeloteView.displayFinPartie([self.scoreTeam1, self.scoreTeam2])
        self.finished = True
        Belote.saveMiddleGame(
            self.team1, self.team2, self.scoreTeam1, self.scoreTeam2, None, None)
        return None

    def tourLoop(self, maitre, idGame, atout, team1, team2):
        idPile = Pile.newPile(int(idGame))
        plis = Pile(idGame, idPile, card_list=[])
        ordre = []
        place_player = [team1[0], team2[0], team1[1], team2[1]]
        if maitre == team1[0]:
            ordre = place_player
        elif maitre == team2[0]:
            ordre = [place_player[1], place_player[2],
                     place_player[3], place_player[0]]
        elif maitre == team1[1]:
            ordre = [place_player[2], place_player[3],
                     place_player[0], place_player[1]]
        elif maitre == team2[1]:
            print('caca')
            ordre == [team2[1], team1[0], team2[0], team1[1]]
        print(ordre)
        cartejoue = BeloteView.displayPoser(ordre[0], plis.card_list, atout)
        plis.poser(cartejoue, maitre)
        couleurask = plis.card_list[0].couleur[0]
        # On retire la carte jouée de la main du joueur
        # JOUE A L'ATOUT
        if couleurask == atout:
            cartemaitre = (self.point_atoutbob[str(plis.card_list[0].valeur[0])])
            pointsplis = (self.point_atout[str(plis.card_list[0].valeur[0])])
            for i in range(1, 4):
                print(maitre.identifiant)
                print("\n C'est à " + ordre[i].identifiant + " de jouer \n")
                card = BeloteView.displayPoser(
                    ordre[i], plis.card_list, atout)
                if Belote.a_de_latout(ordre[i], atout):
                    while card.couleur[0] != atout:
                        print("\nVous devez jouer à l'atout\n")
                        card = BeloteView.displayPoser(
                            ordre[i], plis.card_list, atout)
                    while self.monteratout(ordre[i], cartemaitre, atout) and (self.point_atoutbob[str(card.valeur[0])]) < cartemaitre:
                        print("\nVous devez monter\n")
                        card = BeloteView.displayPoser(
                            ordre[i], plis.card_list, atout)
                    if (self.point_atoutbob[str(card.valeur[0])]) > cartemaitre:
                        cartemaitre = (self.point_atoutbob[str(card.valeur[0])])
                        maitre = ordre[i]
                        plis.poser(card, ordre[i])
                        pointsplis += (
                            self.point_atout[str(card.valeur[0])])

                    else:
                        plis.poser(card, ordre[i])
                        pointsplis += (
                            self.point_atout[str(card.valeur[0])])

                else:

                    plis.poser(card, ordre[i])
                    pointsplis += (self.point_noatout[str(card.valeur[0])])

        # JOUE A UNE AUTRE COULEUR
        else:
            coupe = 0
            cartemaitre = (
                self.point_noatoutbob[str(plis.card_list[0].valeur[0])])
            pointsplis = (
                self.point_noatout[str(plis.card_list[0].valeur[0])])
            for i in range(1, 4):
                print(maitre.identifiant)
                card = BeloteView.displayPoser(
                    ordre[i], plis.card_list, atout)
                # Mon coéquipier est maître
                if Belote.monpote(ordre[i], maitre, team1, team2):
                    # Peut jouer à la couleur
                    if Belote.a_lacouleur(ordre[i], couleurask):
                        while card.couleur[0] != couleurask:
                            print("\n Il faut jouer à la couleur demandée \n ")
                            card = BeloteView.displayPoser(
                                ordre[i], plis.card_list, atout)

                        if coupe == 0 and (self.point_noatoutbob[str(card.valeur[0])]) > cartemaitre:
                            cartemaitre = (
                                self.point_noatoutbob[str(card.valeur[0])])
                            maitre = ordre[i]
                            plis.poser(card, ordre[i])
                            pointsplis += (self.point_noatout[str(card.valeur[0])])
                        else:
                            plis.poser(card, ordre[i])
                            pointsplis += (self.point_noatout[str(card.valeur[0])]) 
                                   
                    elif card.couleur[0] == atout:  # Il coupe
                        if coupe == 0:
                            coupe += 1
                            cartemaitre = (self.point_atoutbob[str(card.valeur[0])])
                            maitre = ordre[i]
                            plis.poser(card, ordre[i])
                            pointsplis += (self.point_atout[str(card.valeur[0])])
                        elif coupe != 0:
                            while Belote.monteratout(ordre[i], cartemaitre, atout) and (self.point_atoutbob[str(card.valeur[0])]) < cartemaitre:
                                print("\n Il faut surcouper\n ")
                                card = BeloteView.displayPoser(
                                    ordre[i], plis.card_list, atout)
                            if (self.point_atoutbob[str(card.valeur[0])]) > cartemaitre:
                                cartemaitre = (
                                    self.point_atoutbob[str(card.valeur[0])])
                                pointsplis += (self.point_atout[str(card.valeur[0])])
                                plis.poser(card, ordre[i])
                                maitre = ordre[i]
                            else:
                                pointsplis += (self.point_atout[str(card.valeur[0])])
                                plis.poser(card, ordre[i])    
                    else:  # N'a pas la couleur, peut pisser
                        plis.poser(card, ordre[i])
                        pointsplis += (
                            self.point_noatout[str(card.valeur[0])])

                if not Belote.monpote(ordre[i], maitre, team1, team2):  # Mon coéquipier n'est pas maître
                    # Doit jouer à la même couleur
                    if Belote.a_lacouleur(ordre[i], couleurask) and card.couleur[0] != couleurask:
                        while card.couleur[0] != couleurask:
                            print("\n Il faut jouer à la couleur demandée \n ")
                            card = BeloteView.displayPoser(
                                ordre[i], plis.card_list, atout)
                        # Devient maitre
                        if coupe == 0 and self.point_noatoutbob[str(card.valeur[0])] > cartemaitre:
                            cartemaitre = (
                                self.point_noatoutbob[str(card.valeur[0])])
                            pointsplis += (
                                self.point_noatout[str(card.valeur[0])])
                            plis.poser(card, ordre[i])
                            maitre = ordre[i]
                        else:
                            pointsplis += (
                                self.point_noatout[str(card.valeur[0])])
                            plis.poser(card, ordre[i])

                    # Doit couper
                    elif Belote.a_de_latout(ordre[i], atout) and card.couleur[0] != atout and not Belote.a_lacouleur(ordre[i], couleurask):
                        if coupe == 0:
                            while card.couleur[0] != atout:
                                print("\n Il faut couper\n ")
                                card = BeloteView.displayPoser(
                                    ordre[i], plis.card_list, atout)
                            coupe += 1
                            maitre = ordre[i]
                            cartemaitre = (
                                self.point_atoutbob[str(card.valeur[0])])
                            plis.poser(card, ordre[i])
                            pointsplis += (self.point_atout[str(card.valeur[0])])
                        elif coupe != 0:
                            while Belote.monteratout(ordre[i], cartemaitre, atout) and (self.point_atoutbob[str(card.valeur[0])]) < cartemaitre:
                                print("\n Il faut surcouper\n ")
                                card = BeloteView.displayPoser(
                                    ordre[i], plis.card_list, atout)
                            if (self.point_atoutbob[str(card.valeur[0])]) > cartemaitre:
                                cartemaitre = (
                                    self.point_atoutbob[str(card.valeur[0])])
                                maitre = ordre[i]
                                plis.poser(card, ordre[i])
                                pointsplis += (self.point_atout[str(card.valeur[0])])
                            else:
                                pointsplis += (self.point_atout[str(card.valeur[0])])
                                plis.poser(card, ordre[i])  
                    else:  # n'a pas la couleur ni de l'atout
                        pointsplis += (
                            self.point_noatout[str(card.valeur[0])])
                        plis.poser(card, ordre[i])
        Pile.savePile(plis)
        input(maitre.identifiant + " remporte le pli !")
        return maitre, plis

    def saveFinishedGame(self):
        GameDAO.saveGame(self.idGame)

    def saveScore(player, score):
        pass

    def saveMiddleGame(self, team1, team2, scoreTeam1, scoreTeam2, atout, maitre, teamPrenant):
        """ Creation des mains et sauvegarde """
        listHand = []
        for player in team1+team2:
            idHand = Hand.newHand(self.idGame, player.identifiant)
            hand = Hand(self.idGame, idHand, ' '.join(
                map(str, player.handList)))
            Hand.saveHand(hand)
            listHand.append(idHand)

        """ Sauvegarde des données jeu """
        listHandsaved = ' '.join(
            map(str, listHand))
        listPlayers = ' '.join(
            map(str, team1+team2))
        data = {"listplayers": listPlayers,
                "listedesmains": listHandsaved,
                "scoreTeam1": scoreTeam1,
                "scoreTeam2": scoreTeam2,
                "atout": atout,
                "maitre": maitre,
                "teamPrenant": self.teamPrenant,
                "finished": self.finished
                }
        GameDAO.saveMiddleGame(data, self.idGame, 'Belote')


# TODO : Modifications dans gameLoop :
# - Checker si les mains sont vide pour éviter la redistribution accidentelle
# - Mettre l'option de quitter à la fin d'un tour
# - Re inplenter les données récupérées
