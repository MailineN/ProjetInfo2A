from app.features.users.guestView import GuestView
from app.features.DAO.databaseConnection import DatabaseConnection


def verif_init_id(username):
    """ On vérifie que l'identifiant choisi n'existe pas déjà dans la base de données"""
    connexion = DatabaseConnection.getConnexion()
    curseur = connexion.cursor()
    try:
        answer = curseur.execute(
            "SELECT * from users WHERE username = %s ; ", ((username),))
        if answer is None:
            return True
        else:
            return False
    finally:
        curseur.close
        DatabaseConnection.putBackConnexion(connexion)
