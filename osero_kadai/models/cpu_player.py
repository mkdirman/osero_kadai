import random
from models.point import Point

class CpuPlayer():

      def __init__(self, color:int):
          
          self.color = color

      @property
      def input_point(self):
          point = self.random_choice

          return point

      @property
      def random_choice(self):
          return random.choice(Point.available_list)