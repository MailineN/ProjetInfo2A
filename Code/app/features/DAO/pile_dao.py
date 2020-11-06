import psycopg2
from app.features.DAO.databaseConnection import DatabaseConnection
from app.features.game.cardObjects.cards import Card


class PileDAO():

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
    def getPreviousPiles(id):
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.curseur()
        try:
            curseur.execute(
                "SELECT idPile, idGame, card1, card2, card3, card4t FROM pile WHERE idGame=id;"
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
    def getPile(id):
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.curseur()
        try:
            curseur.execute(
                "SELECT card1, card2, card3, card4 FROM pile WHERE idPile=id;"
            )

            resultats = curseur.fetchall()
            PreviousPiles = []
            for resultat in resultats:
                PreviousPiles.append(Card.toCards(resultat))
        finally:
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)
        return(PreviousPiles)

