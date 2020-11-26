import psycopg2
from app.features.DAO.databaseConnection import DatabaseConnection


class AdminDAO:

    @staticmethod
    def initDatabase():
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            users = AdminDAO.backupAccount()
            curseur.execute(
                open("Code/app/features/DAO/SQL/tableCreation.sql", "r").read())
            for user in users:
                curseur.execute(
                    """ INSERT INTO users (username,mdp,admini,connected)
                    VALUES (%s,%s, %s,%s)
                    """, (user[1], user[2], True, False)
                )
            connexion.commit()
        except psycopg2.Error as error:
            connexion.rollback()
            raise error
        finally:
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)

    @ staticmethod
    def getAllUserData():
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "SELECT * FROM users")
            connexion.commit()
            users = curseur.fetchall()
        except psycopg2.Error as error:
            connexion.rollback()
            raise error
        finally:
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)
        return(users)

    @ staticmethod
    def getAllGameData():
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "SELECT * FROM games")
            connexion.commit()
            games = curseur.fetchall()
        except psycopg2.Error as error:
            connexion.rollback()
            raise error
        finally:
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)
        return(games)

    @ staticmethod
    def deleteUserAccount(username):
        """ Ajoute le nouveau compte à la base de données """
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "DELETE FROM users WHERE username = %s", ((username),))
            connexion.commit()
        except psycopg2.Error as error:
            connexion.rollback()
            raise error
        finally:
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)

    @ staticmethod
    def checkAccounttoData(username, mdpa):
        """Création de l'instance de l'objet utilisateur """
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                """
                SELECT *
                FROM users u
                WHERE u.username = %s AND u.mdp = %s
                """, (username, str(mdpa)))
            id_user = curseur.fetchone()
            if id_user is not None:
                id_user = id_user[3]
            connexion.commit()
        finally:
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)
        return id_user

    @ staticmethod
    def backupAccount():
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                """
                SELECT *
                FROM users u
                WHERE u.admini = TRUE
                """)
            users = curseur.fetchall()
            connexion.commit()
        finally:
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)
        return users


if __name__ == "__main__":
    AdminDAO.initDatabase()
    AdminDAO.getAllUserData()
    AdminDAO.deleteUserAccount()
