import psycopg2
from databaseConnection import DatabaseConnection


class AdminDAO:
    
    """
    deux méthodes:
        
        initDatabase()
        GetAllUserData()
    
    """
    
    def initDatabase(admin):
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

if __name__ == "__main__":
    initDatabase()

        
    def getAllUserData():
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "SELECT id_users,username,mdp,admini,connecte FROM users WHERE username = %s , (username)" )
        connexion.commit()
        print(id_users,username,mdp,admini,connecte) #on print toutes les informations
    except psycopg2.Error as error:
        connexion.rollback()
        raise error
    finally:
        curseur.close
        DatabaseConnection.putBackConnexion(connexion)

if __name__ == "__main__":
    getAllUserData()
