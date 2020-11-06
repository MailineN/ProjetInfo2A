from .handDAO import HandDAO
from pileDAO import PileDAO
from GameService import GameService
import psycopg2
from app.features.DAO.databaseConnection import DatabaseConnection

class GameDAO :
        
    def fetchCurrentGame() :

        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "SELECT * FROM games WHERE debut = False"
            )
            game = curseur.fetchone()
            connexion.commit()
        finally: 
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)
        return(game[0])

        

    def fetchSaveGame(gameIDE) :

        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.curseur()
        try:
            curseur.execute(
                "SELECT * FROM hand WHERE hand.id = gameIDE"
            )
            Hand = curseur.fetchone()[1]
            curseur.execute(
                "SELECT * FROM pile WHERE pile.id = gameIDE"
            )
            Pile = curseur.fetchone()[1]
            curseur.execute(
                "SELECT * FROM score WHERE score.id = gameIDE"
            )
            Score = curseur.fetchone()[1]      
        finally:
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)
        return(Hand,Pile,Score)

    @staticmethod
    def fetchNumberPlayerGroup(idGame): 
        """ Va chercher le nombre de joueur dans le groupe d'une partie non commencée 

        Args:
            idGame (int): identifiant du jeu rejoint par le joueur
        """
        connexion = DatabaseConnection.getConnexion()
        curseur = connexion.cursor()
        try:
            curseur.execute(
                "SELECT * FROM games WHERE idGame = idGame"
            )
            game = curseur.fetchall()
            connexion.commit()
        finally: 
            curseur.close
            DatabaseConnection.putBackConnexion(connexion)
            if game[5]: 
                # Si la partie a déja commencé alors on renvoie false et null
                return(False,)
            else: 
                return(True, len(game[3].split())) # On retourne la longueur de la table des joueurs et true 

        



        
        



    



