import unittest
from app.features.DAO.pile_dao import PileDAO

class testpileDAO(unnitest.TestCase):
    """Test les fonction de la classe PileDAO"""

    def testnewPile(self):
        test = 00000
        test_pile = PileDAO.newPile(test)
        self.assertIsNotNone(idPile)
        deleted = PileDAO.delete(test_pile)
        self.assertTrue(deleted)
