import psycopg2
from app.features.DAO.databaseConnection import DatabaseConnection


class AdminDAO:

    @staticmethod
    def initDatabase():
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            # path à vérifier
            curseur.execute(
                open("Code/app/features/DAO/SQL/tableCreation.sql", "r").read())
            connexion.commit()
        except psycopg2.Error as error:
            connexion.rollback()
            raise error
        finally:
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)

    @staticmethod
    def getAllUserData(username):
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "SELECT id_users,username,admini,connected, score FROM users WHERE username = %s , (username)")
            connexion.commit()
            users = curseur.fetchall()
            print(users)
        except psycopg2.Error as error:
            connexion.rollback()
            raise error
        finally:
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)

    @staticmethod
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


    @staticmethod
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
                RETURNING admini
                """, (username, str(mdpa)))
            id_user = curseur.fetchone()[0]
            connexion.commit()
        finally:
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)
            print(id_user)
        return id_user


if __name__ == "__main__":
    AdminDAO.initDatabase()
    AdminDAO.getAllUserData()
    AdminDAO.deleteUserAccount()
