import numpy as np
import random
from copy import deepcopy, copy

from qlearning.board import ReversiBoard
from qlearning.players.random_player import RandomPlayer

class QPlayer():
      DEFAULT_E = 0.1

      def __init__(self, color, e=DEFAULT_E, alpha=0.3):
          self.color = color
          self.name = 'ql'
          self.q = Quantity(alpha, 0.9)
          self.next_q_list = []
          self._e = e
          self._action_count = 0

          self._last_board = None
          self._last_move = None

      def next_move(self, board_data) -> tuple[int,int] or None:
          return self._policy(board_data)

      def _policy(self, board_data) -> tuple[int,int] or None:

           self._last_board = deepcopy(board_data)
           board = ReversiBoard(board_data)

           positions = board.get_available_list(self.color)
           if len(positions) == 0:
                return None

           move = self._e_greeting(positions)

           return move

      def _e_greeting(self, positions:list) -> tuple[int,int]:

           if random.random() < (self._e / (self._action_count // 10000 + 1)):
                move = random.choice(positions)
           else:
                move = self._get_best_move(positions)

           self._last_move = move

           return move


      def _get_best_move(self, positions:list) -> tuple[int,int]:

           qs = []

           for position in positions:
               qs.append(self.q.get(tuple(self._last_board.ravel()), position))
           max_q = max(qs)
           #print('max_q:'+str(qs))
                
           #qs.countで最大値の物が一個以上あった場合、ランダムに選択する
           if qs.count(max_q) > 1:
                best_options = [i for i in range(len(positions)) if qs[i] == max_q]
                i = random.choice(best_options)
           else:
                i = qs.index(max_q)

           move = positions[i]

           return move



      #fsを学習者が次に行動を選択する状態に設定する事がポイント
      def getGameResult(self, board_data, opponent_player: RandomPlayer):

           board = ReversiBoard(deepcopy(board_data))
           cpu = opponent_player

           fs,fa = self._get_feature_state_and_acts(board, cpu)
           reward = self._get_reward(board)
           is_game_over = board.is_game_over

           # passしていない場合のみ学習させる
           if self._last_move != None:
               self.learn(self._last_board, self._last_move, reward, fs, fa, is_game_over)
              
           if is_game_over == False:
               self._action_count += 1
               self._last_move = None
               self._last_board = None

      def _get_feature_state_and_acts(self, board: ReversiBoard, cpu: RandomPlayer):
          if board.get_available_list(cpu.color) == []:
              fs = board.board
              fa = []
          else:
              act = cpu.next_move(board.board)
              fs = board.get_next(act, cpu.color)
              fa = board.get_available_list(cpu.color)

          return fs, fa

      #報酬はゲームの最後
      def _get_reward(self, board: ReversiBoard) -> int:
          reward = 0
          if board.is_game_over == True:

              color = board.get_win_color
              if color == self.color:
                   reward = +1
              elif color == '':
                   reward = 0
              elif color != self.color:
                   reward = -1

          return reward

      def learn(self, s, a:tuple, r:int, fs, fa:list, is_game_over: bool):

          list = []

          for position in fa:
              list.append(self.q.get(tuple(fs.ravel()), position))

          if (is_game_over == True)|(len(list) == 0):
                max_q_new = 0
          else:
                max_q_new = max(list)

            #print('max_q_new: %s' % max_q_new)
            #print(list)

          self.next_q_list.append(max_q_new)
          self.q.update(tuple(s.ravel()), a, r, max_q_new)

      @property
      def change_to_battle_mode(self):
          self._e = 0
          self.q._alpha = 0

class Quantity:
    def __init__(self, alpha, gamma, initial_q = 1):
        self._initial_q = initial_q
        self._values = {}
        self._alpha = alpha
        self._gamma = gamma
        self.name = 'qplayer'
    
    #状態と行動からその環境のQを取り出す
    def get(self, state, act):

        if self._values.get((state, act)) is None:
            self._values[(state, act)] = self._initial_q
            return self._initial_q

        return self._values.get((state, act))

    def set(self, state, act, q_value):

        self._values[(state, act)] = q_value

    #(r+self._gamma * max_q)を目指して少しずつ(alphaを使って)更新していく
    def update(self, s, a:tuple, r:int, max_q:float):

        pQ = self.get(s, a)
        new_q = pQ + self._alpha * ((r + self._gamma * max_q) - pQ)
        self.set(s, a, new_q)

        #print('pQ:'+str(pQ))
        #print('new_q:'+str(new_q))
        