
from models.game import Game

game=Game()


def main():
    game.set_up_game

    while game.is_continue:

        game.is_available

        game.show_board
        try:
            game.put_stone
        except ValueError as e:
            print(str(e))
            continue

        game.update_board
        game.change_turn

    game.show_score

if __name__ == "__main__":
    main()

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
