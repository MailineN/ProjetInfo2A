import unittest
from app.features.game.cardObjects.handPile import Pile
from app.features.game.cardObjects.cards import Card

class PilesObjectsTests(unittest.TestCase):

    def testPile(self):
        pile = Pile(1,1,[Card(valeur="ACE", couleur="CLUBS"),Card(valeur="JACK", couleur="SPADES")])
        self.assertEqual(str(pile), "Les cartes de la main sont : ACE de CLUBS, JACK de SPADES, ")