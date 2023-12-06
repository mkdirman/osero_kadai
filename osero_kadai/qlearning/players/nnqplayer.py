import numpy as np
import random
from copy import deepcopy, copy
import matplotlib.pyplot as plt

from qlearning.board import ReversiBoard
from qlearning.players.random_player import RandomPlayer

import warnings
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim


class model(nn.Module):
    def __init__(self, input_size = 4*4, output_size = 4*4):
        super(model, self).__init__()

        self.fc1 = nn.Linear(input_size, 64)
        self.fc2 = nn.Linear(64, 64)
        self.fc3_adv = nn.Linear(64, output_size)
        self.fc3_v = nn.Linear(64,1)

        # Actorの出力層
        self.actor_fc = nn.Linear(64, output_size)

        # Criticの出力層
        self.critic_fc = nn.Linear(64, 1)

        self.softmax = nn.Softmax()

    def forward(self, x):

        x = x.flatten()
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))

        adv = self.fc3_adv(x)
        val = self.fc3_v(x).expand(adv.size())

        x = val + adv - adv.mean(0,keepdim = True)

        return x


def huber_loss(y_true:float, y_pred:float, delta=1.0):
    """
    フーバー損失(delta以降の損失に二乗を外した絶対値損失を適応する)
    →学習の安定化
    """
    error = y_true - y_pred
    absolute_error = torch.abs(error)
    quadratic_error = 0.5 * error**2

    mask = absolute_error < delta
    # フーバー損失を計算
    loss = torch.where(mask, quadratic_error, delta * (absolute_error - 0.5 * delta))

    return loss.mean()

class Quantity:
    BATCH_SIZE = 32
    UPDATE_COUNT = 64
    RANDOM = 10

    def __init__(self, model:model, target_model:model, alpha:float, gamma:float):
        self.model = model
        self.model.train()
        self.target_model = target_model

        self.alpha = alpha
        self.gamma = gamma
        self.optimizer = optim.Adam(self.model.parameters(), lr=alpha)
        self.mse_loss = torch.nn.MSELoss()

        self.loss = 0
        self.count = 0
        self.rewards = 0
        self.loss_list = []
        self.reward_list = []
    
    def get(self, state, action):

        action = action[0]*4+action[1]
        action = torch.tensor(action)
        state_tensor = torch.tensor(state, dtype=torch.float32)

        q_values = self.model(state_tensor)
        return q_values[action]
        
    def update(self,state, action, reward, next_state, is_game_over, priority = None, get_priority_mode = False):

        state_tensor = torch.tensor(state, dtype=torch.float32)
        next_state_tensor = torch.tensor(next_state, dtype=torch.float32)

        #target_netwarkの更新はこちらの決めたタイミングで行う為
        with torch.no_grad():
            next_q_values = self.model(next_state_tensor)
            next_action = torch.argmax(next_q_values)

            target_q_values = self.target_model(next_state_tensor)

        q_values = self.model(state_tensor)

        action = action[0] * 4 + action[1]
        target = reward + self.gamma * target_q_values[next_action]

        loss = huber_loss(q_values[action], target, delta=1.0)

        if get_priority_mode == True:
            priority = float(target-q_values[action])

            return priority
        
        self.loss += loss
        self.count += 1
        self.rewards += reward

        if ((self.count%self.BATCH_SIZE) == 0):
            self.loss_list.append(float(self.loss/self.BATCH_SIZE))
            self.reward_list.append(self.rewards)

            self.optimizer.zero_grad()
            self.loss.backward()
            self.optimizer.step()
            self.loss = 0
            self.rewards = 0
        
        if ((self.count%self.UPDATE_COUNT) == 0):
            self._update_target_network

    # target_modelのパラメータをmodelと同期
    @property
    def _update_target_network(self):
        self.target_model.load_state_dict(self.model.state_dict())


class ReplayBuffer:
    def __init__(self, buffer_size:int):
        self.buffer_size = buffer_size
        self.buffer = pd.DataFrame()
 
    def add(self, experience):

        if len(self.buffer) == 0:
            self.buffer = pd.DataFrame([experience])
            self.buffer.columns = ['s', 'a' , 'reward', 'next_s', 'next_a', 'is_gameover', 'priority']

        else:
        
            index = self._get_reinput_index(experience)

            if (any(index)):
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore")
                    self.buffer['priority'][index] = experience[-1]

            else:
                df = pd.DataFrame([experience])
                df.columns = ['s', 'a' , 'reward', 'next_s', 'next_a', 'is_gameover', 'priority']

                self.buffer = pd.concat([self.buffer, df], ignore_index=True)

    def sample(self, batch_size):
        probs=self._make_priority_probs
        indices = np.random.choice(len(self.buffer), batch_size, p=probs)
        samples = [self.buffer.iloc[idx] for idx in indices]

        return samples

    @property
    def _make_priority_probs(self):
        #priorities = np.array([df['priority'] for i in range(len(self.buffer))])
        priorities = self.buffer['priority']
        priorities = priorities - np.min(priorities)
        probs = priorities / priorities.sum()

        return probs

    @property
    def _get_reinput_index(self,experience):
        s_condition = np.array([np.array_equal(experience[0], tpl) for tpl in self.buffer['s'].values])
        a_condition = np.array([np.array_equal(experience[1], tpl) for tpl in self.buffer['a'].values])
        next_s_condition = np.array([np.array_equal(experience[3], tpl) for tpl in self.buffer['next_s'].values])
        next_a_condition = np.array([np.array_equal(experience[4], tpl) for tpl in self.buffer['next_a'].values])

        index = np.where(s_condition & a_condition & next_s_condition & next_a_condition)[0]
        return index

