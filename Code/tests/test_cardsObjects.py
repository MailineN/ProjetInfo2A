import unittest
from app.features.game.cardObjects.cards import Card
from app.features.game.cardObjects.deck import Deck


class CardsObjectsTests(unittest.TestCase):

    def testCard(self):
        carte = Card(valeur="ACE", couleur="CLUBS")
        self.assertEqual(str(carte), "AS de CLUBS")
