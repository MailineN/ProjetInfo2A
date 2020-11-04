def verif_init_id(identifiant):
    """ On vérifie que l'identifiant choisi n'existe pas déjà dans la base de données"""
    connexion = DatabaseConnection.getConnexion()
    curseur = connexion.curseur()
    try : 
        answer = curseur.execute( "SELECT * from users WHERE id_users = %s ; " , (identifiant))
        if answer == None :
            return True 
        else :
            identifiant = input("Votre identifiant existe déjà, veuillez en choisir un nouveau :")
            return(verif_id(identifiant))
    finally:
        curseur.close
        DatabaseConnection.putBackConnexion(connexion)