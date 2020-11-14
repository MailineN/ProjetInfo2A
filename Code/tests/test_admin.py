import unittest
from app.features.users.admin import admin
from app.features.DAO.adminDAO import adminDAO


class AdminTest(unittest.TestCase):

    #pr tester la méthode createUserAccount de la classe Admin, on test la méthode createUserAccount de GuestDAO (?)
    def testCreateUserAccount(self):
        """
        """
        #fait dans test guestDAO car méthode de cette classe utilisée

    def testSeeUserAccount(self):
        self.assertEqual("Le compte a bien été supprimé", AdminDAO.getAllUserData("chloé"))

    #pr tester la méthode deleteUserAccount de la classe Admin, on test la méthode deleteUserAccount de AdminDAO (?)
    def testDeleteUserAccount(self):

        self.assertEqual("Le compte a bien été supprimé", AdminDAO.DeleteUserAccount("chloé","3107"))#mettre des valeurs


