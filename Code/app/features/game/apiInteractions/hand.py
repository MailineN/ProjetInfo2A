import requests
import json
from app.features.game.cardObjects.card import Card

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
        
    @staticmethod
    def poser():
        
     #on va poser une carte qui appartient à Hand.card_list (utilisation de l'API ? )

        
        pass
    
    @staticmethod
    def tirer():
      response = requests.get(
            "https://deckofcardsapi.com/api/deck/{}/draw/?count={}".format(id, count))
        if (response.status_code == 200) or (response.status_code == 201):
            return(response.json()["deck_id"])
        raise RuntimeError("Une erreur est survenue lors de l'appel de l'API")

      #on va tirer une carte qui appartient à Pile.cardlist (utilisation de l'API ? )
       



        pass