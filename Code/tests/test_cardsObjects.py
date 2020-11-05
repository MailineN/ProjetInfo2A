import unittest
from app.features.game.cardObjects.cards import Card


class CardsObjectsTests(unittest.TestCase):

    def testCard(self):
        carte = Card(valeur="ACE", couleur="CLUBS")
        self.assertEqual(str(carte), "ACE de CLUBS")

    def testStrToCard(self):
        texte = "AS de PIQUE"
        texte2 = "TREFLE de 8"
        self.assertEqual(Card.toCards(texte), Card(
            valeur="AS", couleur="PIQUE"))
        self.assertNotEqual(Card.toCards(texte2), Card(
            valeur="AS", couleur="PIQUE"))
