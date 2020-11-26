from app.features.DAO.databaseConnection import DatabaseConnection


def verif_init_id(username):
    """ On vérifie que l'identifiant choisi n'existe pas déjà dans la base de données
    Args : username (str) : Nom d'utilisateur souhaité par le joueur 
    
    """
    connexion = DatabaseConnection.getConnexion()
    curseur = connexion.cursor()
    try:
        curseur.execute(
            "SELECT * from users WHERE username = %s ; ", ((username),))
        answer = curseur.fetchone()
        connexion.commit()
    finally:
        curseur.close
        DatabaseConnection.putBackConnexion(connexion)
    if answer is None:
        return True
    else:
        return False
