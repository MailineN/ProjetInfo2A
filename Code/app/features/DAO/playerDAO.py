import psycopg2
from app.features.DAO.databaseConnection import DatabaseConnection



class PlayerDAO():

    """ classe Data Access Object de la classe Player """

    def __init__(self):
        pass

    def updateAccountCredentials(self,playerID):
        """ Met à jour les scores dans la base de données """
        # Mettre le code qui récupère le score dans un objet previous_score.

        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            ans = curseur.execute(
                "SELECT score from users WHERE id_users= %s", (playerID))
            new_score = pervious_score + ans
            curseur.execute("UPDATE users SET score = %s WHERE id_users= %s",
                            (new_score, playerID))
            connexion.commit()
        except psycopg2.Error as error:
            connexion.rollback()
            raise error
        finally:
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)

    def getAccountData(self,playerID):
        """ Renvoie les scores """
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.curseur()
        try:
            ans = curseur.execute(
                "SELECT scores from users WHERE id_users = %s", (playerID))
            return(ans)
        finally:
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)

    def fetchGame(idGame):
        """ Recherche un jeu stocké dans une partie """
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.curseur()
        try:
            curseur.execute("Select * from Games WHERE idGame= %s", (idGame))
            ans = curseur.fetchone()[0]
            if ans is None:
                print("Vous n'avez pas de partie en cours")
<<<<<<< HEAD
            else :
                main = curseur.execute( "SELECT card1 card2 card3 card4 from Hand WHERE idGame= %s",(idGame)) 
                pile = curseur.execute("SELECT card1 card2 card3 card4 from Pile WHERE idGame=%s",(idGame))
                return(main,pile)
                # ET LANCE LA PARTIE AUSSI => A FAIRE. 
=======
            else:
                # à adapter selon le nom des attributs dans la bdd
                main = curseur.execute(
                    "SELECT card1 card2 card3 card4 from Hand WHERE idGame= %s", (idGame))
                pile = curseur.execute(
                    "SELECT card1 card2 card3 card4 from Pile WHERE idGame=%s", (idGame))
                return(main, pile)
                # ET LANCE LA PARTIE AUSSI => A FAIRE.
>>>>>>> 190900cd90481f544ba032f256f27476c2ac6ab1
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
