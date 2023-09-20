import numpy as np
import matplotlib.pyplot as plt
import random

class Position():
    wall_limit_low = 1
    wall_limit_high = 8
    row_number = 0
    column_number = 8

class Size():
    square = 80
    half_square = 40
    board = 9
    board_on_square = 720
    stone_radius = 30
    available_point_radius = 10

    @staticmethod
    def convert_to_square(x:int):
        return x*Size.square

    @staticmethod
    def convert_to_put_points(x:int, y:int):
        return x*Size.square+Size.half_square, (Size.board_on_square-y*Size.square)-Size.half_square

class StoneColor():
    black = 1
    white = -1

class ReversiBoard():
    def __init__(self):
       
        self.board = np.zeros((Size.board,Size.board))
        self.board[4,4] = 1
        self.board[5,5] = 1
        self.board[4,5] = -1
        self.board[5,4] = -1

        self.available_list = []
        self.i_show_board_splitting_function = 0

        self.ax = None

    def show_board(self, color = 1):
        self._make_baseboard
        self._put_stones_and_available_points

        plt.xlim(0, Size.board_on_square)
        plt.ylim(0, Size.board_on_square)
        self.ax.set_aspect('equal', adjustable='box')
        plt.axis("off")
        plt.show()

    @property
    def _make_baseboard(self):
        self.i_show_board_splitting_function = 0
        _, self.ax = plt.subplots()
        for y in range(Size.board):
            for x in range(Size.board):
                self.write_on_board(x, y)
            
    def write_on_board(self, x:int, y:int):
        y_on_square = Size.convert_to_square(y)
        x_on_square = Size.convert_to_square(x)

        if (x == Position.row_number)|(y == Position.column_number):
            self._write_number(x_on_square, y_on_square)
        else:
            self._write_green_back(x_on_square, y_on_square)

    def _write_number(self, x_:int, y_:int):
        if self.i_show_board_splitting_function == Position.column_number:
            point = None
            self.i_show_board_splitting_function += 1
        else:
            point = abs(Position.column_number-self.i_show_board_splitting_function)
            self.i_show_board_splitting_function += 1

        self.ax.text(x_+Size.half_square, y_+Size.half_square, point, ha = "center", va = "center", fontsize = 10)

    def _write_green_back(self, x_:int, y_:int):
        rectangle = plt.Rectangle((x_, y_), Size.square, Size.square, edgecolor= "black", facecolor= "green")
        self.ax.add_patch(rectangle)

    @property
    def _put_stones_and_available_points(self):
        for x in range(Size.board):
            for y in range(Size.board):
                self.put_stone(x, y)
                self.put_available_point(x, y)

    def put_stone(self, x:int, y:int):
        x_stone, y_stone = Size.convert_to_put_points(x,y)

        if int(self.board[x][y])== StoneColor.black:
            circle = plt.Circle((x_stone, y_stone), Size.stone_radius, edgecolor= "black", facecolor= "black")
            self.ax.add_patch(circle)
        elif int(self.board[x][y])== StoneColor.white:
            circle = plt.Circle((x_stone, y_stone), Size.stone_radius, edgecolor= "black", facecolor= "white")
            self.ax.add_patch(circle)

    def put_available_point(self, x:int, y:int):
        x_point, y_point = Size.convert_to_put_points(x,y)

        if (x,y) in self.available_list:
            circle = plt.Circle((x_point, y_point), Size.available_point_radius, edgecolor= "white", facecolor= "white")
            self.ax.add_patch(circle)

    def update_board(self, x:int, y:int, color:int):
        self.board[x,y] = color
        self.update_length(x, y, color)
        self.update_width(x, y, color)
        self.update_diagonal1(x, y, color)
        self.update_diagonal2(x, y, color)

    def update_length(self, x:int, y:int, color:int):
        for i in range(1, x):
            if self.is_the_point_has_same_color(x-i, y, color):
                self.board[x-i:x,y]= color
                break
            elif self.is_the_point_has_0(x-i, y):
                break

        for i in range(1, Size.board-x):
            if self.is_the_point_has_same_color(x+i, y, color):
                self.board[x:x+i,y]= color
                break
            elif self.is_the_point_has_0(x+i, y):
                break

    def update_width(self, x:int, y:int, color:int):
        for i in range(1, y):
            if self.is_the_point_has_same_color(x, y-i, color):
                self.board[x,y-i:y]= color
                break
            elif self.is_the_point_has_0(x, y-i):
                break                 

        for i in range(1, Size.board-y):
            if self.is_the_point_has_same_color(x, y+i, color):
                self.board[x,y:y+i] = color
                break
            elif self.is_the_point_has_0(x, y+i):
                break

    def update_diagonal1(self, x:int, y:int, color:int):
        for i in range(1, min(x,y)+1):
            if (x-i < Position.wall_limit_low)|(y-i < Position.wall_limit_low):
                break

            if self.is_the_point_has_same_color(x-i, y-i, color):
                for c in range(i):
                    self.board[x-c,y-c] = color
                break
            elif self.is_the_point_has_0(x-i, y-i):
                break

        for i in range(1, min(Size.board-x,Size.board-y)+1):
            if (x+i > Position.wall_limit_high)|(y+i > Position.wall_limit_high):
                break

            if self.is_the_point_has_same_color(x+i, y+i, color):
                for c in range(i):
                    self.board[x+c,y+c] = color
                break
            elif self.is_the_point_has_0(x+i, y+i):
                break

    def update_diagonal2(self, x:int, y:int, color:int):
        for i in range(1, min(Size.board-x,y)+1):
            if (x+i > Position.wall_limit_high)|(y-i < Position.wall_limit_low):
                break

            if self.is_the_point_has_same_color(x+i, y-i, color):
                for c in range(i):
                    self.board[x+c,y-c] = color
                break
            elif self.is_the_point_has_0(x+i, y-i):
                break

        for i in range(1, min(x,9-y)+1):
            if (x-i < Position.wall_limit_low)|(y+i > Position.wall_limit_high):
                break

            if self.is_the_point_has_same_color(x-i, y+i, color):
                for c in range(i):
                    self.board[x-c,y+c] = color
                break
            elif self.is_the_point_has_0(x-i, y+i):
                break

    def is_the_point_has_0(self, x_i:int, y_i:int):
        return self.board[x_i,y_i] == 0

    def is_the_point_has_same_color(self, x_i, y_i, color):
        return self.board[x_i,y_i] == color

    def get_available_list(self, color:int):
        self.available_list= []

        for y in range(1, Size.board):
            for x in range(1, Size.board):

                if (self.is_the_point_has_0(x, y))&(self.is_frip_over(x, y, color)):
                    self.available_list.append((x, y))

        return self.available_list

    def is_frip_over(self, x:int, y:int, color:int):
        board_before_update = self.board.copy()
        self.update_board(x, y, color)

        if  self.is_update_board(board_before_update):
            self.board = board_before_update 
            return True
        else:
            self.board = board_before_update 
            return False

    def is_update_board(self, board_before_update:np.array((9,9))):
        return abs((self.board-board_before_update).sum()) != 1

    def check_frip_over(self, x:int, y:int, color:int):
        if self.is_frip_over(x, y, color) == False:
            raise ValueError('そこには置けないよ！')

    def check_already_put(self, x:int, y:int):
        if self.board[x,y] != 0:
            raise ValueError('もう置かれてる！')

    def is_put(self, x:int, y:int, color:int):

        self.check_already_put(x, y)
        self.check_flip_over(x, y, color)