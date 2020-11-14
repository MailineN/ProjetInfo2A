import unittest
from app.features.DAO.guestDAO import GuestDAO
from app.features.DAO.databaseConnection import DatabaseConnection
from app.features.DAO.playerDAO import PlayerDAO
from app.features.DAO.adminDAO import AdminDAO

class TestPlayerDAO(unittest.TestCase):

    def testUpdateAccountCredentials(self):
        GuestDAO.addAccounttoData("chloé", "3107")
        score = PlayerDAO.updateAccountCredentials(2,2)
        AdminDAO.deleteUserAccount("chloé")
        self.assertIsNotNone(score)
    
