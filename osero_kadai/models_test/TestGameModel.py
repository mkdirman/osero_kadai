import unittest
from unittest.mock import patch
from io import StringIO
import numpy as np

from models.GameModel import Game
from models.PlayerModel import Player
from models.CpuPlayerModel import CpuPlayer

class TestGame(unittest.TestCase):

    def setUp(self):
        game= Game()
  

    def test_initialize_game(self):

        game= Game()

        game.game_board.board[1,1]= 1

        game= Game()

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

    def test__cpu_or_friends_answer_cpu(self):
        game= Game()
        print('cpuの入力可否')

        game._cpu_or_friends

        self.assertEqual(game.mode, 'cpu')

    def test__cpu_or_friends_answer_friends(self):
        game= Game()
        print('friendsの入力可否')

        game._cpu_or_friends

        self.assertEqual(game.mode, 'friends')

    def test__first_or_later_answer_first(self):
        game= Game()
        print('先攻の入力可否')

        game._first_or_later

        self.assertEqual(game.mode_turn, '先攻')

    def test__first_or_later_answer_later(self):
        game= Game()
        print('後攻の入力可否')

        game._first_or_later

        self.assertEqual(game.mode_turn, '後攻')

    def test_set_cpu_turn_first(self):
        game= Game()
        game.mode_turn='先攻'

        game.set_cpu_turn

        self.assertEqual(type(game.p_b).__name__,type(Player(color= 1)).__name__)
        self.assertEqual(type(game.p_w).__name__,type(CpuPlayer(color= -1)).__name__)

    def test_set_cpu_turn_later(self):
        game= Game()
        game.mode_turn='後攻'

        game.set_cpu_turn

        self.assertEqual(type(game.p_b).__name__,type(CpuPlayer(color= 1)).__name__)
        self.assertEqual(type(game.p_w).__name__,type(Player(color= -1)).__name__)

    def test_set_players_mode_cpu(self):
        game= Game()
        game.mode='cpu'
        game.mode_turn='先攻'

        game.set_players

        self.assertEqual(type(game.p_b).__name__,type(Player(color= 1)).__name__)
        self.assertEqual(type(game.p_w).__name__,type(CpuPlayer(color= -1)).__name__)

    def test_set_players_mode_friends(self):
        game= Game()
        game.mode='friends'

        game.set_players

        self.assertEqual(type(game.p_b).__name__,type(Player(color= 1)).__name__)
        self.assertEqual(type(game.p_w).__name__,type(Player(color= -1)).__name__)

    def test_is_valid_mode_cpu(self):
        game= Game()
        game.mode= 'cpu'
        self.assertIsNone(game.is_valid_mode) 

    def test_is_valid_mode_friends(self):
        game= Game()
        game.mode= 'friends'
        self.assertIsNone(game.is_valid_mode) 

    def test_is_valid_mode_invalid(self):
        game= Game()
        game.mode= 'invalid'
        with self.assertRaises(ValueError):
            game.is_valid_mode  

    def test_is_valid_turn_first(self):
        game= Game()

        game.mode_turn= '先攻'

        self.assertIsNone(game.is_valid_turn) 

    def test_is_valid_turn_second(self):
        game= Game()

        game.mode_turn= '後攻'

        self.assertIsNone(game.is_valid_turn) 

    def test_is_valid_turn_invalid(self):
        game= Game()

        game.mode_turn= 'invalid'

        with self.assertRaises(ValueError):
            game.is_valid_turn 

    def test_set_up_cpu_board_first(self):
        game= Game()
        game.mode= 'cpu'
        game.mode_turn= '先攻'
        game.set_players
        game.p_w.set_available_lists([(5,3), (6,4), (3,5), (4,6)])

        game.set_up_cpu_board

        self.assertEqual(sorted(game.p_w.available_lists), sorted([(4,3), (6,5), (3,4), (5,6)]))

    def test_set_up_cpu_board_later(self):
        game= Game()
        game.mode= 'cpu'
        game.mode_turn= '後攻'
        game.set_players
        game.p_b.set_available_lists([(3,5), (5,3), (4,6), (6,4)])

        game.set_up_cpu_board

        self.assertEqual(sorted(game.p_b.available_lists), sorted([(3,5), (5,3), (4,6), (6,4)]))


    def test_is_available(self):
        game= Game()
        game.game_board.board= np.ones((9,9))
        game.game_board.board[1,1]= -1
        game.game_board.board[8,1]= 0

        game.is_available

        self.assertEqual(game.turn, -1)

    def test_is_continue_True(self):
        game= Game()
        game.game_board.board= np.ones((9,9))
        game.game_board.board[1,1]= -1
        game.game_board.board[8,1]= 0

        result= game.is_continue

        self.assertTrue(result)

    def test_is_continue_False(self):
        game= Game()
        game.game_board.board= np.ones((9,9))
        game.game_board.board[1,1]= -1

        result= game.is_continue

        self.assertFalse(result)

    def test__get_score(self):
        game= Game()

        game._get_score

        self.assertEqual(game.black_score, 2)
        self.assertEqual(game.white_score, 2)

    def test_show_score_black_win(self):
        game= Game()
        game.black_score= 33
        game.white_score= 31

        expected_output= "黒33:白31で黒の勝ち！\nゲーム終了\n"

        with patch('sys.stdout', new=StringIO()) as fake_out:
            game._is_win
            actual_output= fake_out.getvalue()
        print(actual_output)

        self.assertEqual(actual_output, expected_output)
    def test_show_score_white_win(self):
        game= Game()
        game.black_score= 31
        game.white_score= 33

        expected_output= "黒31:白33で白の勝ち！\nゲーム終了\n"

        with patch('sys.stdout', new=StringIO()) as fake_out:
            game._is_win
            actual_output= fake_out.getvalue()

        self.assertEqual(actual_output, expected_output)

    def test_show_score_draw(self):
        game= Game()

        game.black_score= 32
        game.white_score= 32

        expected_output= "引き分け！\nゲーム終了\n"

        with patch('sys.stdout', new=StringIO()) as fake_out:
            game._is_win
            actual_output= fake_out.getvalue()

        self.assertEqual(actual_output, expected_output)
