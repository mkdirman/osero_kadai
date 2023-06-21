import unittest

from Player import Player

class TestPlayer(unittest.TestCase):

    def test_initialize(self):
        player = Player(color= 1)

        player.initialize

        self.assertEqual(player.x, 0)
        self.assertEqual(player.y, 0)
    

    def test_input_point(self):
        player = Player(color= 1)
        result= player.input_point()

        self.assertEqual(player.x, 3)
        self.assertEqual(player.y, 5)

    def test_check_none(self):
        player= Player(color= 1)
        player.x= ''
        player.y= 5

        with self.assertRaises(ValueError):
            player.check_none()

    def test_check_int(self):
        player= Player(color= 1)
        player.x= 'p'
        player.y= 4

        with self.assertRaises(ValueError):
            player.check_int()

    def test_check_range(self):
        player= Player(color= 1)
        player.x= 9
        player.y= 5

        with self.assertRaises(ValueError):
            player.check_range()

unittest.main(argv=[''], verbosity=2, exit=False)

unittest.main(argv=[''], verbosity=2, exit=False)