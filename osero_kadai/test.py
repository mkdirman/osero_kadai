import unittest

from tests.test_game import TestGame,TestMode
from tests.test_reversi_board import TestReversiBoard
from tests.test_player import TestPlayer
from tests.test_cpu_player import TestCpuPlayer

Mode=TestMode
Game=TestGame
Board=TestReversiBoard
Player=TestPlayer
Cpu=TestCpuPlayer

unittest.main(argv=[''], verbosity=2, exit=False)
