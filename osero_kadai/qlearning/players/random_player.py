import random
from qlearning.board import ReversiBoard 

class RandomPlayer():

      def __init__(self, color:int):
          
          self.color = color
          self.name = 'randomplayer'

      def next_move(self, board_data)-> tuple[int,int] or None:

          board=ReversiBoard(board_data)
          positions = board.get_available_list(self.color)

          if len(positions)!=0:
              move = self.random_choice(positions)
          else:
              move = None

          return move

      def random_choice(self, positions=[]):
          return random.choice(positions)

      def getGameResult(self, board_data, player):
          pass