import psycopg2
from app.features.DAO.databaseConnection import DatabaseConnection
from app.features.game.cardObjects.hand import Hand


class HandDAO:

    """
        deux méthodes:
        saveHandinDatabase()
        getPreviousHandfromDatabase()

    """

    @staticmethod
    def saveHandinDatabase(hand):
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "INSERT INTO hand (idHand, idGame, idPlayer, card_list)"
                "VALUES (%s, %s, %s, %s) RETURNING idHand "
                (hand.idHand, hand.idGame, hand.idPlayer, hand.card_list)
            )
            hand.id = curseur.fetchone()["idHand"]
            connexion.commit()
        except psycopg2.Error as error:
            connexion.rollback()
            raise error
        finally:
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)

    @staticmethod
    def getPreviousHandfromDatabase(idGame):
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "SELECT idHand, idGame, idPlayer, card_list FROM hand WHERE idGame=%s;" (
                    idGame)
            )
            resultats = curseur.fetchall()
            PreviousHands = []
            for resultat in resultats:
                PreviousHands.append(
                    Hand(resultat[0], resultat[1], resultat[2], resultat[3]))
        finally:
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)
        return(PreviousHands)
# Attention ici tu ne retourne pas un objet Hand mais une liste [idHand,idGame,card_list]


if __name__ == "__main__":
    HandDAO.getPreviousHandfromDatabase()
    HandDAO.saveHandinDatabase()
