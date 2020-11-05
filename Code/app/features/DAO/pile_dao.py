import psycopg2
from databaseConnection import DatabaseConnection


class PileDAO():

    def savePileinDataBase(pile):
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.curseur()
        try:
            curseur.execute(
                "INSERT INTO Piles (idPile,idGame,card1,card2,card3,card4) \
                VALUES (pile.idPile,pile.idGame,pile.card_list[0],pile.card_list[1],pile.card_list[2],pile.card_list[3]) RETURNING idPile;"
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
                "SELECT (pile.card_list[0],pile.card_list[1],pile.card_list[2],pile.card_list[3]) FROM pile WHERE idGame=id;"
            )

            resultats = curseur.fetchall()
            PreviousPiles = []
            for resultat in resultats:
                PreviousPiles.append(resultat)
        except psycopg2.Error as error:
            connexion.rollback()
            raise error
        finally:
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)
