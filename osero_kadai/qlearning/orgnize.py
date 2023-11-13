import random
from copy import deepcopy

from qlearning.board import ReversiBoard
from qlearning.players.qplayer import QPlayer
from qlearning.players.random_player import RandomPlayer


class Organizer:

    def __init__(self, show_board = True, show_result = True, nplay = 1, stat = 100, debug = False):
        self._show_board = show_board
        self._show_result = show_result
        self._nplay = nplay
        self._stat = stat
        self._debug = debug

        self.player1_win_count = 0
        self.player2_win_count = 0
        self.draw_count = 0

    def play_game(self, player1:QPlayer, player2:RandomPlayer):
        p1 = player1
        p2 = player2
       
        for i in range(0, self._nplay):
            (p2, p1) = (p1, p2)

            if self._show_board:
                print('先攻: %s(%s) vs 後攻: %s(%s)' % (p1.name, p1.color, p2.name, p2.color))

            board = ReversiBoard()
            while not board.is_game_over:

                tmpBoard = deepcopy(board.board)
                next_move = p1.next_move(tmpBoard)

                if next_move == None:
                    pass
                else:
                    board.update_board(next_move, p1.color)

                p1.getGameResult(board.board, p2)

                (p1, p2) = (p2, p1)
                
            self._count_result(board)
            self._print_progress(player1,player2,i)

            if (i%200) == 0:
                print(str(i)+'試合目')
                player1.print_loss
                player1.print_reward
        #return player1,player2

    def _print_progress(self, player1 : QPlayer, player2:QPlayer, i:int):
        if self._nplay > 1 and i % self._stat == 0:
            print("Win count, player1(%s): %d, player2(%s): %d, draw: %d" % (
                 player1.name, self.player1_win_count, player2.name, self.player2_win_count, self.draw_count))
            self.player1_win_count=0
            self.player2_win_count=0
            self.draw_count=0


    def _print_winner(self, winner, loser, winner_count, loser_count):
        if self._show_result:
            if winner_count == loser_count:
                print("TIE %s, %s, (%d to %d)" % (winner, loser, winner_count, loser_count))
            else:
                print("%s Wins %s Loses (%d to %d)" % (winner, loser, winner_count, loser_count))

    def _count_result(self, board):
        win_color = board.get_win_color

        if win_color == 1:
            self.player1_win_count += 1
        elif win_color == -1:
            self.player2_win_count += 1
        else:
            self.draw_count += 1