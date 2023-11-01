import numpy as np
import matplotlib.pyplot as plt
import random

class ReversiBoard():
<<<<<<< Updated upstream
=======

    SQUARE_SIZE = 80
    HALF_SQUARE_SIZE = 40
    BOARD_SIZE = 9
    BOARD_ON_SQUARE_SIZE = 720
    STONE_RADIUS_SIZE = 30
    AVAILABLE_POINT_RADIUS_SIZE = 10
  
>>>>>>> Stashed changes
    def __init__(self):
       
        self.board=np.zeros((9,9))
        self.board[4,4] = 1
        self.board[5,5] = 1
        self.board[4,5] = -1
        self.board[5,4] = -1

        self.available_list = []
        self.i_show_board_splitting_function = 0

        self.ax = None
        self.size_square = 80
        self.board_size = 9

<<<<<<< Updated upstream
    def show_board(self, color=1):
=======
       
    @property
    def get_numpy_board(self):
        numpy_board = np.zeros((self.BOARD_SIZE,self.BOARD_SIZE))

        for x  in range(self.BOARD_SIZE):
            for y  in range(self.BOARD_SIZE):
                if self.board[x][y].color!=0:
                    numpy_board[x,y] = self.board[x][y].color

        return numpy_board

    @property
    def get_numpy_avail_list(self):
        numpy_list = []

        for x  in range(self.BOARD_SIZE):
            for y  in range(self.BOARD_SIZE):

                for a in self.available_list:
   
                  if Point(x,y,a.color)==a:
                     numpy_list.append((x,y))


        return numpy_list

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
>>>>>>> Stashed changes
        self._make_baseboard
        self._put_stones_and_available_points

        plt.xlim(0, 720)
        plt.ylim(0, 720)
        self.ax.set_aspect('equal', adjustable='box')
        plt.axis("off")
        plt.show()

    @property
    def _make_baseboard(self):
        self.i_show_board_splitting_function = 0
        _, self.ax = plt.subplots()
        for y in range(self.board_size):
            for x in range(self.board_size):
                self.write_on_board(x, y)
            
    def write_on_board(self, x, y):
        y_ = y*self.size_square
        x_ = x*self.size_square
        if (x==0)|(y==8):
            self._write_number(x_, y_)
        else:
            self._write_green_back(x_, y_)

    def _write_number(self, x_, y_):
        if self.i_show_board_splitting_function == 8:
            point = None
            self.i_show_board_splitting_function += 1
        else:
            point = abs(8-self.i_show_board_splitting_function)
            self.i_show_board_splitting_function += 1
        self.ax.text(x_+self.size_square/2, y_+self.size_square/2, point, ha = "center", va = "center", fontsize = 10)

    def _write_green_back(self, x_, y_):
        rectangle = plt.Rectangle((x_, y_), self.size_square, self.size_square, edgecolor= "black", facecolor= "green")
        self.ax.add_patch(rectangle)

    @property
    def _put_stones_and_available_points(self):
        for x in range(9):
            for y in range(9):
                self.put_stone(x, y)
                self.put_available_point(x, y)

    def put_stone(self, x, y):
        if int(self.board[x][y])== 1:
            circle = plt.Circle((x*80+40, 680-y*80), 30, edgecolor= "black", facecolor= "black")
            self.ax.add_patch(circle)
        elif int(self.board[x][y])== -1:
            circle = plt.Circle((x*80+40, 680-y*80), 30, edgecolor= "black", facecolor= "white")
            self.ax.add_patch(circle)

    def put_available_point(self, x, y):
        if (x,y) in self.available_list:
            circle = plt.Circle((x*80+40, 680-y*80), 10, edgecolor= "white", facecolor= "white")
            self.ax.add_patch(circle)

    def update_board(self, x, y, color):
        self.board[x,y]= color
        self.update_length(x, y, color)
        self.update_width(x, y, color)
        self.update_diagonal1(x, y, color)
        self.update_diagonal2(x, y, color)

    def update_length(self, x, y, color):
        for i in range(1,x):
            if self.board[x-i,y]== color:
                self.board[x-i:x,y]= color
                break
