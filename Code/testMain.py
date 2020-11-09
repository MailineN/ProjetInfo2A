"""Ce fichier sert à tester des fonctions individuelles du code 
    """
from app.features.game.cardObjects.cards import Card
from app.features.game.gameMechanics.beloteView import BeloteView


if __name__ == "__main__":
    hand = [Card('SPADES', 'JACK'), Card('SPADES', 'JACK'), Card(
        'SPADES', 'JACK'), Card('SPADES', 'JACK'), Card('SPADES', 'JACK')]
    carteAppel = Card('SPADES', '8')
    # Les attributs sont inversés
    BeloteView.displayPoser(hand)