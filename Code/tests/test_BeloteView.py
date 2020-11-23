import unittest
from unittest.mock import patch

from app.features.game.gameMechanics.beloteView import BeloteView
from app.features.game.cardObjects.cards import Card
from app.features.users.player import Player


class BeloteViewTest(unittest.TestCase):

    @patch('app.features.game.gameMechanics.beloteView.prompt')
    def testPoser(self, mockPoser):
        hand = [
            Card('ACE', 'DIAMONDS'),
            Card('9', 'DIAMONDS'),
            Card('KING', 'DIAMONDS'),
            Card('7', 'DIAMONDS')
        ]
        player = Player('test', hand)
        mockPoser.return_value = {'pose': "2. KING de DIAMONDS"}
        carte = BeloteView.displayPoser(player, [])
        self.assertIsNotNone(carte)
        self.assertEqual(carte.valeur[0], 'KING')
        self.assertEqual(carte.couleur[0], 'DIAMONDS')
