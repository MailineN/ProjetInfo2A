from pile_dao import PileDAO
from cardobjects.deck import * 

class Pile():
    def __init__(self, idGame, idPile, card_list=[])
        self.idGame = idGame
        self.idPile = idPile
        self.card_list = card_list
    
 
    def addCard(Card,idPile,idGame):
        card_list.append(Card)