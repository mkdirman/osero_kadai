import numpy as np
import matplotlib.pyplot as plt
import random
from models.point import Point

class StoneColor():
    black = 1
    white = -1

class ReversiBoard():

    SIZE_SQUARE = 80
    SIZE_HALF_SQUARE = 40
    SIZE_BOARD = 9
    SIZE_BOARD_ON_SQUARE_SIZE = 720
    SIZE_STONE_RADIUS = 30
    SIZE_AVAILABLE_POINT_RADIUS = 10

    def __init__(self):

        #二度手間?
        self.board = np.zeros((self.SIZE_BOARD, self.SIZE_BOARD))
        self.board = Point.input_board_init(self.board)

        self.available_list = []
        self.i_show_board_splitting_function = 0

        self.ax = None

    def convert_size_to_square(self, point: Point):
        return point.x*self.SIZE_SQUARE, point.y*self.SIZE_SQUARE

    def convert_size_to_put_points(self, point: Point):
        return point.x*self.SIZE_SQUARE+self.SIZE_HALF_SQUARE, (self.SIZE_BOARD_ON_SQUARE_SIZE-point.y*self.SIZE_SQUARE)-self.SIZE_HALF_SQUARE

    def show_board(self, color = 1):
        self._make_baseboard
        self._put_stones_and_available_points

        plt.xlim(0, self.SIZE_BOARD_ON_SQUARE_SIZE)
        plt.ylim(0, self.SIZE_BOARD_ON_SQUARE_SIZE)
        self.ax.set_aspect('equal', adjustable='box')
        plt.axis("off")
        plt.show()

    @property
    def _make_baseboard(self):
        self.i_show_board_splitting_function = 0
        _, self.ax = plt.subplots()
        for y in range(self.SIZE_BOARD):
            for x in range(self.SIZE_BOARD):
                self.write_on_board(Point(x, y))
           
    def write_on_board(self, point: Point):
        x_on_square, y_on_square = self.convert_size_to_square(point)

        if (point.x == point.ROW_NUM)|(point.y == point.COLUMN_NUM ):
            self._write_number(x_on_square, y_on_square)
        else:
            self._write_green_back(x_on_square, y_on_square)

    def _write_number(self, x_on_square:int, y_on_square:int):
        if self.i_show_board_splitting_function == 8:
            point = None
            self.i_show_board_splitting_function += 1
        else:
            point = abs(8-self.i_show_board_splitting_function)
            self.i_show_board_splitting_function += 1

        self.ax.text(x_on_square+self.SIZE_HALF_SQUARE, y_on_square+self.SIZE_HALF_SQUARE, point, ha = "center", va = "center", fontsize = 10)

    def _write_green_back(self,  x_on_square:int, y_on_square:int):
        rectangle = plt.Rectangle((x__on_square, y__on_square), self.SIZE_SQUARE, self.SIZE_SQUARE, edgecolor= "black", facecolor= "green")
        self.ax.add_patch(rectangle)

    @property
    def _put_stones_and_available_points(self):
        for x in range(1,self.SIZE_BOARD):
            for y in range(1,self.SIZE_BOARD):
                self.put_stone(Point(x, y))
                self.put_available_point(Point(x, y))

    def put_stone(self, point: Point):
        x_stone, y_stone = self.convert_size_to_put_points(point)

        if int(self.board[point.x][point.y]) == StoneColor.black:
            circle = plt.Circle((x_stone, y_stone), self.SIZE_STONE_RADIUS, edgecolor= "black", facecolor= "black")
            self.ax.add_patch(circle)
        elif int(self.board[point.x][point.y]) == StoneColor.white:
            circle = plt.Circle((x_stone, y_stone), self.SIZE_STONE_RADIUS, edgecolor= "black", facecolor= "white")
            self.ax.add_patch(circle)

    def put_available_point(self, point: Point):
  
        x_on_spuare_size, y_on_spuare_size = self.convert_size_to_put_points(point)
    
        if self.is_in_available_list(point):
            circle = plt.Circle((x_on_spuare_size, y_on_spuare_size), self.SIZE_AVAILABLE_POINT_RADIUS, edgecolor= "white", facecolor= "white")
            self.ax.add_patch(circle)

    def is_in_available_list(self, point: Point):
        for point_available in self.available_list:
            if (point_available.x == point.x)&(point_available.y == point.y):
                return True
        return False

    def update_board(self, point: Point):

        self.board[point.x,point.y] = point.color
        self.update_length(point)
        self.update_width(point)
        self.update_diagonal1(point)
        self.update_diagonal2(point)

    def update_length(self, point: Point):
        
        for i in range(1, point.x):
            if self.is_the_point_has_same_color(Point(point.x-i, point.y, point.color)):
                self.board[point.x-i:point.x,point.y]= point.color
                break
            elif self.is_the_point_has_0(Point(point.x-i, point.y)):
                break

        for i in range(1, self.SIZE_BOARD-point.x):
            if self.is_the_point_has_same_color(Point(point.x+i, point.y, point.color)):
                self.board[point.x:point.x+i,point.y] = point.color
                break
            elif self.is_the_point_has_0(Point(point.x+i, point.y)):
                break
          
    def update_width(self, point: Point):
        for i in range(1, point.y):
            if self.is_the_point_has_same_color(Point(point.x, point.y-i, point.color)):
                self.board[point.x, point.y-i:point.y] = point.color
                break
            elif self.is_the_point_has_0(Point(point.x, point.y-i)):
                break                 

        for i in range(1, self.SIZE_BOARD-point.y):
            if self.is_the_point_has_same_color(Point(point.x, point.y+i, point.color)):
                self.board[point.x, point.y:point.y+i] = point.color
                break
            elif self.is_the_point_has_0(Point(point.x, point.y+i)):
                break

    def update_diagonal1(self, point: Point):
        for i in range(1, min(point.x,point.y)+1):
            if (point.x-i < Point.WALL_LIMIT_LOW)|(point.y-i < Point.WALL_LIMIT_HIGH):
                break

            if self.is_the_point_has_same_color(point.x-i, point.y-i, point.color):
                for c in range(i):
                    self.board[point.x-c,point.y-c] = point.color
                break
            elif self.is_the_point_has_0(Point(point.x-i, point.y-i)):
                break

        for i in range(1, min(self.SIZE_BOARD-point.x,self.SIZE_BOARD-point.y)+1):
            if (point.x+i > Point.WALL_LIMIT_HIGH)|(point.y+i > Point.WALL_LIMIT_HIGH):
                break

            if self.is_the_point_has_same_color(Point(point.x+i, point.y+i, point.color)):
                for c in range(i):
                    self.board[point.x+c,point.y+c] = point.color
                break
            elif self.is_the_point_has_0(Point(point.x+i, point.y+i)):
                break

    def update_diagonal2(self, point: Point):
        for i in range(1, min(self.SIZE_BOARD-point.x,point.y)+1):

            if (point.x+i > Point.WALL_LIMIT_HIGH)|(point.y-i < Point.WALL_LIMIT_LOW):
                break

            if self.is_the_point_has_same_color(Point(point.x+i, point.y-i, point.color)):
                for c in range(i):
                    self.board[point.x+c, point.y-c] = point.color
                break
            elif self.is_the_point_has_0(Point(point.x+i, point.y-i)):
                break

        for i in range(1, min(point.x,9-point.y)+1):
            if (point.x-i < Point.WALL_LIMIT_LOW)|(point.y+i > Point.WALL_LIMIT_HIGH):
                break

            if self.is_the_point_has_same_color(Point(point.x-i, point.y+i, point.color)):
                for c in range(i):
                    self.board[point.x-c,point.y+c] = point.color
                break
            elif self.is_the_point_has_0(Point(point.x-i, point.y+i)):
                break

    def is_the_point_has_0(self, point: Point):
        return self.board[point.x, point.y] == 0

    def is_the_point_has_same_color(self, point: Point):
        return self.board[point.x, point.y] == point.color

    def get_available_list(self, color:int):
        self.available_list= []

        for y in range(1, self.SIZE_BOARD):
            for x in range(1, self.SIZE_BOARD):

                if (self.is_the_point_has_0(Point(x, y)))&(self.is_frip_over(Point(x, y, color))):

                    self.available_list.append(Point(x, y))

        return self.available_list

    def is_frip_over(self, point: Point):
        board_before_update = self.board.copy()
        self.update_board(point)

        if  self.is_update_board(board_before_update):
            self.board = board_before_update 
            return True
        else:
            self.board = board_before_update 
            return False

    def is_update_board(self, board_before_update: np.array((9,9))):
        return abs((self.board-board_before_update).sum()) != 1

    def check_frip_over(self, point: Point):
        if self.is_frip_over(point) == False:
            raise ValueError('そこには置けないよ！')

    def check_already_put(self, point: Point):
        if self.board[point.x, point.y] != 0:
            raise ValueError('もう置かれてる！')

    def is_put(self, point: Point):

        self.check_already_put(point)
        self.check_flip_over(point)