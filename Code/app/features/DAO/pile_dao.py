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
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.curseur()
        try:
            curseur.execute(
<<<<<<< HEAD
                "SELECT idPile, idGame, card_list FROM pile WHERE idGame=id;"
=======
                "SELECT (pile.card_list[0],pile.card_list[1],pile.card_list[2],pile.card_list[3]) FROM pile WHERE idGame=id;"
>>>>>>> 67de52c677bb160dd1f19c05ea5819bf3727e8a3
            )
        
            resultats = curseur.fetchall()
            PreviousPiles = []
<<<<<<< HEAD
            for resultat in resultats :
                PreviousPiles.append(resultat)
=======
            for resultat in resultats:
                PreviousPiles.append(resultat)
        except psycopg2.Error as error:
            connexion.rollback()
            raise error
>>>>>>> 67de52c677bb160dd1f19c05ea5819bf3727e8a3
        finally:
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)
        return(PreviousPiles)
