from app.features.DAO.handDAO import HandDAO
from app.features.DAO.pileDAO import PileDAO
import psycopg2
from app.features.DAO.databaseConnection import DatabaseConnection


class GameDAO:

    @staticmethod
    def getBackGame(idGame, nomJeu):

        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "SELECT * FROM %s WHERE idGame = %s", (nomJeu, idGame)
            )
            data = curseur.fetchall()[0]
            connexion.commit()
        finally:
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)
        return(data)
    
    @staticmethod 
    def saveMiddleGame()

    @staticmethod
    def addGame(nomJeu, listString):
        """ Ajoute une partie prête à commencer dans la base de données """
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "INSERT INTO Games (jeu,idPlayers,finished,debut) VALUES (%s,%s, %s, %s) ;",
                (nomJeu, listString, False, True))  # pk un player alors que les guests aussi peuvent ??
            connexion.commit()
        except psycopg2.Error as error:
            connexion.rollback()
            raise error
        finally:
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)

    @staticmethod
    def saveGame(idGame):
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "SELECT * FROM piles WHERE idGame = %s RETURNING ipile", (idGame,))
            piles = curseur.fetchall()
            pilesStr = ' '.join(map(str, piles))
            curseur.execute(
                "UPDATE Games SET idPiles = %s, finished = True WHERE idGame = %s",
                (pilesStr, idGame))  # pk un player alors que les guests aussi peuvent ??
            connexion.commit()
        except psycopg2.Error as error:
            connexion.rollback()
            raise error
        finally:
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)
