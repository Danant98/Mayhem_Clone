import unittest
from player import Player

class test_player(unittest.TestCase):

    def test_hit(self):
        self.assertTRUE(Player().hitByOtherPlayer().HIT)
