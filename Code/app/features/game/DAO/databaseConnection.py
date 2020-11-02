
import psycopg2 


class DatabaseConnection:
    
    __instance = None
    @staticmethod
    def getInstance():
        
        if DatabaseConnection.__instance is None:
            DatabaseConnection()
        return DatabaseConnection.__instance


    @staticmethod
    def getConnexion():
        
        return DatabaseConnection.getInstance().getconn()

    @staticmethod
    def closeConnexions():
        
        try :
            DatabaseConnection.getInstance().closeall
            closed = True
        except Exception :
            print("Problème lors de la fermeture")
            closed = False
        return closed

    @staticmethod
    def putBackConnexion(connection):
        DatabaseConnection.getInstance().putconn(connection)

    def __init__(self):
        if DatabaseConnection.__instance != None:
            raise Exception("Cette classe est un singleton. Utiliser la "
                            "méthode getInstance()")
        else:
            DatabaseConnection.__instance = psycopg2.pool.SimpleConnectionPool(1, 2,
                                                                           host='kandula.db.elephantsql.com',
                                                                           port="5432",
                                                                           user='rkvzuxom',
                                                                           password='gxzP6WQlIbmTH6skR39OpzMXTSULsEqy',
                                                                           cursor_factory=RealDictCursor)

    
    

