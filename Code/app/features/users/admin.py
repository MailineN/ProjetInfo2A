# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 11:24:38 2020

@author: id1537
"""

"""
Questions 

- 

"""


class Admin(Player):
    
    """
    trois méthodes
    
    createPlayerAccount()
    deletePlayerAccount()
    seePlayerAccount()
    
    """
    
    def __init__(self):
        
        super
        
        Player.__init__(self, identifiant, "Admin") #il hérite de l'attribut userType

    def createPlayerAccount():
        
        #créer un compte de player c'est ajouter une ligne à la bdd (?)
        "INSERT INTO AdminBDD (id, mdp, userType)"
        
        pass
    

    def deletePlayerAccount():
        
        pass
    
    def seePlayerAccount():
        
        pass
