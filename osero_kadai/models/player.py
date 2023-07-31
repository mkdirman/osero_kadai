#self.xとself.x_of_putting_stoneならどちらが良いのか


class Player():

      def __init__(self,color):
          self.color= color
          self.x_stone_coordinate= 0
          self.y_stone_coordinate= 0

      @property
      def initialize(self):
          self.__init__(self.color)

      @property
      def input_point(self):
          while True:

              self.x_stone_coordinate = input('x座標を入力してね(1-8):')
              self.y_stone_coordinate = input('y座標を入力してね(1-8):')

              try:
                  self.is_none
                  self.is_int
                  self.is_range
              except ValueError as e:
                  print(str(e))
                  continue

              return self.x_stone_coordinate, self.y_stone_coordinate

      @property
      def is_none(self):
          if (self.x_stone_coordinate == '')|(self.y_stone_coordinate == ''):
              raise ValueError('整数で入力してね！')

      @property
      def is_int(self):
          try:
              self.x_stone_coordinate = int(self.x_stone_coordinate)
              self.y_stone_coordinate = int(self.y_stone_coordinate)
          except ValueError:
              raise ValueError('整数で入力してね！')

      @property
      def is_range(self):

          if (self.x_stone_coordinate < 1)|(self.x_stone_coordinate > 8)|(self.y_stone_coordinate < 1)|(self.y_stone_coordinate > 8):
              raise ValueError('1-8で入力してね！')
