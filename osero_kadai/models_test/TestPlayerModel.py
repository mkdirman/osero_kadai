import unittest

from models.PlayerModel import Player

class TestPlayer(unittest.TestCase):

    def test_initialize(self):
        player = Player(color= 1)

        self.assertEqual(player.x, 0)
        self.assertEqual(player.y, 0)
    

    def test_input_point(self):
        player = Player(color= 1)
        print('x=5 and y=3')

        result= player.input_point()

        self.assertEqual(player.x, 5)
        self.assertEqual(player.y, 3)

    def test_check_none(self):
        player= Player(color= 1)
        player.x= ''
        player.y= 5

        with self.assertRaises(ValueError):
            player.is_none

    def test_check_int(self):
        player= Player(color= 1)
        player.x= 'p'
        player.y= 4

        with self.assertRaises(ValueError):
            player.is_int

    def test_check_range(self):
        player= Player(color= 1)
        player.x= 9
        player.y= 5

        with self.assertRaises(ValueError):
            player.is_range
