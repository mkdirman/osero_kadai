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

class Game():


    def __init__(self):
        self.game_board= ReversiBoard()

        self.player_turn= 1
        self.x= 0
        self.y= 0
        self.black_score= 0
        self.white_score= 0

        self.mode_game= ModeGame.CPU
        self.mode_turn= ModeTurn.FIRST

    @property
    def set_up_mode_and_turn(self):
        self._choose_mode
        self._choose_turn

    @property
    def is_cpu(self):
        return self.mode_game== ModeGame.CPU.value

    @property
    def is_friends(self):
        return self.mode_game== ModeGame.FRIENDS.value

    @property
    def is_first(self):
        return self.mode_turn== ModeTurn.FIRST.value

    @property
    def is_later(self):
        return self.mode_turn== ModeTurn.LATER.value

    @property
    def is_cpu_or_friends(self):
        return self.is_cpu | self.is_friends

    @property
    def is_first_or_later(self):
        return self.is_first | self.is_later

    @property
    def _choose_mode(self):
        self.mode_game= input('モードを選んでね:cpu or friends---')

    @property
    def _choose_turn(self):
        self.mode_turn= input('先攻か後攻か選んでね:先攻 or 後攻---')
    
    @property
    def set_up_players(self):
        if self.is_cpu:
            self.set_cpu_turn
        else:
            self.p_b= Player(color= 1)
            self.p_w= Player(color= -1)

    @property
    def set_cpu_turn(self):
        if self.is_first:
            self.p_b= Player(color= 1)
            self.p_w= CpuPlayer(color= -1)
        else:
            self.p_b= CpuPlayer(color= 1)
            self.p_w= Player(color= -1) 

    @property
    def set_up_game(self):
        while True:
            self.set_up_mode_and_turn
            try:
                self.is_valid_mode
                self.is_valid_turn
            except ValueError as e:
                print(str(e))
                continue

            self.set_up_players
            break

    @property
    def is_valid_mode(self):
        if self.is_cpu_or_friends:
            print('{}モードで遊びます'.format(self.mode_game))
        else:
            raise ValueError('cpuかfriendsで選択してね')

    @property
    def is_valid_turn(self):
        if self.is_first_or_later:
            print('さあ、ゲームを始めよう')
        else:
            raise ValueError('先攻か後攻で選択してね')

    @property
    def put_stone(self):
        self.set_available_position

        if self.player_turn==1:
            self.x,self.y= self.p_b.input_point
        else:
            self.x,self.y= self.p_w.input_point

        self.game_board.check_already_put(self.x, self.y)
        self.game_board.check_frip_over(self.x, self.y, color= self.player_turn)

    @property
    def set_available_position(self):
        if self.is_cpu:
            if self.is_first:
                self.p_w.set_available_lists(self.game_board.get_available_list(self.p_w.color))
            else:
                self.p_b.set_available_lists(self.game_board.get_available_list(self.p_b.color))

    @property
    def is_available_put(self):
        if (self.game_board.get_available_list(self.player_turn)== []):
            print('置けないよ！')
            self.change_turn

    @property
    def is_continue(self):
        if (self.game_board.get_available_list(self.player_turn)== [])&(self.game_board.get_available_list(-self.player_turn)== []):
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
        self.game_board.show_board(color=self.player_turn)

    @property
    def change_turn(self):
        self.player_turn= -self.player_turn

    @property
    def update_board(self):
        self.game_board.update_board(self.x, self.y, self.player_turn)