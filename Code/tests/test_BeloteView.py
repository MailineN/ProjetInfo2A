import unittest
from unittest.mock import patch

from app.features.game.gameMechanics.beloteView import BeloteView
from app.features.game.cardObjects.cards import Card


class BeloteViewTest(unittest.TestCase):

    @patch('app.features.game.gameMechanics.beloteView.prompt')
    def testPoser(self, mockPoser):
        hand = [
            Card('ACE', 'DIAMONDS'),
            Card('9', 'DIAMONDS'),
            Card('KING', 'DIAMONDS'),
            Card('7', 'DIAMONDS')
        ]

        mockPoser.return_value = {'pose': "2. KING de DIAMONDS"}
        carte = BeloteView.displayPoser(hand)
        self.assertIsNotNone(carte)
        self.assertEqual(carte.valeur[0],'KING')
        self.assertEqual(carte.couleur[0],'DIAMONDS')
