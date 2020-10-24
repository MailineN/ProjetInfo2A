from abc import ABC, abstractmethod


class AbstractGame(metaclass=ABC):

    def __init__(self, players=[], deck=None,victoryCondition = None, tourCondition = None, finished = false,listCards = []):
        self.players = list(players)
        self.deck = deck
        self.victoryCondition = victoryCondition, 
        self.tourCondition= tourCondition, 
        self.finished = finished
        self.listCards = listCards
        


    @abstractmethod
    def checkPlayerNumber(self): 
        pass
    
    @abstractmethod
    def gameLoop(self):
        """ A implémenter en fonction du jeu demandé"""
        pass
    
    @abstractmethod
    def tourLoop(self):
        """ A implémenter en fonction du jeu demandé"""
        pass