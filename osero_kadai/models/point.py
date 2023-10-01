import numpy as np

class InvalidInputValueException(Exception):
    "範囲外に石を置こうとする"

class Point():
    WALL_LIMIT_LOW = 1
    WALL_LIMIT_HIGH = 8
    ROW_NUM = 0
    COLUMN_NUM = 8

    def __init__(self, x: int, y: int)->None:

        #write_numberの時は使えない。

        #-----------------
        if x < self.WALL_LIMIT_LOW or self.WALL_LIMIT_HIGH < x:
            raise InvalidInputValueException
        if y < self.WALL_LIMIT_LOW or self.WALL_LIMIT_HIGH < y:
           raise InvalidInputValueException
        #-----------------

        self.x = x
        self.y = y

        self.available_list = []

    @staticmethod
    def inputs():
        while True:
            try:
                x = int(input('x座標を入力してね(1-8):'))
                y = int(input('y座標を入力してね(1-8):'))
                return Point(x, y)
            except InvalidInputValueException:
                print("再度入力してください")

    @staticmethod
    def input_board_init(board: np.array((9, 9))):

        board[4,4] = 1
        board[5,5] = 1
        board[4,5] = -1
        board[5,4] = -1

        return board

    @staticmethod
    def is_wall():
        return (Point.x == Point.ROW_NUM)|(Point.y == Point.COLUMN_NUM)




