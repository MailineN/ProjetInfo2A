import psycopg2
from DAO.databaseConnection import DatabaseConnection
 
 
class PileDAO():
 
 
 
 
    def savePileinDataBase(pile):
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.curseur()
        try:
            curseur.execute(
                "INSERT INTO pile "
            )
            
            pile.id = curseur.fetchone()["id_pile"]
            connexion.commit()
        except psycopg2.Error as error:
            connexion.rollback()
            raise error
        finally:
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)



    def getPreviousPiles():
        pass