import random

class CpuPlayer():

      def __init__(self,color):
          
          self.color= color
          self.x_stone_coordinate= 0
          self.y_stone_coordinate= 0
          self.available_lists=[]

      @property
      def input_point(self):
          
          points= self.random_choice
          self.x_stone_coordinate= points[0]
          self.y_stone_coordinate= points[1]
          
          return self.x_stone_coordinate, self.y_stone_coordinate

      def set_available_lists(self,available_lists):
          self.available_lists= available_lists
      
      @property
      def random_choice(self):
          return random.choice(self.available_lists)


