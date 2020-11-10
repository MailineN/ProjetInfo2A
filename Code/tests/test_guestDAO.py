import unittest
from app.features.users.guestView import GuestView
from app.features.DAO.guestDAO import GuestDAO

class TestGuest(unittest.TestCase):
    """Teste les fonctions de la classe GuestDAO"""
    def testAddAccounttoData():
        self.assertEqual(GuestDAO.addAccounttoData("chloé","3107"), "Votre compte a bien été créé")


    def testCheckAccounttoData():
        self.assertEqual(GuestDAO.checkAccounttoData("chloé","3107"), "Vous êtes connecté")

    def testAddGame():
        self.assertEqual(GuestDAO.addGame(),)