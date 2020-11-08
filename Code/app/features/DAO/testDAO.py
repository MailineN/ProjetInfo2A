import psycopg2
from app.features.DAO.databaseConnection import DatabaseConnection
 
def getUsers():
    connexion = DatabaseConnection.getConnexion()
    curseur = connexion.cursor()
    try:
        curseur.execute(
            "SELECT * FROM Users;"
        )
        
        users = curseur.fetchall()
        connexion.commit()
        print(users)
    except psycopg2.Error as error:
        connexion.rollback()
        raise error
    finally:
        curseur.close
        DatabaseConnection.putBackConnexion(connexion)

if __name__ == "__main__":
    getUsers()