import psycopg2
from app.features.DAO.databaseConnection import DatabaseConnection
from app.features.game.cardObjects.cards import Card


class PileDAO():
    
    @staticmethod
    def newPile(idjeu):
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "INSERT INTO Piles (idGame)"
                "VALUES (%s) RETURNING idPile ",
                (idjeu,)
        #On récupère l'id de la pile        
            )
            idPile = curseur.fetchone()[0]       
            connexion.commit()
        except psycopg2.Error as error:
            # la transaction est annulée
            connexion.rollback()
            raise error
        finally:
            curseur.close()
            DatabaseConnection.putBackConnexion(connexion)
        return idPile

        

    @staticmethod
    def savePileinDataBase(pile):
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "UPDATE Piles SET card1 = %s, card2 = %s, card3 = %s, card4 = %s WHERE idPile = %s",            
                (str(pile.card_list[0]), str(pile.card_list[1]), str(pile.card_list[2]), str(pile.card_list[3]), pile.idPile)
            )
            connexion.commit()
        except psycopg2.Error as error:
            connexion.rollback()
            raise error
        finally:
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)

    @staticmethod
    def getPreviousPiles(idjeu):
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "SELECT idPile, idGame, card1, card2, card3, card4t FROM Piles WHERE idGame=%s",
                (idjeu,)
            )

            resultats = curseur.fetchall()
            PreviousPiles = []
            for resultat in resultats:
                PreviousPiles.append(Card.toCards(resultat))
        finally:
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)
        return(PreviousPiles)

    @staticmethod
    def getPile(idPile):
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "SELECT card1, card2, card3, card4 FROM Piles WHERE idPile=%s",(idPile,)
            )

            resultats = curseur.fetchall()
            PreviousPiles = []
            for resultat in resultats:
                PreviousPiles.append(Card.toCards(resultat))
        finally:
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)
        return(PreviousPiles)

    @staticmethod
    def delete(idPile):
        deleted = False
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "DELETE FROM Piles WHERE idPile=%s"
                , (idPile,)
                )

            if curseur.rowcount > 0:
                deleted = True

            connexion.commit()
        except psycopg2.Error as error:
            connexion.rollback()
            raise error
        finally:
            curseur.close()
            DatabaseConnection.putBackConnexion(connexion)

        return deleted

