"""Ce fichier sert à tester des fonctions individuelles du code 
    """
from app.features.game.apiInteractions.handView import HandView
from app.features.game.cardObjects.cards import Card

if __name__ == "__main__":
    hand = [Card('JACK', 'SPADES'), Card(
        'JACK', 'HEARTS'), Card('ACE', 'SPADES')]
# Les attributs sont inversés
    HandView.displayPoser(hand)
