import psycopg2
from databaseConnection import DatabaseConnection


class AdminDAO:
  
    def initDatabase():
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.run(tableCreation.sql) #attention pas tout le fichier à run non? que la partie admin, à voir
        connexion.commit()
        except psycopg2.Error as error:
        connexion.rollback()
        raise error
    finally:
        curseur.close
        DatabaseConnection.putBackConnexion(connexion)


        
    def getAllUserData(username):
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "SELECT id_users,username,admini,connected, score FROM users WHERE username = %s , (username)" )
        connexion.commit()
        print(id_users,username,admini,connected, score) #?? on print toutes les informations (à faire ici ou ds la classe admin??)
    except psycopg2.Error as error:
        connexion.rollback()
        raise error
    finally:
        curseur.close
        DatabaseConnection.putBackConnexion(connexion)




    def deleteUserAccount(username):
        """ Ajoute le nouveau compte à la base de données """
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.curseur()
        try:
            curseur.execute(
                "DELETE FROM users WHERE username = %s", (username)
            connexion.commit()
        except psycopg2.Error as error:
            connexion.rollback()
            raise error
        finally:
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)

if __name__ == "__main__":
    initDatabase()
    getAllUserData()
    deleteUserAccount()