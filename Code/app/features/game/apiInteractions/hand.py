from app.features.DAO.handDAO import saveHandinDatabase
from app.features.DAO.handDAO import getPreviousHandfromDatabase


class Hand:

    def __init__(self, card_list):
        self.card_list = card_list
        
    @staticmethod
    def poser():
        
# appelle la bdd pr retirer ce qu'il y a ds la main -> vrmt utile comme ya cardlist ? 

      getPreviousHandfromDatabase()

# stocke la main sous forme de liste



# prendre une carte de cette liste



# je la met ds pile



# refaire une dao pr dire ds la main ya plus cette carte et ds la pile ya cette carte en +
 
        
        pass
    






    @staticmethod
    def tirer():

"""du coup api a ne pas utiliser -> à changer""" 

      response = requests.get(
            "https://deckofcardsapi.com/api/deck/{}/draw/?count={}".format(id, count))
        if (response.status_code == 200) or (response.status_code == 201):
            return(response.json()["deck_id"])
        raise RuntimeError("Une erreur est survenue lors de l'appel de l'API")
       