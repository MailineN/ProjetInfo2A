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

        self.assertEqual((29, 1), Belote.countPoint(Belote(), plis, atout))

    def testPointsNonAtout(self):
        atout = "CLUBS"
        plis = [
            Card(valeur="ACE", couleur="DIAMONDS"),
            Card(valeur="KING", couleur="DIAMONDS"),
            Card(valeur="8", couleur="DIAMONDS"),
            Card(valeur="7", couleur="DIAMONDS")
        ]

        self.assertEqual((15, 0), Belote.countPoint(Belote(), plis, atout))

    def testPointsCoupe(self):
        atout = "HEARTS"
        plis = [
            Card(valeur="ACE", couleur="DIAMONDS"),
            Card(valeur="KING", couleur="DIAMONDS"),
            Card(valeur="8", couleur="DIAMONDS"),
            Card(valeur="7", couleur="HEARTS")
        ]

        self.assertEqual((15, 3), Belote.countPoint(Belote(), plis, atout))

    
    def testmonpote(self):
        team1 = ["player1","player2"]
        team2=[]
        testmaitre = "player2"
        maitre = Belote.monpote("player1", testmaitre, team1, team2)
        self.assertEqual(testmaitre,maitre)

    def testade_latout(self):
        atout = "HEARTS"
        testplayer = "testplayer"
        testplayer.handList = [
        Card(valeur="ACE", couleur="DIAMONDS"),
        Card(valeur="KING", couleur="DIAMONDS"),
        Card(valeur="8", couleur="DIAMONDS"),
        Card(valeur="7", couleur="HEARTS")
        ]
        self.assertTrue(Belote.a_de_latout(testplayer,atout))