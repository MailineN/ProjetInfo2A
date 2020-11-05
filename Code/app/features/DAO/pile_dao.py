import psycopg2
from databaseConnection import DatabaseConnection
 
 
class PileDAO():

 
    def savePileinDataBase(pile):
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.curseur()
        try:
            curseur.execute(
                "INSERT INTO pile (idPile, idGame, card_list)"
                "VALUES (%s, %s, %s) RETURNING idPile "
                (pile.idPile, pile.idGame, pile.card_list)
            )

            pile.id = curseur.fetchone()["idPile"]
            connexion.commit()
        except psycopg2.Error as error:
            connexion.rollback()
            raise error
        finally:
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)



    def getPreviousPiles(id):
        pass connexion = DatabaseConnection.getConnexion()
        curseur = connexion.curseur()
        try:
            curseur.execute(
                "SELECT idPile, idGame, card_list FROM pile WHERE idGame=id;"
            )
        
            resultats = curseur.fetchall()
            PreviousPiles = []
            for resultat in resultats :
                PreviousPiles.append(resultat)
        finally:
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)
        return(PreviousPiles)
