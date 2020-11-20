import unittest
from app.features.users.playerGroup import PlayerGroup
from app.features.users.guest import Guest
from app.features.users.player import Player

class TestGuest(unittest.TestCase):

    def testAddPlayer(self) :
        player1 = Player(identifiant = 1,handList = [])
        player2 = Player(2,[])
        player3 = Player(3,[])
        playerGroup1 = PlayerGroup([player1,player2])
        playerGroup2 = PlayerGroup([player1,player2,player3])
        playerGroup1.addPlayer(player3)
        self.assertEqual(playerGroup1,playerGroup2)

