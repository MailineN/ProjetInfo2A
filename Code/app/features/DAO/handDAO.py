import psycopg2
from databaseConnection import DatabaseConnection


class HandDAO:
       
    """ 
        deux méthodes:
        saveHandinDatabase()
        getPreviousHandfromDatabase()
    
    """
      
    def saveHandinDatabase():
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "INSERT qqch INTO HandBDD " #à voir le code sql qu'on doit mettre
        hand = curseur.fetchall() #?
        connexion.commit()
    except psycopg2.Error as error:
        connexion.rollback()
        raise error
    finally:
        curseur.close
        DatabaseConnection.putBackConnexion(connexion)

if __name__ == "__main__":
    saveHandinDatabase()        
        
        
    def getPreviousHandfromDatabase():
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "SELECT qqch FROM hand " #à voir comment ca s'appelle ds la vraie bdd
        hand = curseur.fetchall
        connexion.commit()
    except psycopg2.Error as error:
        connexion.rollback()
        raise error
    finally:
        curseur.close
        DatabaseConnection.putBackConnexion(connexion)

if __name__ == "__main__":
    getPreviousHandfromDatabase()        