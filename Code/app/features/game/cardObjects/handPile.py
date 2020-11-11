from app.features.game.cardObjects.deck import PileCard
from app.features.game.cardObjects.cards import Card


class Hand(PileCard):

    def __init__(self, idHand, idGame, idPlayer, card_list):
        super().__init__(cards=card_list, idend=idHand)
        self.idGame = idGame
        self.idPlayer = idPlayer

    def addCard(self, card):
        self.card_list.append(card)

    def __str__(self):
        rep = "Les cartes de la main sont : "
        liste = ""
        for card in self.cards:
            liste += str(card) + ", "
        return(rep+liste)

    def poser(self, card, pile):
        ide = card.code
        newhand = []
        for i in range(Hand.len()):
            card = self.card_list[i]
            if not(ide == card.code):
                newhand.append(card)
        self.card_list = newhand
        pile.addCard(Card)


class Pile(PileCard):
    def __init__(self, idGame, idPile, card_list=[]):
        self.idGame = idGame
        self.idPile = idPile
        self.card_list = card_list

    def __str__(self):
        rep = "Les cartes du plis sont : \n"
        liste = ""
        for card in self.card_list:
            liste += str(card) + ", "
        return(rep+liste)

    def poser(self, card, joueur):
        joueur.handList.remove(card)
        self.card_list.append(card)