class NNQPlayer:
      DEFAULT_E = 0.3

      def __init__(self, color, e=DEFAULT_E, alpha=1, replay_buffer_size=10000, replay_batch_size=32):
          self.color = color
          self.name = 'ql'
          self.q = Quantity(model(),model(), alpha, 0.9)
          self.next_q_list = []
          self._e = e
          self._action_count = 0

          self._last_board = None
          self._last_move = None
          self.battle_mode = 'off'

          self.replay_buffer = ReplayBuffer(replay_buffer_size)
          self.replay_batch_size = replay_batch_size

      def next_move(self, board_data) -> tuple[int,int] or None:
          return self._policy(board_data)

      def _policy(self, board_data) -> tuple[int,int] or None:
           self._last_board = deepcopy(board_data)
           board = ReversiBoard(board_data)

           positions = board.get_available_list(self.color)
           if len(positions) == 0:
                return None

           move = self._e_greedy(positions)

           return move

      def _e_greedy(self, positions:list) -> tuple[int,int]:
           if random.random() < (self._e / (self._action_count // 10000 + 1)):
                move = random.choice(positions)
           else:
                move = self._get_best_move(positions)

           self._last_move = move

           return move

      def _get_best_move(self, positions:list) -> tuple[int,int]:
           qs = []
           for position in positions:
               qs.append(float(self.q.get(tuple(self._last_board.ravel()), position)))

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
      #*itemsでまとめない方がミスを発見しやすい？
      def getGameResult(self, board_data, opponent_player: RandomPlayer):
           reward, fs, fa, is_game_over = self._get_qlearn_items(board_data, opponent_player)

           if self.battle_mode == 'off':
               self._set_experience_replay(reward, fs, fa, is_game_over)
               self._do_experience_replay
           
           if is_game_over == False:
               self._action_count += 1
               self._last_move = None
               self._last_board = None

      def _get_qlearn_items(self,board_data, opponent_player: RandomPlayer):
           board = ReversiBoard(deepcopy(board_data))
           cpu = opponent_player

           fs,fa = self._get_feature_state_and_acts(board, cpu)
           reward = self._get_reward(board)
           is_game_over = board.is_game_over

           return reward, fs, fa, is_game_over
      
      def _set_experience_replay(self, reward, fs, fa, is_game_over):

          
           if (self._last_move != None):
               priority = self.learn(self._last_board, self._last_move, reward, fs, fa, is_game_over,priority = None,get_priority_mode = True)#get_priority_mode = Trueの時は学習無し
               self.replay_buffer.add([self._last_board, self._last_move, reward, fs, fa, is_game_over, priority])

           """
           # passしていない場合のみ学習
           if (self._last_move != None)&(self.battle_mode == 'off'):
               self.learn(self._last_board, self._last_move, reward, fs, fa, is_game_over)
           """

      @property
      def _do_experience_replay(self):
           if len(self.replay_buffer.buffer) >= self.replay_batch_size:
               replay_batch = self.replay_buffer.sample(self.replay_batch_size)

               for experience in replay_batch:
                   self.learn(*experience)

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
                   reward = 1
              elif color == '':
                   reward = 0
              elif color != self.color:
                   reward = -1

          return reward

      def learn(self, state, action, reward, next_state, fa, is_game_over, priority=None, get_priority_mode = False):
          return self.q.update(state, action, reward, next_state, is_game_over,priority, get_priority_mode)

      @property
      def change_to_battle_mode(self):
          self._e = 0
          #self.q.model.eval()
          #self.battle_mode = 'on'

      @property
      def print_loss(self):
          y = self.q.loss_list
          x = np.arange(len(y))
          
          plt.plot(x,y)
          plt.xlabel('update_p')
          plt.ylabel('batch_loss')
          plt.show()

      @property
      def print_reward(self):
          y = self.q.reward_list
          x = np.arange(len(y))
          
          plt.plot(x,y)
          plt.xlabel('update_p')
          plt.ylabel('batch_reward')
          plt.show()