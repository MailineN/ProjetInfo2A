import requests


class cardAPI:
    """ Classe regroupant l'ensemble des méthodes en interaction avec l'API
    """
    def __init__(self):
        pass

    @staticmethod
    def newDeck():
        """ Initialise un deck complet
        """
        response = requests.get(
            "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
        if (response.status_code == 200) or (response.status_code == 201):
            return(response.json()["deck_id"])
        raise RuntimeError("Une erreur est survenue lors de l'appel de l'API, code d'erreur : " + str(response.status_code))

    @staticmethod
    def newCustomDeck(listofcard):
        """ Initialise un deck avec la liste de carte choisie
        listofcard : Liste de carte sous forme de string
        """
        response = requests.get(
            "https://deckofcardsapi.com/api/deck/new/shuffle/?cards={}".format(listofcard))
        if (response.status_code == 200) or (response.status_code == 201):
            return(response.json()["deck_id"])
        raise RuntimeError("Une erreur est survenue lors de l'appel de l'API, code d'erreur : " + str(response.status_code))

    @staticmethod
    def drawDeck(idend, count=1):
        """ Tire le nombre de carte sélectioné du deck
        """
        response = requests.get(
            "https://deckofcardsapi.com/api/deck/{}/draw/?count={}".format(idend, count))
        if (response.status_code == 200) or (response.status_code == 201):
            return(response.json()['cards'], response.json()['deck_id'])
        raise RuntimeError("Une erreur est survenue lors de l'appel de l'API, code d'erreur : " + str(response.status_code))

    @staticmethod
    def shuffleDeck(idend):
        """ Mélange le deck
        """
        response = requests.get(
            "https://deckofcardsapi.com/api/deck/{}/shuffle/".format(idend))
        if (response.status_code == 200) or (response.status_code == 201):
            return(response.json()["deck_id"])
        raise RuntimeError("Une erreur est survenue lors de l'appel de l'API, code d'erreur : " + str(response.status_code))
    
