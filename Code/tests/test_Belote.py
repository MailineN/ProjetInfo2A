import unittest
from app.features.game.gameMechanics.belote import Belote
from app.features.game.cardObjects.cards import Card


class BeloteTests(unittest.TestCase):

    def testPointsAtout(self):
        atout = "DIAMONDS"
        plis = [
            Card(valeur="ACE", couleur="DIAMONDS"),
            Card(valeur="9", couleur="DIAMONDS"),
            Card(valeur="KING", couleur="DIAMONDS"),
            Card(valeur="7", couleur="DIAMONDS")
        ]

        self.assertEqual((29, 1), Belote.countPoint(Belote(),plis, atout))
