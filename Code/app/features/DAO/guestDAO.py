from app.features.DAO.databaseConnection import DatabaseConnection
import psycopg2
import hashlib
import abc


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
                "VALUES (%s,%s, %s, %s, %s, %s) ;",
                (name, mdp, False, False))

        except psycopg2.Error as error:
            connexion.rollback()
            raise error
        finally:
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)

    @staticmethod
    def checkAccounttoData(username, mdp):
        """Création de l'instance de l'objet utilisateur """
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "Select mdp from users WHERE username = %s ", (username))
            ans = curseur.fetchone()
            if ans == mdp:
                curseur.execute(
                    "Select id_users from users WHERE username = %s ", (username))
                id_user = curseur.fetchone()
                curseur.execute("UPDATE users SET connected = TRUE "
                                " WHERE username = %s", (username))

                connexion.commit()
                return(id_user)
        finally:
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)

# Idem :)
