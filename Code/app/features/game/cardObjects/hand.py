from deck import PileCard
from card import Card
from pile import Pile

class Hand(PileCard) :

    def __init__(self, idGame, idPlayer, card_list, idHand) :

        self.idGame = idGame
        self.idPlayer = idPlayer
        super().__init__(self,idHand,card_list)

    def addCard(Card):
        card_list.append(Card)

    def __str__(self):
        rep = "Les cartes de la main sont : \n"
        liste = ""
        for card in self.card_list:
            liste += str(card) + ", "
        return(rep+liste)

    def poser(self,Card,Pile) :
        ide = Card.code
        newhand = []
        for i in range(Hand.len()) :
            card = self.card_list[i]
            if not(ide == card.code) :
                newhand.append(card)
        self.card_list = newhand
        Pile.addCard(Card)








