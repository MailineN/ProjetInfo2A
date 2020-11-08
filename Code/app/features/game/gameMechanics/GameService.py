from gameMechancis import *
from app.features.DAO import GameDAO


class GameService:

    def initGame(Game, PlayerGroup):

        return(Game(PlayerGroup))

    def saveGame(game):
        """Fonction de sauvegarde d'une partie terminée ou non dans la base de donnée

        Args:
            game : Instance de fille d'AbstractGame, déjà initialisée
        """
        GameDAO.saveGame(Game)

    def saveScore(game, player, score):
        """Fonction de sauvegarde des scores d'une partie d'un joueur

        Args:
            game : Instance de fille d'AbstractGame, déjà initialisée
            player (idPlayer): Joueur souhaitant sauvegarder ses propres scores 
            score (int) 
        """
        GameDAO.saveScore(game, player, score)
        print('Sauvegarde terminée')
