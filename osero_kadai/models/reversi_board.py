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

    def convert_size_to_square(self, x: int ,y: int):
        return x*self.SIZE_SQUARE, y*self.SIZE_SQUARE

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
                self.write_on_board(x, y)
           
    def write_on_board(self, x:int, y: int):
        """

        def convert_size_to_square(point, Point):
            return point.x*SIZE_SQUARE,point.y**SIZE_SQUARE

        #Point(x, y)でやるとPointの__init__の部分でrow_number,column_numberをはじいてしまう
        y_on_square,x_on_square = self.convert_to_square(Point(x, y))

        """

        x_on_square, y_on_square = self.convert_size_to_square(x,y)

        if (x == Point.ROW_NUM)|(y == Point.COLUMN_NUM):
            self._write_number(x_on_square, y_on_square)
        else:
            self._write_green_back(x_on_square, y_on_square)

    def _write_number(self, x_:int, y_:int):
        if self.i_show_board_splitting_function == 8:
            point = None
            self.i_show_board_splitting_function += 1
        else:
            point = abs(8-self.i_show_board_splitting_function)
            self.i_show_board_splitting_function += 1

        self.ax.text(x_+self.SIZE_HALF_SQUARE, y_+self.SIZE_HALF_SQUARE, point, ha = "center", va = "center", fontsize = 10)

    def _write_green_back(self, x_:int, y_:int):
        rectangle = plt.Rectangle((x_, y_), self.SIZE_SQUARE, self.SIZE_SQUARE, edgecolor= "black", facecolor= "green")
        self.ax.add_patch(rectangle)

    @property
    def _put_stones_and_available_points(self):
        for x in range(1,self.SIZE_BOARD):
            for y in range(1,self.SIZE_BOARD):
                self.put_stone(Point(x, y))
                self.put_available_point(Point(x, y))

    def put_stone(self, point:Point):
        x_stone, y_stone = self.convert_size_to_put_points(point)

        if int(self.board[point.x][point.y]) == StoneColor.black:
            circle = plt.Circle((x_stone, y_stone), self.SIZE_STONE_RADIUS, edgecolor= "black", facecolor= "black")
            self.ax.add_patch(circle)
        elif int(self.board[point.x][point.y]) == StoneColor.white:
            circle = plt.Circle((x_stone, y_stone), self.SIZE_STONE_RADIUS, edgecolor= "black", facecolor= "white")
            self.ax.add_patch(circle)

    def put_available_point(self, point:Point):
  
        x_on_spuare_size, y_on_spuare_size = self.convert_size_to_put_points(point)
    
        if self.is_in_available_list(point):
            circle = plt.Circle((x_on_spuare_size, y_on_spuare_size), self.SIZE_AVAILABLE_POINT_RADIUS, edgecolor= "white", facecolor= "white")
            self.ax.add_patch(circle)

    def is_in_available_list(self, point:Point):
        for point_available in self.available_list:
            if (point_available.x == point.x)&(point_available.y == point.y):
                return True
        return False

    def update_board(self, point: Point, color:int):

        self.board[point.x,point.y] = color
        self.update_length(point, color)
        self.update_width(point, color)
        self.update_diagonal1(point, color)
        self.update_diagonal2(point, color)

    def update_length(self, point: Point, color:int):
        
        for i in range(1, point.x):
            if self.is_the_point_has_same_color(Point(point.x-i, point.y), color):
                self.board[point.x-i:point.x,point.y]= color
                break
            elif self.is_the_point_has_0(Point(point.x-i, point.y)):
                break

        for i in range(1, self.SIZE_BOARD-point.x):
            if self.is_the_point_has_same_color(Point(point.x+i, point.y), color):
                self.board[point.x:point.x+i,point.y]= color
                break
            elif self.is_the_point_has_0(Point(point.x+i, point.y)):
                break

    def update_width(self, point: Point, color:int):
        for i in range(1, point.y):
            if self.is_the_point_has_same_color(Point(point.x, point.y-i), color):
                self.board[point.x, point.y-i:point.y]= color
                break
            elif self.is_the_point_has_0(Point(point.x, point.y-i)):
                break                 

        for i in range(1, self.SIZE_BOARD-point.y):
            if self.is_the_point_has_same_color(Point(point.x, point.y+i), color):
                self.board[point.x, point.y:point.y+i] = color
                break
            elif self.is_the_point_has_0(Point(point.x, point.y+i)):
                break

    def update_diagonal1(self, point:Point, color:int):
        for i in range(1, min(point.x,point.y)+1):
            if (point.x-i < Point.WALL_LIMIT_LOW)|(point.y-i < Point.WALL_LIMIT_HIGH):
                break

            if self.is_the_point_has_same_color(point.x-i, point.y-i, color):
                for c in range(i):
                    self.board[point.x-c,point.y-c] = color
                break
            elif self.is_the_point_has_0(Point(point.x-i, point.y-i)):
                break

        for i in range(1, min(self.SIZE_BOARD-point.x,self.SIZE_BOARD-point.y)+1):
            if (point.x+i > Point.WALL_LIMIT_HIGH)|(point.y+i > Point.WALL_LIMIT_HIGH):
                break

            if self.is_the_point_has_same_color(Point(point.x+i, point.y+i), color):
                for c in range(i):
                    self.board[point.x+c,point.y+c] = color
                break
            elif self.is_the_point_has_0(Point(point.x+i, point.y+i)):
                break

    def update_diagonal2(self, point:Point, color:int):
        for i in range(1, min(self.SIZE_BOARD-point.x,point.y)+1):
            #ここも
            if (point.x+i > Point.WALL_LIMIT_HIGH)|(point.y-i < Point.WALL_LIMIT_LOW):
                break

            if self.is_the_point_has_same_color(Point(point.x+i, point.y-i), color):
                for c in range(i):
                    self.board[point.x+c, point.y-c] = color
                break
            elif self.is_the_point_has_0(Point(point.x+i, point.y-i)):
                break

        for i in range(1, min(point.x,9-point.y)+1):
            #ここも
            if (point.x-i < Point.WALL_LIMIT_LOW)|(point.y+i > Point.WALL_LIMIT_HIGH):
                break

            if self.is_the_point_has_same_color(Point(point.x-i, point.y+i), color):
                for c in range(i):
                    self.board[point.x-c,point.y+c] = color
                break
            elif self.is_the_point_has_0(Point(point.x-i, point.y+i)):
                break

    def is_the_point_has_0(self, point: Point):
        return self.board[point.x, point.y] == 0

    def is_the_point_has_same_color(self, point: Point, color):
        return self.board[point.x, point.y] == color

    """
    get_available_listの機能をPointに持たせるためには、
    ・現在のboardの情報
    ・SIZE_BOARDの値
    が必要。更に、移行に必要な関数は
    ・def is_the_point_has_0(self, point: Point)
    ・def is_the_point_has_same_color(self, point: Point, color)
    ・def update_board(self, point, color)
    ・def is_frip_over(self, point: Point, color:int)
     　　↑{
            self.update_board( point, color)
            }
                ↑{
                   is_the_point_has_0(self, point: Point),
                   is_the_point_has_same_color(self, point: Point, color)
                   }
    の4つ。
    update_boardは移行するべきなのかと考えると、
    update_boardを使った引っ繰り返せるかの判断を行う限りget_available_listの移行は難しい。


    """
    def get_available_list(self, color:int):
        self.available_list= []

        for y in range(1, self.SIZE_BOARD):
            for x in range(1, self.SIZE_BOARD):

                if (self.is_the_point_has_0(Point(x, y)))&(self.is_frip_over(Point(x, y), color)):
                    
                    self.available_list.append(Point(x, y))

        return self.available_list

    def is_frip_over(self, point: Point, color:int):
        board_before_update = self.board.copy()
        self.update_board(point, color)

        if  self.is_update_board(board_before_update):
            self.board = board_before_update 
            return True
        else:
            self.board = board_before_update 
            return False

    def is_update_board(self, board_before_update:np.array((9,9))):
        return abs((self.board-board_before_update).sum()) != 1

    def check_frip_over(self, point:Point, color:int):
        if self.is_frip_over(Point(point.x, point.y), color) == False:
            raise ValueError('そこには置けないよ！')

    def check_already_put(self, point: Point):
        
        if self.board[point.x, point.y] != 0:
            raise ValueError('もう置かれてる！')

    def is_put(self, point:Point, color:int):

        self.check_already_put(point)
        self.check_flip_over(point, color)