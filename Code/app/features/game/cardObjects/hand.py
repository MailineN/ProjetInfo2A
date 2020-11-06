from app.features.game.cardObjects.deck import PileCard
from app.features.game.cardObjects.cards import Card
from app.features.game.cardObjects.pile import Pile

class Hand(PileCard) :

    def __init__(self, idHand, idGame, idPlayer, card_list) :
        super().__init__(cards = card_list,idend = idHand)
        self.idGame = idGame
        self.idPlayer = idPlayer
        

    def addCard(self,card):
        self.card_list.append(card)

    def __str__(self):
        rep = "Les cartes de la main sont : "
        liste = ""
        for card in self.cards:
            liste += str(card) + ", "
        return(rep+liste)

    def poser(self,card,pile) :
        ide = card.code
        newhand = []
        for i in range(Hand.len()) :
            card = self.card_list[i]
            if not(ide == card.code) :
                newhand.append(card)
        self.card_list = newhand
        pile.addCard(Card)








