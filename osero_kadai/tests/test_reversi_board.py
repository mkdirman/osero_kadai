import numpy as np
import matplotlib.pyplot as plt
import unittest

from models.reversi_board import ReversiBoard


class TestReversiBoard(unittest.TestCase):

    def test_initialize_board(self):
        board= ReversiBoard()

        self.assertEqual(board.board[4,4], 1)
        self.assertEqual(board.board[5,5], 1)
        self.assertEqual(board.board[4,5], -1)
        self.assertEqual(board.board[5,4], -1)

    def test_update_board_length(self):

        board= ReversiBoard

        board.update_board(5, 3, 1)

        exboard = np.zeros((9,9))
        exboard[4,4]= 1
        exboard[4,5]= -1
        exboard[5,5]= 1
        exboard[5,4]= 1
        exboard[5,3]= 1

        self.assertTrue(np.array_equal(board.board, exboard))

    def test_update_board_width(self):
        board= ReversiBoard()
  
        board.update_board(3, 5, 1)

        exboard = np.zeros((9,9))
        exboard[4,4]= 1
        exboard[4,5]= 1
        exboard[5,5]= 1
        exboard[5,4]= -1
        exboard[3,5]= 1

        self.assertTrue(np.array_equal(board.board, exboard))

    def test_update_board_diagonal1(self):
        board= ReversiBoard()
        board.board[4,4]= 1
        board.board[4,5]= -1
        board.board[5,5]= 1
        board.board[5,4]= 1
        board.board[5,3]= 1

        board.update_board(6, 3, -1)

        exboard= np.zeros((9,9))
        exboard[4,4]= 1
        exboard[4,5]= -1
        exboard[5,5]= 1
        exboard[5,4]= -1
        exboard[5,3]= 1
        exboard[6,3]= -1

        self.assertTrue(np.array_equal(board.board, exboard))

    def test_update_board_diagonal2(self):
        board= ReversiBoard()
        board.board[4,3]= -1
        board.board[4,4]= -1
        board.board[4,5]= -1
        board.board[5,3]= 1
        board.board[5,4]= 1
        board.board[5,5]= 1

        board.update_board(3, 2, 1)

        exboard= np.zeros((9,9))
        exboard[4,3]= 1
        exboard[4,4]= -1
        exboard[4,5]= -1
        exboard[5,3]= 1
        exboard[5,4]= 1
        exboard[5,5]= 1
        exboard[3,2]= 1
 
        self.assertTrue(np.array_equal(board.board, exboard))

    def test_get_available_list(self):
        board= ReversiBoard()

        result= board.get_available_list(1)

        expected_list= [(5, 3), (6, 4), (3, 5), (4, 6)]
        self.assertEqual(result, expected_list)

    def test_is_Frip_over(self):
        board= ReversiBoard()

        result1= board.is_Frip_over(5, 3, 1)
        result2= board.is_Frip_over(3, 3, 1)

        self.assertTrue(result1)
        self.assertFalse(result2)

    def test_input_judge(self):
        board= ReversiBoard()

        with self.assertRaises(ValueError):
            board.is_Frip_over(3, 2, 1)

    def test_is_already_put(self):
        board= ReversiBoard()

        with self.assertRaises(ValueError):
            board.is_already_put(4, 5)
