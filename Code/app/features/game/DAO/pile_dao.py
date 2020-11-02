import psycopg2
from DAO.pool_connexion import PoolConnection
 
 
class PileDAO():
 
 
 
 
    def savePileinDataBase():
        connexion = PoolConnection.getConnexion()
        curseur = connexion.curseur()
 
 
    def getPreviousPiles():
        pass