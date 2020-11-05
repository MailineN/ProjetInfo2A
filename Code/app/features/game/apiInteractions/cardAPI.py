import requests
import json
from app.features.game.cardObjects.cards import Card


class cardAPI:
    def __init__(self):
        pass

    @staticmethod
    def newDeck():
        response = requests.get(
            "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
        if (response.status_code == 200) or (response.status_code == 201):
            return(response.json()["deck_id"])
        raise RuntimeError("Une erreur est survenue lors de l'appel de l'API")

    @staticmethod
    def newCustomDeck(listofcard: str):
        response = requests.get(
            "https://deckofcardsapi.com/api/deck/new/shuffle/?cards={}".format(listofcard))
        if (response.status_code == 200) or (response.status_code == 201):
            return(response.json()["deck_id"])
        raise RuntimeError("Une erreur est survenue lors de l'appel de l'API")

    @staticmethod
    def drawDeck(id, count=1):
        response = requests.get(
            "https://deckofcardsapi.com/api/deck/{}/draw/?count={}".format(id, count))
        if (response.status_code == 200) or (response.status_code == 201):
            jsonfile = response.json()
            listCard = []
            for i in len(jsonfile["cards"]):
                card = Card(jsonfile["cards"][i]["value"], jsonfile["cards"]
                            [i]["suits"], jsonfile["cards"][i]["suits"])
                listCard.append(card)
            newid = jsonfile["deck_id"]
            return(listCard, newid)
        raise RuntimeError("Une erreur est survenue lors de l'appel de l'API")

    @staticmethod
    def shuffleDeck(id):
        response = requests.get(
            "https://deckofcardsapi.com/api/deck/{}/shuffle/".format(id))
        if (response.status_code == 200) or (response.status_code == 201):
            return(response.json()["deck_id"])
        raise RuntimeError("Une erreur est survenue lors de l'appel de l'API")
