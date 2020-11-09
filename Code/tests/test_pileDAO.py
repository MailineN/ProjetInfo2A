import unittest
from app.features.DAO.pile_dao import PileDAO
import psycopg2
from app.features.DAO.databaseConnection import DatabaseConnection


class testpileDAO(unittest.TestCase):
    """Test les fonction de la classe PileDAO"""

    def testnewPile(self):

        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.cursor()
        try:
        curseur.execute(
            "INSERT INTO Games (idGame, idPiles, idHands, idPlayers, finished, enCours, readyToStart, score)"
            "VALUES(%s, %s, %s, %s, %s, %s, %s, %s)",
            (None, None, None, None, False, False, False, None)            
        )
            connexion.commit()
        except psycopg2.Error as error:
            connexion.rollback()
            raise error
        finally:
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)

        test = "1"
        test_pile = PileDAO.newPile(test)
        self.assertIsNotNone(test_pile.idPile)
        deleted = PileDAO.delete(test_pile)
        self.assertTrue(deleted)

    

    def testdelete(self):
        test = "00000"
        test_pile = PileDAO.newPile(test)
        deleted = PileDAO.delete(test_pile)
        self.assertTrue(deleted)
