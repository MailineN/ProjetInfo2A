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
                "INSERT INTO hand (idHand, idGame, card_list)"
                "VALUES (%s, %s, %s) RETURNING idHand "
                (hand.idHand, hand.idGame, hand.card_list)
                # Tu as oublié de mettre hand en argument de tes fonctions
            )
        hand.id = curseur.fetchone()["idHand"]
        connexion.commit()
    except psycopg2.Error as error:
        connexion.rollback()
        raise error
    finally:
        curseur.close
        DatabaseConnection.putBackConnexion(connexion)

   
        
    def getPreviousHandfromDatabase(id):
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.cursor()
        try:
           curseur.execute(
                "SELECT idHand, idGame, card_list FROM hand WHERE idGame=id;"
            )
        
            resultats = curseur.fetchall()
            PreviousHands = []
            for resultat in resultats :
                PreviousHands.append(resultat)
        finally:
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)
        return(PreviousHands)
# Attention ici tu ne retourne pas un objet Hand mais une liste [idHand,idGame,card_list]

if __name__ == "__main__":
    # Il faut tout mettre à la fin pour le name == main
    getPreviousHandfromDatabase()       
    saveHandinDatabase()     