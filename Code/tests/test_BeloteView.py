import unittest
from unittest.mock import patch

from app.features.game.gameMechanics.beloteView import BeloteView
from app.features.game.cardObjects.cards import Card


class BeloteViewTest(unittest.TestCase):

    @patch('app.features.game.gameMechanics.beloteView.prompt')
    def testPoser(self, mockPoser):
        hand = [
            Card(valeur="ACE", couleur="DIAMONDS"),
            Card(valeur="9", couleur="DIAMONDS"),
            Card(valeur="KING", couleur="DIAMONDS"),
            Card(valeur="7", couleur="DIAMONDS")
        ]

        mockPoser.return_value = Card(valeur="KING", couleur="DIAMONDS")
        carte = BeloteView.displayPoser(hand)
        self.assertEqual(carte == Card(valeur="KING", couleur="DIAMONDS"))
