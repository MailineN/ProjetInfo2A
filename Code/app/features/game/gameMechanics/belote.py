from app.features.game.gameMechanics.abstractGame import AbstractGame
from app.features.game.cardObjects.deck import PileCard
from app.features.game.gameMechanics.beloteView import BeloteView
from app.features.game.cardObjects.handPile import Hand, Pile  


class Belote(AbstractGame):

    def __init__(self, players=[], finished=False, idGame):
        super().__init__(
            players=players,
            finished=finished,
            listCards="7S,7D,7C,7H,8S,8D,8C,8H,9S,9D,9C,9H,0S,\
            0D,0C,0H,JS,JD,JC,JH,QS,QD,QC,QH,KS,KD,KC,KH,AS,AD,AC,AH",
            idGame = idGame
        )
        self.point_atout = {"JACK": 20, "9": 14, "ACE": 11,
                            "10": 10, "KING": 4, "QUEEN": 3, "8": 0, "7": 0}
        self.point_noatout = {"ACE": 11, "10": 10, "KING": 4,
                              "QUEEN": 3, "JACK": 2, "9": 0, "8": 0, "7": 0}
        
    def CreateTeams(players): #modif a faire random teams
        team1 = []
        team2 = []
        print("Nous allons former les équipes")
        team1.append(input("Equipe 1 : Joueur 1 :"))
        team1.append(input("Equipe 1 : Joueur 2 :"))
        team2.append(input("Equipe 2 : Joueur 1 :"))
        team2.append(input("Equipe 2 : Joueur 2 :"))
        return (team1, team2)

    def checkPlayerNumber(players):
        try:
            nbjoueur = len(players)
            if nbjoueur == 4:
                print("Le nombre de joueur est bon")

        except nbjoueur != 4:
            print("Le nombre de joueurs n'est pas bon")

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
        premiereCouleur = plis[0].couleur
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
            if joueur.handList[i].couleur == color:
                return True
        return False

    def a_de_latout(joueur, atout):  # fonction qui vérifie si on a de l'atout
        for i in range(len(joueur.handList)):
            if joueur.handList[i].couleur == atout:
                return True
        return False

    def monteratout(self, joueur, vcarte, atout):  # fonction qui vérifie si on peut monter à l'atout
        for i in range(len(joueur.handList)):
            if joueur.handList[i].couleur == atout and float(self.point_atout[joueur.handList[i].valeur]) > vcarte:
                return True
        return False

    def monpote(joueur, master, equipe1, equipe2):  # vérifie si deux joueurs sont dans la même équipe
        if joueur in equipe1 and master in equipe1:
            return True
        elif joueur in equipe2 and master in equipe2:
            return True
        else:
            return False

    def gameLoop(self, idGame):
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

        # initialise un premier joueur
        maitre = place_player[0]
        for i in range(8):
            tourLoop(self, maitre, idGame, atout, team1, team2)

    def tourLoop(self, maitre, idGame, atout, team1, team2):
        idPile = Pile.newPile(idGame)
        plis = Pile.pile(idGame,idPile, card_list = [])
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
        cartejoue = ordre[0].poser.card_list(plis).card_list[0] # hand_list.poser prend en argument pile
        couleurask = plis[0].couleur
        # On retire la carte jouée de la main du joueur
        # JOUE A L'ATOUT
        if couleurask == atout:
            cartemaitre = float(self.point_atout[str(plis[0].valeur)])
            pointsplis = cartemaitre
            for i in range(1, 4):
                card = ordre[i].handList.poser(idPile)
                if a_de_latout(ordre[i]):
                    while monteratout(ordre[i], cartemaitre, atout) and float(self.point_atout[str(card.valeur)]) < cartemaitre:
                        print("Vous devez monter")
                        card = ordre[i].handList.poser(idPile)
                    if float(self.point_atout[str(card.valeur)]) > cartemaitre:
                        cartemaitre = float(self.point_atout[str(card.valeur)])
                        maitre = ordre[i]
                        plis.append(card)
                        pointsplis += float(
                            self.point_noatout[str(card.valeur)])

                else:
                    plis.append(card)
                    pointsplis += float(self.point_noatout[str(card.valeur)])

        # JOUE A UNE AUTRE COULEUR
        else:
            coupe = 0
            cartemaitre = float(self.point_noatout[str(plis[0].valeur)])
            pointsplis = cartemaitre
            for i in range(1, 4):
                card = ordre[i].handList.poser(idPile)
                if monpote(ordre[i], maitre,team1,team2):  # Mon coéquipier est maître
                    if a_lacouleur(ordre[i], couleurask):  # Peut jouer à la couleur
                        while card.couleur != couleurask:
                            print("Il faut jouer à la couleur demandée")
                            card = ordre[i].handList.poser(idPile)

                        plis.append(card)
                        pointsplis += float(
                            self.point_noatout[str(card.valeur)])
                        if coupe == 0 and float(self.point_noatout[str(card.valeur)]) > cartemaitre:
                            cartemaitre = float(
                                self.point_noatout[str(card.valeur)])
                            maitre = ordre[i]
                    elif card.couleur == atout:  # Il coupe
                        coupe += 1
                        cartemaitre = float(self.point_atout[str(card.valeur)])
                        maitre = ordre[i]
                        plis.append(card)
                        pointsplis += cartemaitre

                    elif card.couleur != couleurask and card.couleur != atout:  # N'a pas la couleur, peut pisser
                        plis.append(card)
                        pointsplis += float(
                            self.point_noatout[str(card.valeur)])

                else:  # Mon coéquipier n'est pas maître
                    # Doit jouer à la même couleur
                    if a_lacouleur(ordre[i], couleurask) and card.couleur != couleurask:
                        while card.couleur != couleurask:
                            print("Il faut jouer à la couleur demandée")
                            card = ordre[i].handList.poser(idPile)
                        # Devient maitre
                        if float(self.point_noatout[str(card.valeur)]) > cartemaitre and coupe == 0:
                            cartemaitre = float(
                                self.point_noatout[str(card.valeur)])
                            maitre = ordre[i]
                            pointsplis += float(
                                self.point_noatout[str(card.valeur)])

                            plis.append(card)
                        else:
                            pointsplis += float(
                                self.point_noatout[str(card.valeur)])

                            plis.append(card)
                    # Doit couper
                    elif a_de_latout(ordre[i], atout) and card.couleur != couleurask and card.couleur != atout:
                        if coupe == 0:
                            while card.couleur != atout:
                                print("Il faut couper")
                                card = ordre[i].handList.poser(idPile)
                            coupe += 1
                            maitre = ordre[i]
                            cartemaitre = float(
                                self.point_atout[str(card.valeur)])
                            plis.append(card)

                        elif coupe != 0:
                            while monteratout(ordre[i], cartemaitre, atout) and float(self.point_atout[str(card.valeur)]) < cartemaitre:
                                print("Il faut surcouper")
                                card = ordre[i].handList.poser(idPile)
                            if float(self.point_atout[str(card.valeur)]) > cartemaitre:
                                cartemaitre = float(
                                    self.point_atout[str(card.valeur)])

                                plis.append(card)
                                coupe.append(
                                    float(self.point_atout[str(card.valeur)]))
                    else:  # n'a pas la couleur ni de l'atout
                        pointsplis += float(
                            self.point_noatout[str(card.valeur)])

                        plis.append(card)
        return maitre


