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
            curseur.execute(
                "CREATE TABLE AdminBDD (id varchar(jsp combien on met), mdp varchar(idem),userType ())"  #???
                #quid du mdp et userType
                #attention il faut mettre un not null à la clé primaire
                
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
                "SELECT * FROM userData" #jsp comment ca s'appelle ds bdd le "userData"
        userData = curseur.fetchall()
        connexion.commit()
        print(userData)
    except psycopg2.Error as error:
        connexion.rollback()
        raise error
    finally:
        curseur.close
        DatabaseConnection.putBackConnexion(connexion)

if __name__ == "__main__":
    getAllUserData()

