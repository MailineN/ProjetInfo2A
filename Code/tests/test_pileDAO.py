import unittest
from app.features.DAO.pile_dao import PileDAO
import psycopg2
from app.features.DAO.databaseConnection import DatabaseConnection


class PileDAOTests(unittest.TestCase):
    """Test les fonction de la classe PileDAO"""

    def test_newPile(self):

        test = "1"
        test_pile = PileDAO.newPile(test)
        self.assertIsNotNone(test_pile)
        PileDAO.delete(test_pile)

    def test_delete(self):
        test = "1"
        test_pile = PileDAO.newPile(test)
        deleted = PileDAO.delete(test_pile)
        self.assertTrue(deleted)
