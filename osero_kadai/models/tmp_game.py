from distutils.command import install_scripts
import numpy as np

from models.player import Player
from models.reversi_board import ReversiBoard
from models.cpu_player import CpuPlayer

import numpy as np
from enum import Enum

class ModeGame(Enum):
    CPU='cpu'
    FRIENDS='friends'

class ModeTurn(Enum):
    FIRST='先攻'
    LATER='後攻'

class Turn():
    def __init__(self):
        self.main_player= ModeTurn.FIRST

    def inputs(self):
        self.main_player = input('先攻後攻を選んでね:先攻 or 後攻---')

    @property
    def is_first(self):
        return self.main_player== ModeTurn.FIRST.value

    @property
    def is_later(self):
        return self.main_player== ModeTurn.LATER.value

    @property
    def is_first_or_later(self):
        return self.is_first | self.is_later

    @property
    def is_valid(self):
        if self.is_first_or_later:
            print('さあ、ゲームを始めよう')
        else:
            raise ValueError('先攻か後攻で選択してね')


class  Mode():
    def __init__(self):
        self.game_mode = ModeGame.CPU

    def inputs(self):
        self.game_mode = input('モードを選んでね:cpu or friends---')

    @property
    def is_cpu(self):
        return self.game_mode== ModeGame.CPU.value

    @property
    def is_friends(self):
        return self.game_mode== ModeGame.FRIENDS.value

    @property
    def is_cpu_or_friends(self):
        return self.is_cpu | self.is_friends

    @property
    def is_valid(self):
        if self.is_cpu_or_friends:
            print('{}モードで遊びます'.format(self.game_mode))
        else:
            raise ValueError('cpuかfriendsで選択してね')


class Players():

    def __init__(self):
        self.first= Player(color=1)
        self.later= Player(color=-1)

    @property
    def set_up(self):
        if self.Mode.is_cpu:
            self.set_up_cpu_and_player

        if self.Mode.is_friends:
            self.set_up_player_and_player

    @property
    def set_up_cpu_and_player(self):
        if self.Turn.is_first:
            self.Player_first=Player(color=1)
            self.Player_later=CpuPlayer(color=-1)

        if self.Turn.is_later:
            self.Player_first=CpuPlayer(color=1)
            self.Player_later=Player(color=-1)

    @property
    def set_up_player_and_player(self):
        if self.Turn.is_first:
            self.Player_first=Player(color=1)
            self.Player_later=Player(color=-1)

        if self.Turn.is_later:
            self.Player_first=Player(color=1)
            self.Player_later=Player(color=-1)

class Game():

    def __init__(self):
        self.game_board= ReversiBoard()
        self.turn=Turn()
        self.mode=Mode()
        self.players=Players()

        self.x= 0
        self.y= 0
        self.black_score= 0
        self.white_score= 0
        self.game_turn=1

    @property
    def set_up_mode_and_turn(self):
        self.turn.inputs
        self.mode.inputs

    @property
    def set_up_game(self):
        while True:
            self.set_up_mode_and_turn
            try:
                self.mode.is_valid
                self.turn.is_valid
            except ValueError as e:
                print(str(e))
                continue

            self.players.set_up
            break

    @property
    def put_stone(self):
        self.set_available_position

        self.input_points
        self.game_board.is_already_put(self.x, self.y)
        self.game_board.is_flip_over(self.x, self.y, color= self.game_turn)

    @property
    def input_points(self):
        if self.game_turn==1:
            self.x,self.y= self.players.first.input_point
        if self.game_turn==-1:
            self.x,self.y= self.players.later.input_point

    @property
    def set_available_position(self):#cpu_playerに移行してもいいかも？
        if self.mode.is_cpu:
            if self.turn.is_first:
                self.players.first.set_available_lists(self.game_board.get_available_list(1))
            else:
                self.players.later.set_available_lists(self.game_board.get_available_list(-1))

    @property
    def is_available_put(self):
        if (self.game_board.get_available_list(self.game_turn)== []):
            print('置けないよ！')
            self.change_turn

    @property
    def is_continue(self):
        if (self.game_board.get_available_list(self.game_turn)== [])&(self.game_board.get_available_list(-self.game_turn)== []):
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
        elif self.black_score < self.white_score:
            print('黒{}:白{}で白の勝ち！'.format(self.black_score, self.white_score))
        else:
            print('引き分け！')
        print('ゲーム終了')

    @property
    def _count_stones(self):
        self.black_score= np.sum(self.game_board.board== 1)
        self.white_score= np.sum(self.game_board.board== -1)

    @property
    def display_board(self):
        self.game_board.show_board(color=self.game_turn)

    @property
    def change_turn(self):
        self.game_turn= -self.game_turn

    @property
    def update_board(self):
        self.game_board.update_board(self.x, self.y, self.game_turn)
