import unittest
from Code.app.features.users.guestView import GuestView
from Code.app.features.users.GuestDAO import GuestDAO

class TestGuest(unittest.TestCase):
    """Teste les fonctions de la classe GuestDAO"""
    def testAddAccounttoData():
        self.assertEqual(GuestDAO.addAccounttoData("chloé","3107"), "Votre compte a bien été créé")


