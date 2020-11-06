""" Objet gérant les différents paquets de cartes du jeu
"""
from app.features.game.cardObjects.cards import Card
from app.features.game.apiInteractions.cardAPI import cardAPI


class PileCard:
    def __init__(self, cards=[], idend=None) -> None:
        """[summary]

        Args:
            idend ([type], optional): Identifiant utilisé pour appeler l'API en cas d'utilisation multiples. Defaults to None.
            cards ([type], optional): Liste de cartes du deck. Defaults to list[Card].
        """
        self.id = idend
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

    def len(self) -> int:
        return(len(self.cards))

    def topCard(self) -> Card:
        """ Montre la première carte du paquet
        """
        return self.cards[0]

    def shuffleDeck(self) -> None:
        """ Mélange le paquet grace à l'API
        """
        self.id = cardAPI.shuffleDeck(self.id)

    def drawDeck(self, count):
        """ Prend le nombre spécifié de cartes du paquet, les retire et les renvoient
        """
        (cards, iden) = cardAPI.drawDeck(self.id, count)
        listCard = []
        for i in len(cards):
            card = Card(cards[i]["value"], cards[i]["suits"], cards[i]["code"])
            listCard.append(card)
        self.id = iden
        return(listCard)
