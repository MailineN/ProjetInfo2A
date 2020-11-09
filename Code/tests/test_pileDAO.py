import unittest
from app.features.DAO.pile_dao import PileDAO
import psycopg2
from app.features.DAO.databaseConnection import DatabaseConnection
from app.features.DAO.gameDAO import GameDAO

class testpileDAO(unittest.TestCase):
    """Test les fonction de la classe PileDAO"""
    GameDAO.newGame()
    def testnewPile(self):
        
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
