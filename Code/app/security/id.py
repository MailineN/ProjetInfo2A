def verif_init_id(username):
    """ On vérifie que l'identifiant choisi n'existe pas déjà dans la base de données"""
    connexion = DatabaseConnection.getConnexion()
    curseur = connexion.curseur()
    try : 
        answer = curseur.execute( "SELECT * from users WHERE username = %s ; " , (username))
        if answer == None :
            return True 
        else :
            username = input("Votre identifiant existe déjà, veuillez en choisir un nouveau :")
            return(verif_id(username))
    finally:
        curseur.close
        DatabaseConnection.putBackConnexion(connexion)