import unittest
from app.features.DAO.pile_dao import PileDAO

class testpileDAO(unittest.TestCase):
    """Test les fonction de la classe PileDAO"""

    def testnewPile(self):
        test = 00000
        test_pile = PileDAO.newPile(test)
        self.assertIsNotNone(idPile)
        deleted = PileDAO.delete(test_pile)
        self.assertTrue(deleted)

    def testdelete(self):
        test = 00000
        test_pile = PileDAO.newPile(test)
        deleted = PileDAO.delete(test_pile)
        self.assertTrue(deleted)
