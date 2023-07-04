import unittest

from models.cpu_player import CpuPlayer

class TestCpuPlayer(unittest.TestCase):

    def test_initialize(self):
        player = CpuPlayer(color= 1)

        self.assertEqual(player.color, 1)
        self.assertEqual(player.x, 0)
        self.assertEqual(player.y, 0)
        self.assertEqual(player.available_lists, [])

    def test_set_available_lists(self):
        player = CpuPlayer(color= 1)
        player.set_available_lists([(5,3),(3,5),(4,6),(6,4)])

        self.assertEqual(player.available_lists, [(5,3),(3,5),(4,6),(6,4)])

    def test_random_choice(self):
        player= CpuPlayer(color= 1)
        player.set_available_lists([(5,3),(3,5),(4,6),(6,4)])
        result=player.random_choice

        self.assertIn(result,[(5,3),(3,5),(4,6),(6,4)])

    def test_input_point(self):
        player= CpuPlayer(color= 1)
        player.set_available_lists([(5,3),(3,5),(4,6),(6,4)])
        x,y=player.input_point

        self.assertIn((x,y),[(5,3),(3,5),(4,6),(6,4)])








