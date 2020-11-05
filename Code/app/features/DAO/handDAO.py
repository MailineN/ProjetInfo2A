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
                "INSERT INTO hand (idHand, idGame, idPlayer, card_list)"
                "VALUES (%s, %s, %s, %s) RETURNING idHand "
                (hand.idHand, hand.idGame, hand.idPlayer hand.card_list)
            )
        hand.id = curseur.fetchone()["idHand"]
        connexion.commit()
    except psycopg2.Error as error:
        connexion.rollback()
        raise error
    finally:
        curseur.close
        DatabaseConnection.putBackConnexion(connexion)

if __name__ == "__main__":
    saveHandinDatabase()        
        
        
    def getPreviousHandfromDatabase(id):
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.cursor()
        try:
           curseur.execute(
                "SELECT idHand, idGame, idPlayer, card_list FROM hand WHERE idGame=id;"
            )
        
            resultats = curseur.fetchall()
            PreviousHands = []
            for resultat in resultats :
                PreviousHands.append(resultat)
        finally:
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)
        return(PreviousHands)

if __name__ == "__main__":
    getPreviousHandfromDatabase()        