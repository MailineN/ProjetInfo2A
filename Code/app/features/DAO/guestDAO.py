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
                "INSERT INTO users (username,mdp,admini, connected) "
                "VALUES (%s,%s, %s, %s) RETURNING username;",
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
    def checkAccounttoData(username, mdp):
        """Création de l'instance de l'objet utilisateur """
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "Select mdp from users WHERE username = %s ", (username,))
            ans = curseur.fetchone()[0]
            if ans == mdp:
                curseur.execute(
                    "Select id_users from users WHERE username = %s ", (username,))
                id_user = curseur.fetchone()[0]
                curseur.execute("UPDATE users SET connected = True WHERE username = %s ", (username,))
                connexion.commit()
                return id_user
        finally:
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)


# Idem :)
