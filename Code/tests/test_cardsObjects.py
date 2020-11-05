import unittest
from app.features.game.cardObjects.cards import Card
from app.features.game.cardObjects.deck import Deck


class CardsObjectsTests(unittest.TestCase):

    def testCard(self):
        carte = Card(valeur="ACE", couleur="CLUBS")
        self.assertEqual(str(carte), "AS de CLUBS")

    def testStrToCard(self):
        texte = "AS de PIQUE"
        texte2 = "TREFLE de 8"
        self.assertEqual(Card.toCards(texte), Card("AS", "PIQUE"))
        self.assertNotEqual(Card.toCards(texte2), Card("AS", "PIQUE"))
