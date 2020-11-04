from handDAO import HandDAO
from pileDAO import PileDAO
from GameService import GameService
import psycopg2
from DAO.databaseConnection import DatabaseConnection

class GameDAO :

    def saveGame(gameService) :

        for pile in gameService.PileList :
            savePileinDataBase(pile)
        for hand in gameService.HandList :
            saveHandinDatabase(hand)
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.curseur()
        try:
            curseur.execute(
                "INSERT INTO score VALUES %s"
                (gameService.score)
            )
            score.id = curseur.fetchone()[0]
            connexion.commit()
        except psycopg2.Error as error:
            connexion.rollback()
            raise error
        finally:
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)
    
    def fetchCurrentGame() :

        pass

    def fetchSaveGame(gameIDE) :

        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.curseur()
        try:
            curseur.execute(
                "SELECT * FROM hand WHERE hand.id = gameIDE"
            )
            Hand = curseur.fetchone()[1]
            curseur.execute(
                "SELECT * FROM pile WHERE pile.id = gameIDE"
            )
            Pile = curseur.fetchone()[1]
            curseur.execute(
                "SELECT * FROM score WHERE score.id = gameIDE"
            )
            Score = curseur.fetchone()[1]      
        finally:
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)
        return(Hand,Pile,Score)




        
        



    



