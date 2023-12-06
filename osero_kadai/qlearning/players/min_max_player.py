from qlearning.board import ReversiBoard
import numpy as np

class MinmaxPlayer:
    INF = float('inf')
    BOARD_SIZE = 4

    def __init__(self, color):
        self.color = color
        self.name = 'minmax'

    def next_move(self, board_data)-> tuple[int,int] or None:
        board = ReversiBoard(board_data)
        position = board.get_available_list(self.color)
        depth = 3

        if len(position)==0:
            return None
        
        (move, value) = self._max_val(board, -self.INF, self.INF, depth, self.color)

        return move

    def _max_val(self, state:ReversiBoard, alpha, beta, depth, color):
        if state.is_game_over:
            return None, self._utility(state, color)
        elif depth == 0:
            return None, self._evaluation(state, color)

        best = None
        v = -self.INF

        moves = state.get_available_list(color)
        #実質depthの数だけ探索→それ以降はevalation
        for move in moves:
            new_board = ReversiBoard(state.get_next(move, color))
            _, value = self._min_val(new_board, alpha, beta, depth - 1, color)#交互に-1して代入していくことでdepthの数探索する
            if best is None or value > v:
                best = move
                v = value
            if v >= beta:
                return best, v
            alpha = max(alpha, v)
        return best, v

    #相手の最小スコアを検索する
    def _min_val(self, state:ReversiBoard, alpha, beta, depth, color):
        if state.is_game_over:
            return None, self._utility(state, color)
        elif depth == 0:
            return None, self._evaluation(state, color)

        best = None
        v = self.INF

        moves = state.get_available_list(-color)
        for move in moves:
            new_board = ReversiBoard(state.get_next(move, -color))
            _, value = self._max_val(new_board, alpha, beta, depth - 1, color)

            if best is None or value < v:
                best = move
                v = value
            if alpha >= v:
                return best, v
            beta = min(beta, v)
        return best, v

    def _utility(self, state, color):
        black_score = np.sum(state.get == 1)
        white_score = np.sum(state.get == -1)
        if black_score > white_score:
            return self.INF if color == 1 else -self.INF
        elif black_score < white_score:
            return self.INF if color == -1 else -self.INF
        else:
            return 0

    #方策のようなもの(荷重をかけている)
    def _evaluation(self, state, color):
        result = 0
        weight = [
            #[0, 0, 0, 0, 0],
            [ 2, 1, 1, 2],
            [ 1, 1, 1, 1],
            [ 1, 1, 1, 1],
            [ 2, 1, 1, 2]
        ]
        """
        weight = [
        #[0,0,0,0,0,0,0,0,0],
        [0,99,-8,8,6,6,8,-8,99],
        [0,-8,-24,-4,-3,-3,-4,-24,-8],
        [0,8,-4,7,4,4,7,-4,8],
        [0,6,-3,4,0,0,4,-3,6],
        [0,6,-3,4,0,0,4,-3,6],
        [0,8,-4,7,4,4,7,-4,8],
        [0,-8,-24,-4,-3,-3,-4,-24,-8],
        [0,99,-8,8,6,6,8,-8,99]
         ]
        """
        for x in range(self.BOARD_SIZE):
            for y in range(self.BOARD_SIZE):
                if state.get[x, y] == color:
                    result += weight[x][y]
                elif state.get[x, y] == -color:
                    result -= weight[x][y]

        return result
    def getGameResult(self, board, p2,):
        pass



