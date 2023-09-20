class Point():
    x = 0
    y = 0

    available_list = []
    expect_input_list = [1,2,3,4,5,6,7,8]

    @staticmethod
    def check_input():
        if (Point.x in Point.expect_input_list)&(Point.y in Point.expect_input_list):
            return True
        raise ValueError('1-8の整数で入力してね')


class Player():
      def __init__(self, color:int):
          self.color = color

      @property
      def input_point(self):
          while True:

              Point.x = int(input('x座標を入力してね(1-8):'))
              Point.y = int(input('y座標を入力してね(1-8):'))

              try:
                  Point.check_input()
                  break
              except ValueError as e:
                  print(str(e))
                  continue

          return Point.x, Point.y

