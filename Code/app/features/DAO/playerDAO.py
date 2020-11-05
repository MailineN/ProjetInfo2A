from app.features.users.player import Player

class PlayerDAO(GuestDAO):
    
    """ classe Data Access Object de la classe Player """
    
    def __init__(self):
        
        GuestDAO.__init__(self)
    
    def updateAccountCredentials(self):
        """ Met à jour les scores dans la base de données """
        #### Mettre le code qui récupère le score dans un objet previous_score. 

        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.curseur()
        try:
            ans = curseur.execute( "SELECT score from users WHERE id_users= %s", (player.id_users))
            new_score = pervious_score + ans
            curseur.execute("UPDATE users SET score = %s WHERE id_users= %s", 
            ,(new_score, player.id_users))
            connexion.commit()
        except psycopg2.Error as error:
            connexion.rollback()
            raise error
        finally:
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)

    
    def getAccountData(self):
        """ Renvoie les scores """
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.curseur()
        try:
            ans = curseur.execute( "SELECT scores from users WHERE id_users = %s",(player.id_users))
            return(ans)
        finally:
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)
    
    def updatePassword(self, hashmdp, newmdp) :

        """ Met à jour dans la base de données le mot de passe qui vient d'être modifié"""
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.curseur()
        try:
            ans = curseur.execute( "SELECT username from users WHERE mdp = %s", (hashmdp))
            if ans =! None :
                curseur.execute("UPDATE users SET mdp = %s WHERE username = %s", (newmdp,ans))
                connexion.commit()
                print("Votre mot de passe a bien été changé")
            else :
                print("Votre mot de passe est erroné. Veuillez renouveler l'opération")
                Player.changePassword(self)

        except psycopg2.Error as error:
            connexion.rollback()
            raise error
        finally:
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)
    

    
    