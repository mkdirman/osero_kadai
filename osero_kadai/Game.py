from Player import Player
from ReversiBoard import ReversiBoard

class Game():

    def __init__(self):
        self.game_board= ReversiBoard()
        self.p_b= Player(color= 1)
        self.p_w= Player(color= -1)

        self.turn= 1
        self.x= 0
        self.y= 0
        self.black_score= 0
        self.white_score= 0

    @property
    def initialize_game(self):
        self.game_board.initialize_board
        self.p_b.initialize
        self.p_w.initialize

        self.turn= 1
        self.x= 0
        self.y= 0
        self.black_score= 0
        self.white_score= 0

    def main(self):
        self.initialize_game

        while True:
            if self.is_gameover:
                break
            self.is_available
            self.game_board.show_board(color= self.turn)

            self.input_main
            try:
                self.game_board.is_0(self.x, self.y)
                self.game_board.input_judge(self.x, self.y, color= self.turn)
            except ValueError as e:
                print(str(e))
                continue

            self.game_board.update_board(self.x, self.y, self.turn)
            self.turn= -self.turn

    @property
    def input_main(self):
        if self.turn==1:
            self.x,self.y= self.p_b.input_point()
        else:
            self.x,self.y= self.p_w.input_point()

    @property
    def is_available(self):
        if (self.game_board.get_available_list(self.turn)== []):
            print('置けないよ！')
            self.turn= -self.turn

    @property
    def is_gameover(self):
        if (self.game_board.get_available_list(self.turn)== [])&(self.game_board.get_available_list(-self.turn)== []):
            self.get_score
            self.show_score
            return True
        else:
            return False

    @property
    def get_score(self):
        self.black_score= np.sum(self.board== 1)
        self.white_score= np.sum(self.board== -1)

    @property
    def show_score(self):
        if self.black_score > self.white_score:
            print('黒{}:白{}で黒の勝ち！'.format(self.black_score, self.white_score))
        elif self.black_score < self.white_score:
            print('黒{}:白{}で白の勝ち！'.format(self.black_score, self.white_score))
        else:
            print('引き分け！')
        print('ゲーム終了')