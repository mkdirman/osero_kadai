import numpy as np
import matplotlib.pyplot as plt
import random


class reversi_board():
    def __init__(self):
        self.board=np.zeros((9,9))
        self.board[4,4]=1
        self.board[5,5]=1
        self.board[4,5]=-1
        self.board[5,4]=-1

        self.ax=None

    def initialize_board(self):
        self.__init__()

    def show_board(self,color=1):
        available_list=self.get_available_list(color)
        self.make_baseboard()
        self.put_coin(available_list)

        plt.xlim(0,720)
        plt.ylim(0,720)
        self.ax.set_aspect('equal',adjustable='box')
        plt.axis("off")
        plt.show()

    def make_baseboard(self):
        i=0
        fig,self.ax=plt.subplots()
        for y in range(9):  
            for x in range(9): 
                y_=y*80
                x_=x*80
                if (x==0)|(y==8):
                    if i==8:
                      point=None
                      i+=1
                    else:
                      point=abs(8-i)
                      i+=1
                    self.ax.text(x_+40,y_+40,point,ha="center",va="center",fontsize=10)                   
                else:
                    rectangle = plt.Rectangle((x_,y_),80,80,edgecolor="black",facecolor="green")
                    self.ax.add_patch(rectangle)

    def put_coin(self,available_list):
        for x in range(9):
            for y in range(9):
                if int(self.board[x][y])==1:
                    circle = plt.Circle((x*80+40,680-y*80),30,edgecolor="black",facecolor="black")
                    self.ax.add_patch(circle)
                elif int(self.board[x][y])==-1:
                    circle = plt.Circle((x*80+40,680-y*80),30,edgecolor="black",facecolor="white")
                    self.ax.add_patch(circle)
                elif (x,y) in available_list:
                    circle = plt.Circle((x*80+40,680-y*80),10,edgecolor="white",facecolor="white")
                    self.ax.add_patch(circle)

    def update_board(self,x,y,color):
        self.board[x,y]=color
        #縦制御
        self.update_length(x,y,color)
        #横制御
        self.update_width(x,y,color)
        #斜め制御-左上・右下
        self.update_diagonal1(x,y,color)
        #斜め制御-左下・右上
        self.update_diagonal2(x,y,color)

    def update_length(self,x,y,color):
        for i in range(1,x):
            if self.board[x-i,y]==color:
                self.board[x-i:x,y]=color
                break
            elif self.board[x-i,y]==0:
                break
            else:
                continue

        for i in range(1,9-x):
            if self.board[x+i,y]==color:
                self.board[x:x+i,y]=color
                break
            elif self.board[x+i,y]==0:
                break 
            else:
                continue

    def update_width(self,x,y,color):
        for i in range(1,y):
            if self.board[x,y-i]==color:
                self.board[x,y-i:y]=color
                break
            elif self.board[x,y-i]==0:
                break
            else:
                continue

        for i in range(1,9-y):
            if self.board[x,y+i]==color:
                self.board[x,y:y+i]=color
                break
            elif self.board[x,y+i]==0:
                break
            else:
                continue
    
    def update_diagonal1(self,x,y,color):
        for i in range(1,min(x,y)+1):
            if (x-i<1)|(y-i<1):
                break
            if self.board[x-i,y-i]==color:
                for c in range(i):
                    self.board[x-c,y-c]=color
                break
            elif self.board[x-i,y-i]==0:
                break
            else:
                continue

        for i in range(1,min(9-x,9-y)+1):
            if (x+i>8)|(y+i>8):
                break         
            if self.board[x+i,y+i]==color:
                for c in range(i):
                    self.board[x+c,y+c]=color
                break
            elif self.board[x+i,y+i]==0:
                break
            else:
                continue

    def update_diagonal2(self,x,y,color):
        for i in range(1,min(9-x,y)+1):
            if (x+i>8)|(y-i<1):
                break
            if self.board[x+i,y-i]==color:
                for c in range(i):
                    self.board[x+c,y-c]=color
                break
            elif self.board[x+i,y-i]==0:
                break
            else:
                continue

        for i in range(1,min(x,9-y)+1):
            if (x-i<1)|(y+i>8):
                break
            if self.board[x-i,y+i]==color:
                for c in range(i):
                    self.board[x-c,y+c]=color
                break
            elif self.board[x-i,y+i]==0:
                break
            else:
                continue

    def get_available_list(self,color):
        available_list=[]

        for y in range(1,9):
            for x in range(1,9):
                if self.board[x,y]==0:

                    if self.judge(x,y,color)==True:
                        available_list.append((x,y))

        return available_list

    def judge(self,x,y,color):
        board_p=self.board.copy()
        self.update_board(x,y,color)

        if abs((self.board-board_p).sum())==1:
            self.board=board_p
            return False
        else:
            self.board=board_p
            return True

    def input_judge(self,x,y,color,board):
        board_p=board.copy()
        self.update_board(x,y,color)

        if abs((board-board_p).sum())==1:
            return False
        else:
            return True


