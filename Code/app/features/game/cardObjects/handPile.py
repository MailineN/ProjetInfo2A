from app.features.game.cardObjects.deck import PileCard
from app.features.game.cardObjects.cards import Card
from app.features.DAO.pileDAO import PileDAO
from app.features.DAO.handDAO import HandDAO


class Hand(PileCard):

    def __init__(self, idGame, idHand, card_list):
        self.idGame = idGame
        self.idHand = idHand
        self.card_list = card_list

    def __str__(self):
        """ Permet de montrer les cartes de la main 
        """
        rep = "Les cartes de la main sont : \n"
        liste = ""
        for card in self.card_list:
            liste += str(card) + ", "
        return(rep+liste)

    @staticmethod
    def newHand(idGame, idUsers):
        """ Initialise une pile vide

        Args:
            idGame (int): Identifiant du jeu pour laquelle la main est crée
            idUsers (str): Username du joueur possédant la main

        """
        return HandDAO.newHand(idGame, idUsers)

    def saveHand(self):
        """ Sauvegarde de la main dans la base de donnée
        """
        HandDAO.savehandinDataBase(self)

    @staticmethod
    def getHand(idHand):
        """ Récupération de la main du joueur

        Args:
            idHand (int): identifiant de la main du joueur

        Returns:
            list_card: Liste des cartes de la main du joueur
        """
        resultats = HandDAO.getHand(idHand)
        list_card = []
        for card in resultats.split():
            list_card.append(Card.toCards(card))

        return list_card


class Pile(PileCard):

    def __init__(self, idGame, idPile, card_list=[]):
        """ Pile de cartes utilisées lors des parties de cartes

        Args:
            idGame (int): Identifiant de la partie relié à la pile
            idPile (int): Identifiant de la pile
            card_list (list, optional): Liste des cartes du plis. Defaults to [].
        """
        self.idGame = idGame
        self.idPile = idPile
        self.card_list = card_list

    def __str__(self):
        """ Permet de montrer les cartes du pli
        """
        rep = "Les cartes du plis sont : \n"
        liste = ""
        for card in self.card_list:
            liste += str(card) + ", "
        return(rep+liste)

    def poser(self, card, joueur):
        """ Pose une carte de la main du joueur dans le pli
        et le retire de sa main

        Args:
            card (Card): Carte à poser 
            joueur (str): Identifiant du joueur
        """
        joueur.handList.remove(card)
        self.card_list.append(card)

    @staticmethod
    def newPile(idGame):
        """ Initialise une pile vide

        Args:
            idGame (str): Identifiant du jeu pour laquelle la pile est crée

        """
        return PileDAO.newPile(idGame)

    def savePile(self):
        """ Permet de sauvegarder la pile dans la base de données
        """
        PileDAO.savePileinDataBase(self)
