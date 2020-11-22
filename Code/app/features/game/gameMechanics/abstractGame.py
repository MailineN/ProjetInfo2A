from abc import ABC, abstractmethod


class AbstractGame(ABC):

    def __init__(self, idGame, players=[], listCards=None, finished=False, save=False):
        """ Liste des attributs pour chaque instance fille d'Abstract Games

        Args:
            players (list, optional): Liste des joueurs associés au jeu. Defaults to [].
            listCards ([type], optional): Liste des cartes autorisées pour le jeu. Defaults to None.
            finished (bool, optional): Jeu terminé ou non. Defaults to False.
        """
        self.idGame = idGame
        self.players = list(players)
        self.finished = finished
        self.listCards = listCards
        self.save = save

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

    @abstractmethod
    def saveMiddleGame(self):
        pass

