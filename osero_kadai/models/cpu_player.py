import random

class CpuPlayer():

      def __init__(self,color):
          
          self.color= color
          self.x= 0
          self.y= 0
          self.available_lists= []

      @property
      def input_point(self):
          
          points= self.random_choice
          self.x= points[0]
          self.y= points[1]
          
          return self.x, self.y

      def set_available_lists(self,available_lists):
          self.available_lists= available_lists
      
      @property
      def random_choice(self):
          return random.choice(self.available_lists)


