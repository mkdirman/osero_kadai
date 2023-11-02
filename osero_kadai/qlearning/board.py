import numpy as np
import matplotlib.pyplot as plt
import random

class ReversiBoard():
    BOARD_SIZE =  4
    INIT_POINT = int(4/2)-1
    def __init__(self, board_data=None):
       
        self.board=np.zeros((self.BOARD_SIZE, self.BOARD_SIZE))
        self.board[self.INIT_POINT,self.INIT_POINT]= 1
        self.board[self.INIT_POINT+1,self.INIT_POINT+1]= 1
        self.board[self.INIT_POINT,self.INIT_POINT+1]= -1
        self.board[self.INIT_POINT+1,self.INIT_POINT]= -1

        if board_data is not None :
            self.board = board_data

        self.available_list=[]
        self.i_show_board_splitting_function=0

        self.ax=None
        self.black_score = 0
        self.white_score = 0

  
    def update_board(self, move, color):
        x = move[0]
        y = move[1]
        self.board[x,y]= color
        self._update_length(x, y, color)
        self._update_width(x, y, color)
        self._update_diagonal1(x, y, color)
        self._update_diagonal2(x, y, color)

    def _update_length(self, x, y, color):
        for i in range(1,x):
            if self.board[x-i,y]== color:
                self.board[x-i:x,y]= color
                break
            elif self.board[x-i,y]== 0:
                break

        for i in range(1,self.BOARD_SIZE-x):
            if self.board[x+i,y]== color:
                self.board[x:x+i,y]= color
                break
            elif self.board[x+i,y]== 0:
                break

    def _update_width(self, x, y, color):
        for i in range(1,y):
            if self.board[x,y-i]== color:
                self.board[x,y-i:y]= color
                break
            elif self.board[x,y-i]== 0:
                break                 

        for i in range(1,self.BOARD_SIZE-y):
            if self.board[x,y+i]== color:
                self.board[x,y:y+i]= color
                break
            elif self.board[x,y+i]== 0:
                break

    def _update_diagonal1(self, x, y, color):
        for i in range(1, min(x,y)+1):
            if (x-i < 0)|(y-i < 0):
                break
            if self.board[x-i,y-i]== color:
                for c in range(i):
                    self.board[x-c,y-c]= color
                break
            elif self.board[x-i,y-i]== 0:
                break

        for i in range(1, min(self.BOARD_SIZE-x,self.BOARD_SIZE-y)+1):
            if (x+i > self.BOARD_SIZE-1)|(y+i >= self.BOARD_SIZE-1):
                break
            if self.board[x+i,y+i]== color:
                for c in range(i):
                    self.board[x+c,y+c]= color
                break
            elif self.board[x+i,y+i]== 0:
                break

    def _update_diagonal2(self, x, y, color):

        for i in range(1, min(self.BOARD_SIZE-x,y)+1):
            if (x+i > self.BOARD_SIZE-1)|(y-i < 0):
                break
            if self.board[x+i,y-i]== color:
                for c in range(i):
                    self.board[x+c,y-c]= color
                break
            elif self.board[x+i,y-i]== 0:
                break

        for i in range(1, min(x,self.BOARD_SIZE-y)+1):
            if (x-i < 0)|(y+i > self.BOARD_SIZE-1):
                break
            if self.board[x-i,y+i]== color:
                for c in range(i):
                    self.board[x-c,y+c]= color
                break
            elif self.board[x-i,y+i]== 0:
                break


    def get_available_list(self, color) -> list:
        self.available_list= []

        for y in range(0,self.BOARD_SIZE):
            for x in range(0,self.BOARD_SIZE):

                if self.board[x,y]== 0:

                    if self.is_frip_over(x, y, color)== False:
                        self.available_list.append((x, y))

        return self.available_list

    @property
    def get(self):
        return self.board

    @property
    def get_win_color(self) -> int:
        self.count_stone
        if self.black_score > self.white_score:
            return 1
        elif self.black_score < self.white_score:
            return -1
        elif self.black_score == self.white_score:
            return 0

    def get_next(self,move,color):
        
        self.update_board(move, color)

        return self.board

    def is_frip_over(self, x, y, color):
        move = (x,y)
        board_p= self.board.copy()
        self.update_board(move, color)

        if abs((self.board-board_p).sum())== 1:
            self.board= board_p
            return True
        else:
            self.board= board_p
            return False

    @property
    def is_game_over(self):
        if (self.get_available_list(1) == [])&(self.get_available_list(-1) == []):
            return True
        else:
            return False

    @property
    def count_stone(self):
        self.black_score = np.sum(self.board == 1)
        self.white_score = np.sum(self.board == -1)
