import numpy as np

class InvalidInputValueException(Exception):
    "範囲外に石を置こうとする"

class Point():
    WALL_LIMIT_LOW = 1
    WALL_LIMIT_HIGH = 8
    ROW_NUM = 0
    COLUMN_NUM = 8

    def __init__(self, x: int, y: int, color = None)->None:
        self.x = x
        self.y = y
        self.color = color

        self.available_list = []

        if self.is_number_pos:
            pass
        else:
            if x < self.WALL_LIMIT_LOW or self.WALL_LIMIT_HIGH < x:
               raise InvalidInputValueException
            if y < self.WALL_LIMIT_LOW or self.WALL_LIMIT_HIGH < y:
               raise InvalidInputValueException

    def __eq__(self, other)->bool:
         return self.x == other.x and self.y == other.y and self.color == other.color

    @staticmethod
    def inputs(color: int):
        while True:
            try:
                x = int(input('x座標を入力してね(1-8):'))
                y = int(input('y座標を入力してね(1-8):'))
                return Point(x, y, color)
            except InvalidInputValueException:
                print("再度入力してください")

    #pltを使って表示する際と、np.array()の配置が違う為ややこしい。
    @property
    def is_number_pos(self):
        return (self.x == 0)|(self.y == 0)

    @property
    def is_0(self):
        return self.color == 0

    def is_same_color(self,other):
        return self.color == other.color

    #@staticmethod
    def get_right_point(self, i):
        return Point(self.x + i, self.y)
    #@staticmethod
    def get_left_point(self, i):
        return Point(self.x - i, self.y)
    #@staticmethod
    def get_top_point(self, i) :
        return Point(self.x , self.y + i)

    def get_bottom_point(self, i):
        return Point(self.x , self.y - i)

    def get_top_right_point(self, i):
        return Point(self.x + i, self.y + i)

    def get_top_left_point(self, i):
        return Point(self.x - i, self.y + i)

    def get_bottom_right_point(self, i):
        return Point(self.x + i, self.y - i)

    def get_bottom_left_point(self, i):
        return Point(self.x - i, self.y - i)