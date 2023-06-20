import unittest
from unittest.mock import patch
from io import StringIO
import numpy as np

from Game import Game

class TestGame(unittest.TestCase):

    def test_initialize_game(self):

        game= Game()

        game.game_board.board[1,1]=1
        game.initialize_game

        exboard= np.zeros((9,9))
        exboard[4,4]= 1
        exboard[5,5]= 1
        exboard[4,5]= -1
        exboard[5,4]= -1

        self.assertTrue(np.array_equal(game.game_board.board, exboard))
        self.assertEqual(game.turn, 1)
        self.assertEqual(game.x, 0)
        self.assertEqual(game.y, 0)
        self.assertEqual(game.black_score, 0)
        self.assertEqual(game.white_score, 0)

        return self

    def test_input_main(self):
        game= Game()

        game.input_main

        self.assertEqual(game.x, 5)
        self.assertEqual(game.y, 3)

    def test_is_available(self):
        game= Game()
        game.game_board.board=np.ones((9,9))
        game.game_board.board[1,1]= -1
        game.game_board.board[8,1]= 0

        game.is_available

        self.assertEqual(game.turn, -1)

    def test_is_gameover_True(self):
        game= Game()
        game.game_board.board= np.ones((9,9))
        game.game_board.board[1,1]= -1

        result= game.is_gameover

        self.assertTrue(result)

    def test_is_gameover_False(self):
        game= Game()
        game.game_board.board= np.ones((9,9))
        game.game_board.board[1,1]= -1
        game.game_board.board[8,1]= 0

        result= game.is_gameover

        self.assertFalse(result)


        game.initialize_game

        result= game.is_gameover

        self.assertFalse(result)

    def test_get_score(self):
        game= Game()

        game.get_score

        self.assertEqual(game.black_score, 2)
        self.assertEqual(game.white_score, 2)

    def test_show_score(self):
        game= Game()

        game.get_score
    def test_show_score_black_win(self):
        game= Game()
        game.black_score= 33
        game.white_score= 31

        expected_output= "黒33:白31で黒の勝ち！\nゲーム終了！\n"

        with patch('sys.stdout', new=StringIO()) as fake_out:
            game.show_score
            actual_output= fake_out.getvalue()

        self.assertEqual(actual_output, expected_output)
    def test_show_score_white_win(self):
        game= Game()

        game.black_score= 31
        game.white_score= 33

        expected_output= "黒31:白33で白の勝ち！\nゲーム終了！\n"

        with patch('sys.stdout', new=StringIO()) as fake_out:
            game.show_score
            actual_output= fake_out.getvalue()

        self.assertEqual(actual_output, expected_output)

    def test_show_score_draw(self):
        game= Game()

        game.black_score= 32
        game.white_score= 32

        expected_output= "引き分け！\nゲーム終了！\n"

        with patch('sys.stdout', new=StringIO()) as fake_out:
            game.show_score
            actual_output= fake_out.getvalue()

        self.assertEqual(actual_output, expected_output)

unittest.main(argv=[''], verbosity=2, exit=False)