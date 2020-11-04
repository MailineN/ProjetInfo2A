# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 11:26:41 2020

@author: id1537
"""


"""

Questions

- méthode tirer..? on  tire pas de carte à la belote, on est d'acc que c'est pr abstraire et ajouter des new jeux plus facilement ?? 
- 



"""


import requests
api_draw_card = requests.get('https://deckofcardsapi.com/api/deck/<<deck_id>>/draw/?count=nb') #remplacer le <<deck_id>> et le nb (nb de carte à tirer)
print(api_draw_card)


import requests
adding_to_piles = requests.get('https://deckofcardsapi.com/api/deck/<<deck_id>>/pile/<<pile_name>>/add/?cards=AS,2S') #remplacer le <<deck_id>> et le <<pile_name>>
print(adding_to_piles)



class Hand:
    
    """
    un attribut
    card_list
    
    deux méthodes
    poser()
    tirer()
    
    
    """
    
    def __init__(self, card_list):
        self.card_list = card_list
        
    def poser():
        
     #on va poser une carte qui appartient à Hand.card_list (utilisation de l'API ? )

        
        pass
    

    def tirer():
        
      #on va tirer une carte qui appartient à Pile.cardlist (utilisation de l'API ? )
        
        pass