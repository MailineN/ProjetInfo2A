import unittest
from app.features.users.admin import admin
from app.features.DAO.adminDAO import adminDAO


class AdminTest(unittest.TestCase):

    def testCreateUserAccount(self):
        self.assertEqual("le compte a bien été créé", CreateUserAccount()) #mettre des valeurs
    
    def
        testDeleteUserAccount