<<<<<<< Updated upstream
            elif self.board[x-i,y]== 0:
                break

        for i in range(1,9-x):
            if self.board[x+i,y]== color:
                self.board[x:x+i,y]= color
                break
            elif self.board[x+i,y]== 0:
                break

    def update_width(self, x, y, color):
        for i in range(1,y):
            if self.board[x,y-i]== color:
                self.board[x,y-i:y]= color
                break
            elif self.board[x,y-i]== 0:
                break                 

        for i in range(1,9-y):
            if self.board[x,y+i]== color:
                self.board[x,y:y+i]= color
                break
            elif self.board[x,y+i]== 0:
                break

    def update_diagonal1(self, x, y, color):
        for i in range(1, min(x,y)+1):
            if (x-i < 1)|(y-i < 1):
                break
            if self.board[x-i,y-i]== color:
                for c in range(i):
                    self.board[x-c,y-c]= color
                break
            elif self.board[x-i,y-i]== 0:
                break

        for i in range(1, min(9-x,9-y)+1):
            if (x+i > 8)|(y+i > 8):
                break
            if self.board[x+i,y+i]== color:
=======
            """
            if (self.is_top_color_same(point, i))&(i > 1):
                for c in range(1,i):
                        self.board[point.x][point.y+c].color = point.color
                        self.frip_num += 1

            """
            #複雑かも
            #何個違う色があるのかを数える関数を作成
            #for文は中身でやるべき
            if self.is_top_color_same(point, i):
>>>>>>> Stashed changes
                for c in range(i):
                    self.board[x+c,y+c]= color
                break
            elif self.board[x+i,y+i]== 0:
                break

    def update_diagonal2(self, x, y, color):

        for i in range(1, min(9-x,y)+1):
            if (x+i > 8)|(y-i < 1):
                break
            if self.board[x+i,y-i]== color:
                for c in range(i):
                    self.board[x+c,y-c]= color
                break
            elif self.board[x+i,y-i]== 0:
                break

        for i in range(1, min(x,9-y)+1):
            if (x-i < 1)|(y+i > 8):
                break
            if self.board[x-i,y+i]== color:
                for c in range(i):
                    self.board[x-c,y+c]= color
                break
            elif self.board[x-i,y+i]== 0:
                break


<<<<<<< Updated upstream
    def get_available_list(self, color):
        self.available_list= []
=======
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
                    if not self.is_top_left_color_same(point, c):
                        self.board[point.x-c][point.y+c].color = point.color
                        self.frip_num += 1

                break
            elif self.is_top_left_point_0(point,i):
                break

    def get_available_list(self, color:int):
        self.available_list= []
        #print('init')
>>>>>>> Stashed changes

        for y in range(1,9):
            for x in range(1,9):
                if self.board[x,y]== 0:

<<<<<<< Updated upstream
                    if self.is_frip_over(x, y, color)== False:
                        self.available_list.append((x, y))

        return self.available_list

    def is_frip_over(self, x, y, color):
        board_p= self.board.copy()
        self.update_board(x, y, color)

        if abs((self.board-board_p).sum())== 1:
            self.board= board_p
            return True
        else:
            self.board= board_p
=======
                if (self.is_point_0(x,y))&(self.is_frip_over(Point(x, y, color))):

                    self.available_list.append(self.board[x][y])

        return self.available_list


    def is_frip_over(self, point: Point):
        board_before_update = copy.deepcopy(self.board)
        
        self.update_board(point)
        self.board = board_before_update 

        if  self.is_update_board:
            return True
        else:
>>>>>>> Stashed changes
            return False

    def check_frip_over(self, x, y, color):
        if self.is_frip_over(x, y, color):
            raise ValueError('そこには置けないよ！')

    def check_already_put(self, x, y):
        if self.board[x,y]!= 0:
            raise ValueError('もう置かれてる！')

    def is_put(self,x,y,color):

<<<<<<< Updated upstream
        self.is_already_put(x, y)
        self.is_flip_over(x, y, color)
=======
        self.check_already_put(point)
        self.check_flip_over(point)

    def get_point(self, point: Point) -> Point:
        return self.board[point.x][point.y]

    #0ってなによ→Noneみたいな
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
>>>>>>> Stashed changes
