import psycopg2
from app.features.DAO.databaseConnection import DatabaseConnection
from app.features.DAO.guestDAO import GuestDAO

class PlayerDAO(GuestDAO):

    """ classe Data Access Object de la classe Player """

    def __init__(self):
        pass

    @staticmethod
    def updateAccountCredentials(playerID,score_game):
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
                "UPDATE users SET score = %s WHERE id_users= %s",(new_score, playerID))
            connexion.commit()
        except psycopg2.Error as error:
            connexion.rollback()
            raise error
        finally:
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)

    def getAccountData(playerID):
        """ Renvoie les scores """
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.curseur()
        try:
            curseur.execute(
                "SELECT scores from users WHERE id_users = %s", (playerID))
            ans = curseur.fetchone[0]
            return(ans)
        finally:
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)

    def fetchGame(self,idGame):
        """ Recherche un jeu stocké dans une partie """
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.curseur()
        try:
            curseur.execute("Select * from Games WHERE idGame= %s", (idGame))
            ans = curseur.fetchone()[0]
            if ans is None:
                print("Vous n'avez pas de partie en cours")
            else:
                curseur.execute( "SELECT card1 card2 card3 card4 from Hand WHERE idGame= %s",(idGame)) 
                main = curseur.fetchone[0]
                curseur.execute("SELECT card1 card2 card3 card4 from Pile WHERE idGame=%s",(idGame))
                pile = curseur.fetchone
                return(main,pile)
                # ET LANCE LA PARTIE AUSSI => A FAIRE. 
        finally:
            curseur.close()
            DatabaseConnection.putBackConnexion(connexion)

    def updatePassword(self, hashmdp, newmdp,playerID):
        """ Met à jour dans la base de données le mot de passe qui vient d'être modifié"""
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.curseur()
        try:
            curseur.execute(
                "SELECT username from users WHERE mdp = %s", (hashmdp))
            ans = curseur.fetchone()[0]
            if ans is not None:
                curseur.execute(
                    "UPDATE users SET mdp = %s WHERE username = %s", (newmdp, ans))
                connexion.commit()
                print("Votre mot de passe a bien été changé")
            else:
                print("Votre mot de passe est erroné. Veuillez renouveler l'opération")

        except psycopg2.Error as error:
            connexion.rollback()
            raise error
        finally:
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)
