import psycopg2
from app.features.DAO.databaseConnection import DatabaseConnection
from app.features.game.cardObjects.cards import Card


class PileDAO():

    def newPile(idGame):
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.curseur()
        try:
            curseur.execute(
                "INSERT INTO pile (idGame)"
                "VALUES (%s)  RETURNING idPile "
                (pile.idGame)
        #On récupère l'id de la pile        
        pile.id = curseur.fetchone()["idPile"]       
            )
            connexion.commit()
        except psycopg2.Error as error:
            # la transaction est annulée
            connexion.rollback()
            raise error
        finally:
            curseur.close()
            PoolConnection.putBackConnexion(connexion)
        return idPile

    def savePileinDataBase(pile):
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.curseur()
        try:
            curseur.execute(
                "INSERT INTO pile (idPile, idGame, card_list)"
                "VALUES (%s, %s, %s, %s,%s,%s) RETURNING idPile "
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
    def getPreviousPiles(idGame):
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.curseur()
        try:
            curseur.execute(
                "SELECT idPile, idGame, card1, card2, card3, card4t FROM pile WHERE idGame=%s;"
                (idGame)
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
        curseur = connexion.curseur()
        try:
            curseur.execute(
                "SELECT card1, card2, card3, card4 FROM pile WHERE idPile=%s;"(idPile)
            )

            resultats = curseur.fetchall()
            PreviousPiles = []
            for resultat in resultats:
                PreviousPiles.append(Card.toCards(resultat))
        finally:
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)
        return(PreviousPiles)

