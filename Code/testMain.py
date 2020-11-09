"""Ce fichier sert à tester des fonctions individuelles du code 
    """
from app.features.game.cardObjects.cards import Card
from app.features.game.gameMechanics.beloteView import BeloteView


if __name__ == "__main__":
    hand = [
        Card('ACE', 'DIAMONDS'),
        Card('9', 'DIAMONDS'),
        Card('KING', 'DIAMONDS'),
        Card('7', 'DIAMONDS')
    ]
    carteAppel = Card('SPADES', '8')
    # Les attributs sont inversés
    carte = BeloteView.displayPoser(hand)
    print(str(carte))
