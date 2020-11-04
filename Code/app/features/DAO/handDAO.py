import psycopg2
from databaseConnection import DatabaseConnection





class HandDAO:
    
       
    """ 
        deux méthodes:
        saveHandinDatabase()
        getPreviousHandfromDatabase()
    
    
    """
      
    def saveHandinDatabase():
        # Etape 1 : On récupère une connexion
        connexion = DatabaseConnection.getConnexion()
        
        # Etape 2 : on crée un curseur qui va nous permettre d'exécuter la
        #requête
        curseur = connexion.cursor()
        
        # Etape 3 : on crée un bloc try/except
        try:
            
        # Etape 4 : on exécute notre requête SQL. Les %s vont être remplacé
        #par les valeurs passé dans la seconde partie du execute
            curseur.execute(
                "INSERT qqch INTO HandBDD " #à voir le code sql qu'on doit mettre

                
        # Etape 5 (optionnelle) : on récupère le résultat de la requête
        admin. = curseur.fetchone()[0]
    
        # Etape 6 : on commit notre requête pour la rendre permanente.
        connexion.commit()
        except psycopg2.Error as error:
        
        # Etape 7 : s'il y a une erreur on fait un rollback et on annule
        #la requête
            AbstractDao.connection.rollback()
            raise error
        finally:
        
            # Etape 8 : on ferme le curseur pour libérer de la mémoire coté
            #base et on remet la connexion dans notre reservoir à connexion.
            curseur.close()
            ReservoirConnexion.putBackConnexion(connexion)

        # Etape 9 : on retourne l'objet demandé.
        return 
        
        
        
    def getPreviousHandfromDatabase():
        # Etape 1 : On récupère une connexion
        connexion = DatabaseConnection.getConnexion()
        
        # Etape 2 : on crée un curseur qui va nous permettre d'exécuter la
        #requête
        curseur = connexion.cursor()
        
        # Etape 3 : on crée un bloc try/except
        try:
            
        # Etape 4 : on exécute notre requête SQL. Les %s vont être remplacé
        #par les valeurs passé dans la seconde partie du execute
            curseur.execute(
                "SELECT qqch FROM HandBDD " #à voir le code sql qu'on doit mettre

        # Etape 5 (optionnelle) : on récupère le résultat de la requête
        admin. = curseur.fetchone()[0]
    
        # Etape 6 : on commit notre requête pour la rendre permanente.
        connexion.commit()
        except psycopg2.Error as error:
        
        # Etape 7 : s'il y a une erreur on fait un rollback et on annule
        #la requête
            AbstractDao.connection.rollback()
            raise error
        finally:
        
            # Etape 8 : on ferme le curseur pour libérer de la mémoire coté
            #base et on remet la connexion dans notre reservoir à connexion.
            curseur.close()
            ReservoirConnexion.putBackConnexion(connexion)

        # Etape 9 : on retourne l'objet demandé.
        return 