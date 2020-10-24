import uuid # Will be used to generate deck id in the database
from card import Card
from app.features.game.apiInteractions.cardAPI import cardAPI


class PileCard:
    def __init__(self, idend=None, cards=list[Card]) -> None:
        # cards représente une liste de cartes et id correspond à l'id de l'api
        self.id = idend
        self.cards = cards

    @staticmethod
    def generateNewDeck():
        return PileCard(cardAPI.newDeck())

    @staticmethod
    def generateNewCustomDeck(listofcard: str):
        return PileCard(cardAPI.newCustomDeck(listofcard))

    def len(self) -> int:
        return(len(self.cards))

    def topCard(self) -> Card:
        return self.cards[0]

    def shuffleDeck(self) -> None:
        self.id = cardAPI.shuffleDeck(self.id)

    def drawDeck(self, count) -> list[Card]:
        result = cardAPI.drawDeck(self.id, count)
        self.id = result[1]
        return(result[0])


"""     def shufflePile(self):
        pass
    def drawPile(self):
        pass
    
    def addToPile(self, gameId,cards): 
        cardAPI.addToPile(self.id,gameId,cards) """

# Todo : Implement custom pile drawing and shuffling