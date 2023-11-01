from distutils.command import install_scripts
from turtle import mode
import numpy as np

from models.player import Player
<<<<<<< Updated upstream
=======
from models.qplayer import QPlayer
from models.cpu_player import CpuPlayer

>>>>>>> Stashed changes
from models.reversi_board import ReversiBoard
from models.cpu_player import CpuPlayer

import numpy as np
from enum import Enum

#一緒にしてしまうとGameModeにTurnが入る可能性もあるから×

class ModeGame(Enum):
    CPU = 'cpu'
    FRIENDS = 'friends'

    @staticmethod
    def value_of(v: str):

        for k in ModeGame:
            if k.value == v:
                return k
        raise ValueError('cpuかfriendsで選択してね')

    @staticmethod
    def set_up():
        while True:
            try:
                mode = ModeGame.value_of(input('モードを選んでね:cpu or friends---'))
                break
            except ValueError as e:
                print(e)

        return mode



class ModeTurn(Enum):
    FIRST = '先攻'
    LATER = '後攻'

    @staticmethod
    def value_of(v: str):
        for k in ModeTurn:
            if k.value == v:
                return k
        raise ValueError('先攻か後攻で選択してね')

    @staticmethod
    def set_up():
        while True:
            try:
                turn_main_player = ModeTurn.value_of(input('先攻・後攻を選んでね:先攻 or 後攻---'))
                break
            except ValueError as e:
                print(e)

        return turn_main_player


class Players():
    def __init__(
        self,
        first_player: (QPlayer, CpuPlayer),
        later_player: (QPlayer, CpuPlayer)
    )-> None:
        self.first = first_player
        self.later = later_player

class PlayersFactory():
    @staticmethod
    def create_vs_cpu(turn_main_player):

        if turn_main_player == ModeTurn.FIRST:
            return Players(
                first_player = Player(color= 1),
                later_player = CpuPlayer(color= -1)
                )

        if turn_main_player == ModeTurn.LATER:
            return Players(
                first_player = CpuPlayer(color= 1),
                later_player = Player(color= -1)
                )

    @staticmethod
    def create_training_cpu(turn_main_player):

        if turn_main_player == ModeTurn.FIRST:
            return Players(
                first_player = QPlayer(color= 1),
                later_player = CpuPlayer(color= -1)
                )

        if turn_main_player == ModeTurn.LATER:
            return Players(
                first_player = CpuPlayer(color= 1),
                later_player = QPlayer(color= -1)
                )

    @staticmethod
    def create_vs_player():
        return Players(
            first_player = Player(color= 1),
            later_player = Player(color= -1)
            )

class Game():

    def __init__(self, players: Players)-> None:
        self.players = Players
 
        self.game_board = ReversiBoard()

        self.x = 0
        self.y = 0
        self.black_score = 0
        self.white_score = 0
        self.game_turn = 1

    @property
    def initialize(self):
        self.game_board= ReversiBoard()
        self.black_score = 0
        self.white_score = 0
        self.game_turn = 1

    @property
    def put_stone(self):
        self.set_available_position

        self.input_points
        self.game_board.check_already_put(self.x, self.y)
        self.game_board.check_frip_over(self.x, self.y, color= self.game_turn)

    @property
    def learn(self):
        self.players.first.getGameResult(self.game_board.get_numpy_board, self.game_board.get_numpy_avail_list, self.players.later, self.is_continue, self._is_win)

    #名前は
    @property
    def get_numpy_(self):
        return self.game_board.get_numpy_board,self.game_board.get_numpy_avail_list

    @property
    def input_points(self):
        if self.game_turn == 1:
<<<<<<< Updated upstream
            self.x,self.y = self.players.first.input_point
=======
            self.point = self.players.first.input_point(self.game_board.get_numpy_board, self.game_board.get_numpy_avail_list)
>>>>>>> Stashed changes
        if self.game_turn == -1:
            self.x,self.y = self.players.later.input_point

    @property
    def get_numpy_board(self):
        return self.game_board.get_numpy_board


    @property
    def set_available_position(self):
<<<<<<< Updated upstream
        self.players.first.set_available_lists(self.game_board.get_available_list(1))
        self.players.later.set_available_lists(self.game_board.get_available_list(-1))
=======
        Point.available_list = self.game_board.get_available_list(self.game_turn)
        self.game_board.available_list = self.game_board.get_available_list(self.game_turn)
>>>>>>> Stashed changes

    @property
    def is_available_put(self):
        if (self.game_board.get_available_list(self.game_turn) == []):
            print('置けないよ！')
            self.change_turn

    @property
    def is_continue(self):
        if (self.game_board.get_available_list(self.game_turn) == [])&(self.game_board.get_available_list(-self.game_turn) == []):
            return False
        else:
            return True

    @property
    def display_final_score(self):
        self._count_stones
        self._is_win

    @property  
    def _is_win(self):
        if self.black_score > self.white_score:
            print('黒{}:白{}で黒の勝ち！'.format(self.black_score, self.white_score))
            return 1
        elif self.black_score < self.white_score:
            print('黒{}:白{}で白の勝ち！'.format(self.black_score, self.white_score))
            return -1
        else:
            print('引き分け！')
            return 0

    @property
    def _count_stones(self):
        self.black_score = np.sum(self.game_board.get_numpy_board == 1)
        self.white_score = np.sum(self.game_board.get_numpy_board == -1)

    @property
    def display_board(self):
        self.game_board.show_board(color = self.game_turn)

    @property
    def change_turn(self):
        self.game_turn = -self.game_turn

    @property
    def update_board(self):
        self.game_board.update_board(self.x, self.y, self.game_turn)


class GameFactory():

    @staticmethod
    def create(mode: str, turn_main_player: str)->None:

        if mode == ModeGame.CPU:
            #players = PlayersFactory.create_vs_cpu(turn_main_player)  
            players = PlayersFactory.create_training_cpu(turn_main_player)  
        elif mode == ModeGame.FRIENDS:
            players = PlayersFactory.create_vs_player()
        else:
            raise ValueError('mode or turn is None')

        return Game(players)








    

    
