import psycopg2
from app.features.DAO.databaseConnection import DatabaseConnection
from psycopg2.extensions import AsIs


class GameDAO:

    @staticmethod
    def getBackGame(idGame, nomJeu):

        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            if nomJeu == 'Belote':
                curseur.execute(
                    "SELECT * FROM Belote WHERE idGame = %s", (nomJeu, idGame)
                )
            data = curseur.fetchall()
            if data is not None:
                data = data[0]
            connexion.commit()
        finally:
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)
        return(data)

    @staticmethod
    def saveMiddleGame(data, idGame, nomJeu):
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.cursor()
        if nomJeu == 'Belote':
            insert_statement = """UPDATE Belote SET handlist = %s,score1 = %s,score2 = %s,atout= %s,maitre= %s,teamprenant= %s,finished= %s WHERE idGame = %s"""
        try:
            curseur.execute(insert_statement, (data['handlist'], data['scoreTeam1'],
                                               data['scoreTeam2'], data['atout'], data['maitre'], data['teamPrenant'], data['finished'], idGame))
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
            idJeu = curseur.fetchall()
            if nomJeu == 'Belote':
                curseur.execute(
                    "INSERT INTO Belote (players,finished,idgame) VALUES (%s,%s,%s)", (listString, False, idJeu[0]))
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
            if nomJeu == 'Belote' : 
                curseur.execute(
                    "SELECT * FROM Belote WHERE players = %s RETURNING idGame",
                    (idPlayers,))
            idJeu = curseur.fetchone()
            connexion.commit()
        except psycopg2.Error as error:
            connexion.rollback()
            raise error
        finally:
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)
        return idJeu
