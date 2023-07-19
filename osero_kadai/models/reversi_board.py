import numpy as np
import matplotlib.pyplot as plt
import random

class ReversiBoard():
    def __init__(self):
        self.board=np.zeros((9,9))
        self.board[4,4]= 1
        self.board[5,5]= 1
        self.board[4,5]= -1
        self.board[5,4]= -1
        self.available_list=[]
        self.i=0

        self.ax=None

    def show_board(self, color=1):
        self._make_baseboard
        self._put_all

        plt.xlim(0, 720)
        plt.ylim(0, 720)
        self.ax.set_aspect('equal', adjustable='box')
        plt.axis("off")
        plt.show()

    @property
    def _make_baseboard(self):
        self.i=0
        _, self.ax=plt.subplots()
        for y in range(9):
            for x in range(9):
                self.show(x, y)

    def show(self, x, y):
        y_=y*80
        x_=x*80
        if (x==0)|(y==8):
            self._show_number(x_, y_)
        else:
            self._show_point(x_, y_)


    def _show_number(self, x_, y_):
        if self.i== 8:
            point=None
            self.i+= 1
        else:
            point=abs(8-self.i)
            self.i+= 1
        self.ax.text(x_+40, y_+40, point, ha="center", va="center", fontsize=10)

    def _show_point(self, x_, y_):
        rectangle = plt.Rectangle((x_, y_), 80, 80, edgecolor="black", facecolor="green")
        self.ax.add_patch(rectangle)

    @property
    def _put_all(self):
        for x in range(9):
            for y in range(9):
                self.put_coin(x, y)
                self.put_available_point(x, y)

    def put_coin(self, x, y):
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
            elif self.board[x-i,y]== 0:
                break
            else:
                continue

        for i in range(1,9-x):
            if self.board[x+i,y]== color:
                self.board[x:x+i,y]= color
                break
            elif self.board[x+i,y]== 0:
                break
            else:
                continue

    def update_width(self, x, y, color):
        for i in range(1,y):
            if self.board[x,y-i]== color:
                self.board[x,y-i:y]= color
                break
            elif self.board[x,y-i]== 0:
                break
            else:
                continue

        for i in range(1,9-y):
            if self.board[x,y+i]== color:
                self.board[x,y:y+i]= color
                break
            elif self.board[x,y+i]== 0:
                break
            else:
                continue

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
            else:
                continue

        for i in range(1, min(9-x,9-y)+1):
            if (x+i > 8)|(y+i > 8):
                break
            if self.board[x+i,y+i]== color:
                for c in range(i):
                    self.board[x+c,y+c]= color
                break
            elif self.board[x+i,y+i]== 0:
                break
            else:
                continue

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
            else:
                continue

        for i in range(1, min(x,9-y)+1):
            if (x-i < 1)|(y+i > 8):
                break
            if self.board[x-i,y+i]== color:
                for c in range(i):
                    self.board[x-c,y+c]= color
                break
            elif self.board[x-i,y+i]== 0:
                break
            else:
                continue

    def get_available_list(self, color):
        self.available_list= []

        for y in range(1,9):
            for x in range(1,9):
                if self.board[x,y]== 0:

                    if self.judge(x, y, color)== True:
                        self.available_list.append((x, y))

        return self.available_list

    def judge(self, x, y, color):
        board_p= self.board.copy()
        self.update_board(x, y, color)

        if abs((self.board-board_p).sum())== 1:
            self.board= board_p
            return False
        else:
            self.board= board_p
            return True

    def input_judge(self, x, y, color):
        board_p= self.board.copy()
        self.update_board(x, y, color)

        if abs((self.board-board_p).sum())== 1:
            self.board= board_p
            raise ValueError('そこには置けないよ！')
        self.board= board_p

    def already_put(self, x, y):
        if self.board[x,y]!= 0:
            raise ValueError('もう置かれてる！')