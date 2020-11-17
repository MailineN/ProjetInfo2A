""" Objet gérant les différents paquets de cartes du jeu
"""
from app.features.game.cardObjects.cards import Card
from app.features.game.apiInteractions.cardAPI import cardAPI


class PileCard:
    def __init__(self, cards=[], idend=None) -> None:
        """ Base servant à la création des piles de cartes utilisées pour les piles et les decks

        Args:
            idend (str, optional): Identifiant utilisé pour appeler l'API en cas d'utilisation multiples. Defaults to None.
            cards (list[Card], optional): Liste de cartes du deck. Defaults to list[Card].
        """
        self.idend = idend
        self.cards = cards

    @staticmethod
    def generateNewDeck():
        """ Création d'un nouveau deck grace à l'API
        """
        return PileCard(cards=[], idend=cardAPI.newDeck())

    @staticmethod
    def generateNewCustomDeck(listofcard):
        """ Création d'un nouveau deck grace à l'API
            Ici avec les cartes adaptées selon le jeu
        """
        return PileCard(cards=[], idend=cardAPI.newCustomDeck(listofcard))

    def len(self):
        return(len(self.cards))

    def topCard(self):
        """ Montre la première carte du paquet
        """
        return self.cards[0]

    def shuffleDeck(self):
        """ Mélange le paquet grace à l'API
        """
        self.idend = cardAPI.shuffleDeck(self.idend)
    
    def drawDeck(self, count=1):
        """ Prend le nombre spécifié de cartes du paquet, les retire et les renvoient
        """
        (cards, iden) = cardAPI.drawDeck(self.idend, count)
        listCard = []
        for i in range(len(cards)):
            card = Card(cards[i]["value"], cards[i]["suit"], cards[i]["code"])
            listCard.append(card)
        self.idend = iden
        return(listCard)
