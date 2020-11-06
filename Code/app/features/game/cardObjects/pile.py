from app.features.DAO.pile_dao import PileDAO
from app.features.game.cardObjects.deck import PileCard


class Pile(PileCard):
    def __init__(self, idGame, idPile, card_list=[]):
        self.idGame = idGame
        self.idPile = idPile
        self.card_list = card_list

    def addcard(self, card):
        self.card_list.append(card)

    def __str__(self):
        rep = "Les cartes du plis sont : \n"
        liste = ""
        for card in self.card_list:
            liste += str(card) + ", "
        return(rep+liste)
