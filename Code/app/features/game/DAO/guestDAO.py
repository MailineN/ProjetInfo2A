
class GuestDAO :
    
    """ Classe Data Access Object de la classe Guest """
    
    def __init__(self):
        
        pass
    
    def addAccounttoData(self):
        #CE CODE EST UN MODELE 
        # Etape 1 : On récupère une connexion
        connexion = databaseConnection.getConnexion()
        # Etape 2 : on crée un curseur qui va nous permettre d'exécuter la requête
        curseur = connexion.cursor()
        # Etape 3 : on crée un bloc try/except
        try:
            # Etape 4 : on exécute notre requête SQL. Les %s vont être remplacé par les valeurs passé dans la seconde partie du execute
            curseur.execute(
                "INSERT INTO arme (nom, description_attaque,degat)"
                " VALUES (%s, %s, %s) RETURNING id_arme;"
                , (arme.nom, arme.description_attaque, arme.degat))
            # Etape 5 (optionnelle) : on récupère le résultat de la requête
            guest.id = curseur.fetchone()[0]
            # Etape 6 : on commit notre requête pour la rendre permanente.
            connexion.commit()
        except psycopg2.Error as error:
            # Etape 7 : s'il y a une erreur on fait un rollback et on annule la requête
            AbstractDao.connection.rollback()
            raise error
        finally:
            # Etape 8 : on ferme le curseur pour libérer de la mémoire coté base et on remet la connexion dans notre reservoir à connexion.
            curseur.close()
            DatabaseConnection.putBackConnexion(connexion)
            # Etape 9 : on retourne l'objet demandé.
        return arme

    
    def checkAccounttoData(self):
        pass
    