import unittest
from Code.app.features.game.cardObjects.hand import Hand
from app.features.game.cardObjects.cards import Card

class HandsObjectsTests(unittest.TestCase):

    def testCard(self):
        hand = Hand(1,1,1,[Card(valeur="ACE", couleur="CLUBS"),Card(valeur="JACK", couleur="SPADES")])
        self.assertEqual(str(hand), "Les cartes de la main sont : ACE de CLUBS, JACK de SPADES")





