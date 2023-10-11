import numpy as np
import matplotlib.pyplot as plt
import random
from models.point import Point
import copy


class StoneColor():
    black = 1
    white = -1

class ReversiBoard():

    SQUARE_SIZE = 80
    HALF_SQUARE_SIZE = 40
    BOARD_SIZE = 9
    BOARD_ON_SQUARE_SIZE = 720
    STONE_RADIUS_SIZE = 30
    AVAILABLE_POINT_RADIUS_SIZE = 10

    def __init__(self):
        self.board = self.make_board_

        self.board[4][4] = Point(4, 4, 1)
        self.board[5][5] = Point(5, 5, 1)
        self.board[4][5] = Point(4, 5, -1)
        self.board[5][4] = Point(5, 4, -1)

        self.available_list = []
        self.i_show_board_splitting_function = 0
        self.frip_num = 0

        self.ax = None

    @property
    def make_board_(self):
        board = []
        for x in range(self.BOARD_SIZE):
            board_row = []
            for y in range(self.BOARD_SIZE):
                board_row.append(Point(x,y,0))
            board.append(board_row)
        return board

    def convert_size_to_square(self, point: Point):
        return point.x*self.SQUARE_SIZE, point.y*self.SQUARE_SIZE

    def convert_size_to_put_points(self, point: Point):
        return point.x*self.SQUARE_SIZE+self.HALF_SQUARE_SIZE, (self.BOARD_ON_SQUARE_SIZE-point.y*self.SQUARE_SIZE)-self.HALF_SQUARE_SIZE

    def show_board(self, color = 1):
        self._make_baseboard
        self._put_stones_and_available_points

        plt.xlim(0, self.BOARD_ON_SQUARE_SIZE)
        plt.ylim(0, self.BOARD_ON_SQUARE_SIZE)
        self.ax.set_aspect('equal', adjustable='box')
        plt.axis("off")
        plt.show()

    @property
    def _make_baseboard(self):
        self.i_show_board_splitting_function = 0
        _, self.ax = plt.subplots()
        for y in range(self.BOARD_SIZE):
            for x in range(self.BOARD_SIZE):
                self.write_on_board(Point(x,y))
           
    def write_on_board(self, point: Point):
        x_on_square, y_on_square = self.convert_size_to_square(point)

        if (point.x == point.ROW_NUM)|(point.y == point.COLUMN_NUM ):
            self._write_number(x_on_square, y_on_square)
        else:
            self._write_green_back(x_on_square, y_on_square)

    def _write_number(self, x_on_square:int, y_on_square:int):
        if self.i_show_board_splitting_function ==  Point.WALL_LIMIT_HIGH:
            point = None
            self.i_show_board_splitting_function += 1
        else:
            point = abs(8-self.i_show_board_splitting_function)
            self.i_show_board_splitting_function += 1

        self.ax.text(x_on_square+self.HALF_SQUARE_SIZE, y_on_square+self.HALF_SQUARE_SIZE, point, ha = "center", va = "center", fontsize = 10)

    def _write_green_back(self, x_on_square:int, y_on_square:int):
        rectangle = plt.Rectangle((x_on_square, y_on_square), self.SQUARE_SIZE, self.SQUARE_SIZE, edgecolor= "black", facecolor= "green")
        self.ax.add_patch(rectangle)

    @property
    def _put_stones_and_available_points(self):
        for x in range(1,self.BOARD_SIZE):
            for y in range(1,self.BOARD_SIZE):
                self.put_stone(self.board[x][y])
                self.put_available_point(self.board[x][y])

    def put_stone(self, point: Point):
        x_stone, y_stone = self.convert_size_to_put_points(point)

        if int(self.get_point(point).color) == StoneColor.black:
            circle = plt.Circle((x_stone, y_stone), self.STONE_RADIUS_SIZE, edgecolor= "black", facecolor= "black")
            self.ax.add_patch(circle)
        elif int(self.get_point(point).color) == StoneColor.white:
            circle = plt.Circle((x_stone, y_stone), self.STONE_RADIUS_SIZE, edgecolor= "black", facecolor= "white")
            self.ax.add_patch(circle)

    def put_available_point(self, point: Point):
  
        x_on_spuare_size, y_on_spuare_size = self.convert_size_to_put_points(point)
    
        if self.is_in_available_list(point):
            circle = plt.Circle((x_on_spuare_size, y_on_spuare_size), self.AVAILABLE_POINT_RADIUS_SIZE, edgecolor= "white", facecolor= "white")
            self.ax.add_patch(circle)

    def is_in_available_list(self, point: Point):
        for point_available in self.available_list:
            if (point_available.x == point.x)&(point_available.y == point.y):
                return True
        return False

    def update_board(self, point: Point):
        self.frip_num = 0

        self.board[point.x][point.y] = point
        self.update_length(point)
        self.update_width(point)
        self.update_diagonal1(point)
        self.update_diagonal2(point)
         
    #同じ色なら同じ色を入れていくので、動作をそのままself.numで数えるのは不可
    #→違う色の時だけcolorを入れ替える動作を行う
    #if not self.is_right_color_same(point, c)ではなく、if self.is_right_color_different(point, c)を新しく作るべきか

    def update_length(self, point: Point):

        for i in range(1, point.x):
            if (point.y+i > Point.WALL_LIMIT_HIGH):
                break
            """
            if (self.is_top_color_same(point, i))&(i > 1):
                for c in range(i):
                        self.board[point.x][point.y+c].color = point.color
                self.frip_num += i-1

            """
            #複雑かも
            if self.is_top_color_same(point, i):
                for c in range(i):
                    if not self.is_top_color_same(point, c):
                        self.board[point.x][point.y+c].color = point.color
                        self.frip_num += 1

                break
            elif self.is_top_point_0(point,i):
                break

        for i in range(1, self.BOARD_SIZE-point.x):
            if (point.y-i < Point.WALL_LIMIT_LOW):
                break

            if self.is_bottom_color_same(point, i):
                for c in range(i):
                    if not self.is_bottom_color_same(point, c):
                        self.board[point.x][point.y-c].color = point.color
                        self.frip_num += 1

                break
            elif self.is_bottom_point_0(point, i):
                break

    def update_width(self, point: Point):
        for i in range(1, point.y):
            if (point.x+i > Point.WALL_LIMIT_HIGH):
                break

            if self.is_right_color_same(point, i):
                for c in range(i):
                    if not self.is_right_color_same(point, c):
                        self.board[point.x+c][point.y].color = point.color
                        self.frip_num += 1

                break
            elif self.is_right_point_0(point, i):
                break               

        for i in range(1, self.BOARD_SIZE-point.y):
            if (point.x-i < Point.WALL_LIMIT_LOW):
                break
            if self.is_left_color_same(point, i):
                for c in range(i):
                    if not self.is_left_color_same(point, c):
                        self.board[point.x-c][point.y].color = point.color
                        self.frip_num += 1

                break
            elif self.is_left_point_0(point, i):
                break

    def update_diagonal1(self, point: Point):
        for i in range(1, min(point.x,point.y)+1):
            if (point.x-i < Point.WALL_LIMIT_LOW)|(point.y-i < Point.WALL_LIMIT_HIGH):
                break

            if self.is_bottom_left_color_same(point, i):
                for c in range(i):
                    if not self.is_bottom_left_color_same(point, c):
                        self.board[point.x-c][point.y-c].color = point.color
                        self.frip_num += 1

                break
            elif self.is_bottom_left_point_0(point, i):
                break

        for i in range(1, min(self.BOARD_SIZE-point.x,self.BOARD_SIZE-point.y)+1):
            if (point.x+i > Point.WALL_LIMIT_HIGH)|(point.y+i > Point.WALL_LIMIT_HIGH):
                break

            if self.is_top_right_color_same(point, i):
                for c in range(i):
                    if not self.is_top_right_color_same(point, c):
                        self.board[point.x+c][point.y+c].color = point.color
                        self.frip_num += 1

                break
            elif self.is_top_right_point_0(point, i):
                break

    def update_diagonal2(self, point: Point):
        for i in range(1, min(self.BOARD_SIZE-point.x,point.y)+1):
            if (point.x+i > Point.WALL_LIMIT_HIGH)|(point.y-i < Point.WALL_LIMIT_LOW):
                break

            if self.is_bottom_right_color_same(point, i):
                for c in range(i):
                    if not self.is_bottom_right_color_same(point, c):
                        self.board[point.x+c][point.y-c].color = point.color
                        self.frip_num += 1

                break
            elif self.is_bottom_right_point_0(point, i):
                break

        for i in range(1, min(point.x,9-point.y)+1):
            if (point.x-i < Point.WALL_LIMIT_LOW)|(point.y+i > Point.WALL_LIMIT_HIGH):
                break

            if self.is_top_left_color_same(point, i):
                for c in range(i):
                    if not self.is_top_right_color_same(point, c):
                        self.board[point.x-c][point.y+c].color = point.color
                        self.frip_num += 1

                break
            elif self.is_top_left_point_0(point,i):
                break

    def get_available_list(self, color:int):
        self.available_list= []
        print('init')

        for y in range(1, self.BOARD_SIZE):
            for x in range(1, self.BOARD_SIZE):

                if (self.is_point_0(x,y))&(self.is_frip_over(Point(x, y, color))):
                    print('available_list')
                    print(self.frip_num)
                    print(x,y,color)

                    self.available_list.append(self.board[x][y])

        return self.available_list

    def is_frip_over(self, point: Point):
        board_before_update = copy.deepcopy(self.board)
        
        self.update_board(point)
        if  self.is_update_board:
            self.board = board_before_update 

            return True
        else:
            self.board = board_before_update 
            return False

    @property
    def is_update_board(self):
        return self.frip_num > 0
       
    def check_frip_over(self, point: Point):
        if self.is_frip_over(point) == False:
            raise ValueError('そこには置けないよ！')

    def check_already_put(self, point: Point):
        if self.get_point(point).color != 0:
            raise ValueError('もう置かれてる！')

    def is_put(self, point: Point):

        self.check_already_put(point)
        self.check_flip_over(point)

    def get_point(self, point: Point) -> Point:
        return self.board[point.x][point.y]

    def is_point_0(self, x, y) -> bool:
        return self.get_point(Point(x, y)).is_0


    def is_left_color_same(self, base_point:Point, i) -> bool:
        return base_point.is_same_color(self.get_left_point(base_point, i))
    def is_right_color_same(self, base_point:Point, i)->  bool:
        return base_point.is_same_color(self.get_right_point(base_point, i))
    def is_top_color_same(self, base_point:Point, i) -> bool:
        return base_point.is_same_color(self.get_top_point(base_point, i))
    def is_bottom_color_same(self, base_point, i) -> bool:
        return base_point.is_same_color(self.get_bottom_point(base_point, i))
    def is_top_left_color_same(self, base_point:Point, i) -> bool:
        return base_point.is_same_color(self.get_top_left_point(base_point, i))
    def is_top_right_color_same(self, base_point:Point, i) -> bool:
        return base_point.is_same_color(self.get_top_right_point(base_point, i))
    def is_bottom_left_color_same(self, base_point:Point, i) -> bool:
        return base_point.is_same_color(self.get_bottom_left_point(base_point, i))
    def is_bottom_right_color_same(self, base_point:Point, i) -> bool:
        return base_point.is_same_color(self.get_bottom_right_point(base_point, i))
 

    def is_right_point_0(self, base_point, i) -> Point:
        p = self.get_right_point(base_point, i)
        return p.is_0
    def is_left_point_0(self, base_point, i) -> Point:
        p = self.get_left_point(base_point, i)
        return p.is_0
    def is_top_point_0(self, base_point, i) -> Point:
        p = self.get_top_point(base_point, i)
        return p.is_0
    def is_bottom_point_0(self, base_point, i) -> Point:
        p = self.get_bottom_point(base_point, i)
        return p.is_0
    def is_top_right_point_0(self, base_point, i) -> Point:
        p = self.get_top_right_point(base_point, i)
        return p.is_0
    def is_bottom_right_point_0(self, base_point, i) -> Point:
        p = self.get_bottom_right_point(base_point, i)
        return p.is_0
    def is_top_left_point_0(self, base_point, i) -> Point:
        p = self.get_top_left_point(base_point,i)
        return p.is_0
    def is_bottom_left_point_0(self, base_point, i) -> Point:
        p = self.get_bottom_left_point(base_point, i)
        return p.is_0


    def get_top_point(self, base_point, i) -> Point:
        p = base_point.get_top_point(i)
        return self.get_point(p)
    def get_right_point(self, base_point, i) -> Point:
        p = base_point.get_right_point(i)
        return self.get_point(p)
    def get_left_point(self, base_point, i) -> Point:
        p = base_point.get_left_point(i)
        return self.get_point(p)
    def get_bottom_point(self, base_point, i) -> Point:
        p = base_point.get_bottom_point(i)
        return self.get_point(p)
    def get_top_left_point(self, base_point, i) -> Point:
        p = base_point.get_top_left_point(i)
        return self.get_point(p)
    def get_bottom_right_point(self, base_point, i) -> Point:
        p = base_point.get_bottom_right_point(i)
        return self.get_point(p)
    def get_top_right_point(self, base_point, i) -> Point:
        p = base_point.get_top_right_point(i)
        return self.get_point(p)
    def get_bottom_right_point(self, base_point, i) -> Point:
        p = base_point.get_bottom_right_point(i)
        return self.get_point(p)