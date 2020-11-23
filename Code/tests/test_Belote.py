import unittest
from app.features.game.gameMechanics.belote import Belote
from app.features.game.cardObjects.cards import Card
from app.features.users.guest import Guest
from app.features.game.cardObjects.handPile import Pile


class BeloteTests(unittest.TestCase):

    def test_PointsAtout(self):
        players = ['a', 'b', 'a', 'b']
        atout = "DIAMONDS"
        plis = Pile(None, None, card_list=[
            Card(valeur="ACE", couleur="DIAMONDS"),
            Card(valeur="9", couleur="DIAMONDS"),
            Card(valeur="KING", couleur="DIAMONDS"),
            Card(valeur="7", couleur="DIAMONDS")
        ])
        self.assertEqual((29, 1), Belote(players=players).countPoint(plis, atout))

    def test_PointsNonAtout(self):
        players = ['a', 'b', 'a', 'b']
        atout = "CLUBS"
        plis = Pile(None, None, card_list=[
            Card(valeur="ACE", couleur="DIAMONDS"),
            Card(valeur="9", couleur="DIAMONDS"),
            Card(valeur="KING", couleur="DIAMONDS"),
            Card(valeur="7", couleur="DIAMONDS")
        ])

        self.assertEqual((15, 0), Belote(players=players).countPoint(plis, atout))

    def test_PointsCoupe(self):
        players = ['a', 'b', 'a', 'b']
        atout = "HEARTS"
        plis = Pile(None, None, card_list=[
            Card(valeur="ACE", couleur="DIAMONDS"),
            Card(valeur="KING", couleur="DIAMONDS"),
            Card(valeur="8", couleur="DIAMONDS"),
            Card(valeur="7", couleur="HEARTS")
        ])
        self.assertEqual((15, 3), Belote(players=players).countPoint(plis, atout))

    def test_monpote(self):
        team1 = ["player1", "player2"]
        team2 = []
        testmaitre = "player2"
        self.assertTrue(Belote.monpote(
            "player1", testmaitre, team1, team2))

    def testa_de_latout(self):
        atout = "HEARTS"
        testplayer = Guest(handList=[
            Card(valeur="ACE", couleur="DIAMONDS"),
            Card(valeur="KING", couleur="DIAMONDS"),
            Card(valeur="8", couleur="DIAMONDS"),
            Card(valeur="7", couleur="HEARTS")
        ])

        self.assertTrue(Belote.a_de_latout(testplayer, atout))

    def testa_lacouleur(self):
        couleur = "HEARTS"
        testplayer = Guest(handList=[
            Card(valeur="ACE", couleur="DIAMONDS"),
            Card(valeur="KING", couleur="DIAMONDS"),
            Card(valeur="8", couleur="DIAMONDS"),
            Card(valeur="7", couleur="HEARTS")
        ])
        self.assertTrue(Belote.a_lacouleur(testplayer, couleur))

    def test_monteratout(self):
        players = ['a', 'b', 'a', 'b']
        vcarte = 11
        atout = "HEARTS"
        testplayer = Guest(handList=[
            Card(valeur="ACE", couleur="DIAMONDS"),
            Card(valeur="KING", couleur="DIAMONDS"),
            Card(valeur="8", couleur="DIAMONDS"),
            Card(valeur="7", couleur="HEARTS")
        ])

        self.assertFalse(Belote(players=players).monteratout(testplayer, vcarte, atout))

    def test_checkPlayerNumber(self):
        testplayers = [1, 2, 3, 4]
        self.assertEqual(Belote.checkPlayerNumber(
            testplayers), True)
