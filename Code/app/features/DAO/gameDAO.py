import psycopg2
from app.features.DAO.databaseConnection import DatabaseConnection
from psycopg2.extensions import AsIs


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
    def saveMiddleGame(data, idGame, nomJeu):
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.cursor()
        columns = data.keys()
        values = [data[column] for column in columns]
        insert_statement = 'UPDATE %s SET %s = %s WHERE idGame = %s'
        try:
            curseur.execute(insert_statement, (nomJeu, AsIs(
                ','.join(columns)), tuple(values), idGame))
            connexion.commit()
        finally:
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)

    @staticmethod
    def addGame(nomJeu, listString):
        """ Ajoute une partie prête à commencer dans la base de données """
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "INSERT INTO Games (jeu,idPlayers) VALUES (%s,%s) RETURNING idGame;",
                (nomJeu, listString))
            idJeu = curseur.fetchall()  # pk un player alors que les guests aussi peuvent ??
            connexion.commit()
        except psycopg2.Error as error:
            connexion.rollback()
            raise error
        finally:
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)
        return idJeu

    @staticmethod
    def getIDwithPlayers(idPlayers, nomJeu):
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "SELECT * FROM %s WHERE players = %s RETURNING idGame",
                (nomJeu, idPlayers))
            idJeu = curseur.fetchone()
            connexion.commit()
        except psycopg2.Error as error:
            connexion.rollback()
            raise error
        finally:
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)
        return idJeu
