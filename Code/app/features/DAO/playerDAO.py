import psycopg2
from app.features.DAO.databaseConnection import DatabaseConnection
from app.features.DAO.guestDAO import GuestDAO


class PlayerDAO(GuestDAO):

    """ classe Data Access Object de la classe Player """

    def __init__(self):
        pass

    @staticmethod
    def updateAccountCredentials(playerID, score_game):
        """ Met à jour les scores dans la base de données """
        # Mettre le code qui récupère le score dans un objet previous_score.

        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "SELECT score from users WHERE id_users= %s", playerID)
            previous_score = curseur.fetchone[0]
            new_score = previous_score + score_game
            curseur.execute(
                "UPDATE users SET score = %s WHERE id_users= %s", (new_score, playerID))
            connexion.commit()
        except psycopg2.Error as error:
            connexion.rollback()
            raise error
        finally:
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)

    @staticmethod
    def getAccountDataBelote(id_users):
        """ Renvoie les scores """
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                """SELECT * 
                FROM games g INNER JOIN belote b ON (g.idGame = b.idGame) 
                WHERE position(b.players in %s) >0 """ , (id_users[0][1],))
            ans = curseur.fetchall()
            connexion.commit()
        finally:
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)
        return(ans)

    @staticmethod
    def updatePassword(username, hashmdp, newmdp):
        """ Met à jour dans la base de données le mot de passe qui vient d'être modifié"""
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "UPDATE users SET mdp = %s WHERE mdp = %s and username = %s RETURNING username", (newmdp, hashmdp, username))
            connexion.commit()
            rep = curseur.fetchone()[0]
        except psycopg2.Error as error:
            connexion.rollback()
            raise error
        finally:
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)
            return rep

    @staticmethod
    def updateName(username, hashmdp, nusername):
        """ Met à jour dans la base de données le mot de passe qui vient d'être modifié"""
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "UPDATE users SET username = %s WHERE mdp = %s and username = %s RETURNING username", (nusername, hashmdp, username))
            connexion.commit()
            rep = curseur.fetchone()[0]
        except psycopg2.Error as error:
            connexion.rollback()
            raise error
        finally:
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)
        return rep