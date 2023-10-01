from models.point import Point

class Player():
      def __init__(self, color:int):
          self.color = color

      @property
      def input_point(self):
          point = Point.inputs()

          return point