class player(reversi_board):

  def __init__(self,color):
      super().__init__()

      self.color=color
      self.x=0
      self.y=0

  def initialize(self):
      self.__init__(self.color)

  def input_point(self,board):
      while True:

          self.x=input('行を選択してください(1-8): ')
          self.y=input('列を選択してください(1-8): ')
          if self.check_none()==False:
              continue
          if self.check_int()==False:
              continue
          if self.check_range()==False:
              continue
          if self.check_available(board)==False:
              print('そこには置けないよ！！')
              continue

          return self.x,self.y
      
  def check_none(self):
      if (self.x=='')|(self.y==''):
          print('整数を入力してね！')
          return False
      else:
          return True

  def check_int(self):
      try:
          self.x =int(self.x)
          self.y =int(self.y)
      except ValueError:
          print('整数で入力してね！！')
          return False

      return True

  def check_range(self):

      if (self.x<1)|(self.x>8)|(self.y<1)|(self.y>8):
          print('1-8で入力してね！！')
          return False 
      elif self.board[self.x,self.y]!=0:
          print('そこはもう埋まってる！！')
          return False
      else:
          return True

  def check_available(self,board):
      
    return self.input_judge(self.x,self.y,self.color,board)


class game():

    def __init__(self):
        self.game_board=reversi_board()
        self.p_b=player(color=1)
        self.p_w=player(color=-1)

        self.turn=1
        self.x=0
        self.y=0
        self.black_score=0
        self.white_score=0
    
    def initialize_game(self):
        self.game_board.initialize_board()
        self.p_b.initialize()
        self.p_w.initialize()
        
        self.turn=1
        self.x=0
        self.y=0
        self.black_score=0
        self.white_score=0

    def play(self):
        self.initialize_game()

        while True:
            if self.check_gameover()==True:
                break
            self.check_available()
            self.game_board.show_board(color=self.turn)
            self.input_main()
            self.game_board.update_board(self.x,self.y,self.turn)
            self.turn=-self.turn
      
    def input_main(self):
        if self.turn==1:
            self.x,self.y=self.p_b.input_point(self.game_board.board)
        else:
            self.x,self.y=self.p_w.input_point(self.game_board.board)
    
    def check_available(self):
        if (self.game_board.get_available_list(self.turn)==[]):
            print('置けないから相手のターンになるよ')           
            self.turn=-self.turn

    def check_gameover(self):
        if (self.game_board.get_available_list(self.turn)==[])&(self.game_board.get_available_list(-self.turn)==[]):
            self.get_score()
            self.show_score()

            return True
        else:
            return False

    def get_score(self):
        self.black_score=np.sum(self.board==1)
        self.white_score=np.sum(self.board==-1)

    def show_score(self):
        if self.black_score>self.white_score:
            print('黒{}:白{}で黒の勝ち！'.format(self.black_score,self.white_score))
        elif self.black_score<self.white_score:
            print('黒{}:白{}で白の勝ち！'.format(self.black_score,self.white_score))
        else:
            print('引き分け！')
        print('ゲーム終了！')
