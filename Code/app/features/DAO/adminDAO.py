# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 11:25:31 2020

@author: id1537
"""

"""
Questions

- est ce que ds la bdd player il faut pas mettre des attributs genre statistics blabla 
-

"""


class AdminDAO:
    
    """
    deux méthodes:
        
        initDatabase()
        GetAllUserData()
    
    """
    
    def initDatabase(admin):
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
                "CREATE TABLE AdminBDD (id varchar(jsp combien on met), mdp varchar(idem),userType ())"  
                #quid du mdp et userType
                #attention il faut mettre un not null à la clé primaire
                

        # Etape 5 (optionnelle) : on récupère le résultat de la requête
        #admin. = curseur.fetchone()[0]
    
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
        
        
        
    def getAllUserData(admin):
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
                "SELECT (, , ,) FROM AdminBDD"
                            
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