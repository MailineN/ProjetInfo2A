import unittest
from app.features.game.cardObjects.handPile import Hand
from app.features.game.cardObjects.cards import Card

class HandsObjectsTests(unittest.TestCase):

    def testHand(self):
        hand = Hand(1,1,1,[Card(valeur="ACE", couleur="CLUBS"),Card(valeur="JACK", couleur="SPADES")])
        self.assertEqual(str(hand), "Les cartes de la main sont : ACE de CLUBS, JACK de SPADES, ")

    def testAddCard(self):
        hand = Hand(1,1,1,[Card(valeur="ACE", couleur="CLUBS")])
        hand.addCard(Card(valeur="JACK", couleur="SPADES"))
        self.assertEqual(str(hand),"Les cartes de la main sont : ACE de CLUBS, JACK de SPADES, ")

    



