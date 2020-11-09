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
                "INSERT INTO Piles (idjeu)"
                "VALUES (%s)  RETURNING idPile, "
                (idjeu)
        #On récupère l'id de la pile        
            )
            idPile = curseur.fetchone()["idPile"]       
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
                "INSERT INTO Piles (idPile, idGame, card_list)"
                "VALUES (%s, %s, %s, %s,%s,%s) RETURNING idPile, "
                (pile.idPile, pile.idGame, pile.card_list[0],pile.card_list[1],pile.card_list[2],pile.card_list[3])
            )

            pile.id = curseur.fetchone()["idPile"]
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
                "SELECT idPile, idGame, card1, card2, card3, card4t FROM Piles WHERE idGame=%s,"
                (idjeu)
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
                "SELECT card1, card2, card3, card4 FROM Piles WHERE idPile=%s,"(idPile)
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
                "DELETE FROM Piles WHERE idPile=%s,"
                , (idPile)
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

