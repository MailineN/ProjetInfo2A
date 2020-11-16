from app.features.DAO.databaseConnection import DatabaseConnection
import psycopg2


class GuestDAO:

    """ Classe Data Access Object de la classe Guest """

    @staticmethod
    def __init__():
        pass

    @staticmethod
    def addAccounttoData(name, mdp):
        """ Ajoute le nouveau compte à la base de données """
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "INSERT INTO users (username,mdp,admini,connected) "
                "VALUES (%s,%s, %s,%s) RETURNING username;",
                ((name,), (mdp,), False, False))
            user = curseur.fetchone()[0]
            connexion.commit()
        except psycopg2.Error as error:
            connexion.rollback()
            raise error
        finally:
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)
        return user

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
                """, (username, str(mdpa)))
            curseur.execute("""
                    UPDATE users SET connecte = TRUE 
                    WHERE u.username = %s AND u.mdp = %s 
                """, (username, str(mdpa)))
            id_user = curseur.fetchall()
            connexion.commit()
        finally:
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)
            print(id_user)
        return id_user


# Idem :)
