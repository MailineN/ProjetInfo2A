import unittest
from unittest.mock import patch

from app.features.game.gameMechanics.beloteView import BeloteView
from app.features.game.cardObjects.cards import Card


class BeloteViewTest(unittest.TestCase):

    def testPoser(self):
        hand = [
            Card(valeur="ACE", couleur="DIAMONDS"),
            Card(valeur="9", couleur="DIAMONDS"),
            Card(valeur="KING", couleur="DIAMONDS"),
            Card(valeur="7", couleur="DIAMONDS")
        ]

        with patch('app.features.game.gameMechanics.beloteView.BeloteView', return_value=Card(valeur="KING", couleur="DIAMONDS")):
            b = BeloteView()
            rep = b.displayPoser(hand)
            assert rep == Card(valeur="KING", couleur="DIAMONDS")
