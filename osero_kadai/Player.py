class Player():

      def __init__(self,color):
          self.color= color
          self.x= 0
          self.y= 0

      @property
      def initialize(self):
          self.__init__(self.color)

      def input_point(self):
          while True:

              self.x= input('x座標を入力してね(1-8):')
              self.y= input('y座標を入力してね(1-8):')

              try:
                  self.check_none
                  self.check_int
                  self.check_range
              except ValueError as e:
                  print(str(e))
                  continue

              return self.x, self.y

      @property
      def check_none(self):
          if (self.x== '')|(self.y== ''):
              raise ValueError('整数で入力してね！')

      @property
      def check_int(self):
          try:
              self.x = int(self.x)
              self.y = int(self.y)
          except ValueError:
              raise ValueError('整数で入力してね！')

      @property
      def check_range(self):

          if (self.x < 1)|(self.x > 8)|(self.y < 1)|(self.y > 8):
              raise ValueError('1-8で入力してね！')
