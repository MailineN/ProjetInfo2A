import psycopg2
from app.features.DAO.databaseConnection import DatabaseConnection


class HandDAO:

    @staticmethod
    def newHand(idjeu, idUsers):
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                """INSERT INTO Hands (idGame,idUsers)
                VALUES (%s,%s) RETURNING hands.idhands """,
                (int(idjeu), idUsers)
                # On récupère l'id de la hand
            )
            idHand = curseur.fetchone()[0]
            connexion.commit()
        except psycopg2.Error as error:
            # la transaction est annulée
            connexion.rollback()
            raise error
        finally:
            curseur.close()
            DatabaseConnection.putBackConnexion(connexion)
        return idHand

    @staticmethod
    def savehandinDataBase(hand):
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                """UPDATE hands 
                SET (idGame = %s, listCard = %s)
                WHERE idhands = %s""",
                (hand.idGame, hand.card_list, hand.idHand)
            )
            connexion.commit()
        except psycopg2.Error as error:
            connexion.rollback()
            raise error
        finally:
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)

    @staticmethod
    def getHand(idPlayer, idGame):
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "SELECT * FROM hands WHERE idPlayer=%s AND idGame = %s RETURNING listCard", (
                    idPlayer, idGame)
            )

            resultats = curseur.fetchall()
        finally:
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)
        return(resultats)

    @staticmethod
    def delete(idHand):
        deleted = False
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "DELETE FROM hands WHERE idHands=%s", (idHand,)
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
