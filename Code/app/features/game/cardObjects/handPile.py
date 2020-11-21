from app.features.game.cardObjects.deck import PileCard
from app.features.game.cardObjects.cards import Card
from app.features.DAO.pileDAO import PileDAO
from app.features.DAO.handDAO import HandDAO


class Hand(PileCard):

    def __init__(self, idGame, idHand, card_list=[]):
        self.idGame = idGame
        self.idPile = idHand
        self.card_list = card_list

    def __str__(self):
        """ Permet de montrer les cartes de la main 
        """
        rep = "Les cartes de la main sont : \n"
        liste = ""
        for card in self.card_list:
            liste += str(card) + ", "
        return(rep+liste)

    def newHand(idGame):
        """ Initialise une pile vide

        Args:
            idGame (str): Identifiant du jeu pour laquelle la pile est crée

        """
        return HandDAO.newHand(idGame)

    def saveHand(hand):
        HandDAO.saveHandinDataBase(hand)

    @staticmethod
    def getHand(idGame, idPlayer):
        resultats = HandDAO.getHand(idPlayer, idGame)
        list_card = []
        for card in resultats.split():
            list_card.append(Card.toCards(card))

        return list_card


class Pile(PileCard):
    """ Pile de cartes utilisées lors des parties de cartes

    Args:
        PileCard (PileCard): Classe mère possédant les actions principales sur le deck
    """

    def __init__(self, idGame, idPile, card_list=[]):
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

    def newPile(idGame):
        """ Initialise une pile vide

        Args:
            idGame (str): Identifiant du jeu pour laquelle la pile est crée

        """
        return PileDAO.newPile(idGame)

    def savePile(pile):
        PileDAO.savePileinDataBase(pile)
