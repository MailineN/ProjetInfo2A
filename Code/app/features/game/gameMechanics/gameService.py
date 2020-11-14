from app.features.DAO.gameDAO import GameDAO
from app.features.users.guest import Guest
from app.features.gameMechanics.belote import Belote

class GameService:

    def __init__(self):
        pass

    @staticmethod
    def startGame(nomJeu, idJeu, PlayerGroup):
        if nomJeu == 'Belote' : 
            return(Belote(idJeu, PlayerGroup, False))

    def saveGame(game):
        """Fonction de sauvegarde d'une partie terminée ou non dans la base de donnée

        Args:
            game : Instance de fille d'AbstractGame, déjà initialisée
        """
        GameDAO.saveGame(game)

    def saveScore(game, player, score):
        """Fonction de sauvegarde des scores d'une partie d'un joueur

        Args:
            game : Instance de fille d'AbstractGame, déjà initialisée
            player (idPlayer): Joueur souhaitant sauvegarder ses propres scores 
            score (int) 
        """
        GameDAO.saveScore(game, player, score)
        print('Sauvegarde terminée')

    @staticmethod
    def initListPlayers(jeu):
        listPlayers = []
        while not jeu.checkPlayersNumber(listPlayers):
            listPlayers = Guest.connexionJeu(listPlayers)
        return(listPlayers)

    @staticmethod
    def initEmptyGame(nomJeu):
        """initialise un jeu vide du jeu sélectionné avec une liste de joueur complete """  # comment récupérer le choix du jeu avec les menus ?
        listPlayers = GameService.initListPlayers(nomJeu)
        listString = ' '.join(map(str, listPlayers))
        # Convertit la liste de joueur [1,2,3] en string '1 2 3'
        id_Jeu = GameDAO.addGame(nomJeu, listString)
        GameService.startGame(nomJeu, id_Jeu, listPlayers)
