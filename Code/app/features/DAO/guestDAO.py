from app.features.users.player import Player

class GuestDAO:
    
    """ Classe Data Access Object de la classe Guest """

    @staticmethod
    def __init__():
        pass
    
    def addAccounttoData(name,mdp):
        """ Ajoute le nouveau compte à la base de données """
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.curseur()
        try:
            curseur.execute(
                "INSERT INTO users (id_users, username,mdp,admini, connected, score) "
                "VALUES (%s,%s, %s, %s, %s, %s) ;",
                (DEFAULT, name, mdp, False, False, NULL))
        
            connexion.commit()
        except psycopg2.Error as error:
            connexion.rollback()
            raise error
        finally:
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)

        
    def checkAccounttoData(username,mdp):
        """Création de l'instance de l'objet utilisateur """
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.curseur()
        try:
            ans = curseur.execute("Select mdp from users WHERE username = %s ", (username))  
            if ans == mdp :
                id_users = curseur.execute("Select id_users from users WHERE username = %s ", (username))
                list_player = []
                player = Player(id_users)
                list_player.append(player)
                curseur.execute("UPDATE users SET connected = TRUE "
                                " WHERE username = %s", (username))
                print("Vous êtes connecté")
        finally :
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)
    
    def addGame() :
        """ Ajoute une partie prête à commencer dans la base de données """
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.curseur()
        try:
            curseur.execute(
                "INSERT INTO Games (idGame, idPiles, idHands,idPlayers,finished,enCours, readyToStart,score",
                "VALUES (%s,%s, %s, %s, %s, %s, %s, %s) ;",
                (DEFAULT, DEFAULT , DEFAULT, player.id_users, False, False, True, NULL))
            connexion.commit()
        except psycopg2.Error as error:
            connexion.rollback()
            raise error
        finally:
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)


       