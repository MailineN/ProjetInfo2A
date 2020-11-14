from app.features.users.guestView import GuestView
from app.features.DAO.databaseConnection import DatabaseConnection


def verif_init_mdp(mdp, vmdp):
    """ Vérifie que le mot de passe est le même que celui de la confirmation """
    if mdp == vmdp:
        return True
    else:
        return False
