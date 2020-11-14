import unittest
from app.features.DAO.guestDAO import GuestDAO
from app.features.DAO.adminDAO import AdminDAO
from app.features.DAO.databaseConnection import DatabaseConnection


class TestGuestDAO(unittest.TestCase):
    """Teste les fonctions de la classe GuestDAO"""

    def testAddAccounttoData(self):
        GuestDAO.addAccounttoData("chloé", "3107")
        users = GuestDAO.addAccounttoData("chloé", "3107")
        AdminDAO.deleteUserAccount("chloé")
        self.assertIsNotNone(users)

    def testCheckAccounttoData(self):
        GuestDAO.addAccounttoData("chloé", "3107")
        idUser = GuestDAO.checkAccounttoData("chloé", "3107")
        AdminDAO.deleteUserAccount("chloé")
        self.assertIsNotNone(idUser)
    
    
