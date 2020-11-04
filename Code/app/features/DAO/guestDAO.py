
class GuestDAO:
    
    """ Classe Data Access Object de la classe Guest """

    @staticmethod
    def __init__():
        pass
    
    def addAccounttoData(id,mdp):
        """ Ajoute le nouveau compte à la base de données """
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.curseur()
        try:
            curseur.execute(
                "INSERT INTO users VALUES (username, mdp  ;",
            )
            
            connexion.commit()
        except psycopg2.Error as error:
            connexion.rollback()
            raise error
        finally:
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)
        
    def checkAccounttoData(id,mdp):
        pass
    