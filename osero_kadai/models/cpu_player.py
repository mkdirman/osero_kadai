import random
from models.player import Point

class CpuPlayer():

      def __init__(self, color:int):
          
          self.color = color

      @property
      def input_point(self):

          points = self.random_choice
          x = points[0]
          y = points[1]
          
          return x, y

      @property
      def random_choice(self):
          return random.choice(Point.available_list)