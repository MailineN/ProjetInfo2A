import unittest
from app.features.game.users.playerGroup import PlayerGroup
from app.features.game.users.guest import guest
from app.features.game.users.player import Player

class PlayerGroupsObjectsTests(unittest.TestCase):

    def testAddPlayer(self) :
        guest1 = Player("1")
        guest2 = Player("2")
        guest3 = Player("3")
        playerGroup1 = PlayerGroup([guest1,guest2])
        playerGroup2 = PlayerGroup([guest1,guest2,guest3])
        self.assertequal(playerGroup1.addPlayer(guest3),playerGroup2)
