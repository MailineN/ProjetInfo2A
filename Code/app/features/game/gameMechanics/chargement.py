import threading
from app.features.DAO.gameDAO import gameDAO

def chargement(idGame,nameGame): 
	print("*******************************************************\n")
	print("La partie commencera lorsqu'il y aura assez de joueurs\n")
	print("*******************************************************\n")
	gameDAO.