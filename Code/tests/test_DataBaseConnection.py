import unittest
from app.features.DAO.databaseConnection import DatabaseConnection


class DatabaseConnectionTest(unittest.TestCase):

    def test_getInstance(self):
        # GIVEN
        reservoir_connexion = DatabaseConnection.getInstance()

        # THEN
        self.assertIsNotNone(reservoir_connexion)

    def test_getConnexion(self):
        # GIVEN
        connexion = DatabaseConnection.getConnexion()

        # THEN
        self.assertIsNotNone(connexion)
