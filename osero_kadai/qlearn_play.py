from qlearning.players.nnqplayer import NNQPlayer
from qlearning.players.qplayer import QPlayer
from qlearning.players.random_player import RandomPlayer
from qlearning.players.min_max_player import MinmaxPlayer
from qlearning.orgnize import Organizer
import random
import torch

seed = 100
torch.manual_seed(seed)


p1 = NNQPlayer(1)
p2 = MinmaxPlayer(-1)

organizer = Organizer(nplay=20000, show_board=False, show_result=False)
organizer.play_game(p1, p2)
#print(p1.q._values)

p1.change_to_battle_mode
p2 = MinmaxPlayer(-1)


organizer = Organizer(nplay=10000, show_board=False, show_result=False)
organizer.play_game(p1, p2)
"""
experience replay (優先度付き)
↑学習が進んでいないものを優先して学習していく

Win count, player1(ql): 1, player2(minmax): 0, draw: 0
0試合目
Win count, player1(ql): 38, player2(minmax): 62, draw: 0
Win count, player1(ql): 33, player2(minmax): 67, draw: 0
200試合目
Win count, player1(ql): 13, player2(minmax): 86, draw: 1
Win count, player1(ql): 11, player2(minmax): 89, draw: 0
400試合目
Win count, player1(ql): 20, player2(minmax): 80, draw: 0
Win count, player1(ql): 20, player2(minmax): 80, draw: 0
600試合目
Win count, player1(ql): 14, player2(minmax): 85, draw: 1
Win count, player1(ql): 23, player2(minmax): 76, draw: 1
800試合目
Win count, player1(ql): 21, player2(minmax): 75, draw: 4
Win count, player1(ql): 18, player2(minmax): 82, draw: 0
1000試合目
Win count, player1(ql): 23, player2(minmax): 73, draw: 4
Win count, player1(ql): 19, player2(minmax): 77, draw: 4
1200試合目
Win count, player1(ql): 17, player2(minmax): 81, draw: 2
Win count, player1(ql): 13, player2(minmax): 87, draw: 0
1400試合目
Win count, player1(ql): 16, player2(minmax): 83, draw: 1
Win count, player1(ql): 17, player2(minmax): 80, draw: 3
1600試合目
Win count, player1(ql): 23, player2(minmax): 75, draw: 2
Win count, player1(ql): 10, player2(minmax): 88, draw: 2
1800試合目
Win count, player1(ql): 19, player2(minmax): 80, draw: 1
Win count, player1(ql): 18, player2(minmax): 80, draw: 2
2000試合目
Win count, player1(ql): 15, player2(minmax): 81, draw: 4
Win count, player1(ql): 18, player2(minmax): 79, draw: 3
2200試合目
Win count, player1(ql): 58, player2(minmax): 42, draw: 0
Win count, player1(ql): 62, player2(minmax): 37, draw: 1
2400試合目
Win count, player1(ql): 55, player2(minmax): 44, draw: 1
Win count, player1(ql): 63, player2(minmax): 34, draw: 3
2600試合目
Win count, player1(ql): 61, player2(minmax): 38, draw: 1
Win count, player1(ql): 61, player2(minmax): 36, draw: 3
2800試合目
Win count, player1(ql): 54, player2(minmax): 45, draw: 1
Win count, player1(ql): 44, player2(minmax): 55, draw: 1
3000試合目
Win count, player1(ql): 61, player2(minmax): 37, draw: 2
Win count, player1(ql): 53, player2(minmax): 47, draw: 0
3200試合目
Win count, player1(ql): 56, player2(minmax): 44, draw: 0
Win count, player1(ql): 57, player2(minmax): 43, draw: 0
3400試合目
Win count, player1(ql): 57, player2(minmax): 42, draw: 1
Win count, player1(ql): 45, player2(minmax): 51, draw: 4
3600試合目
Win count, player1(ql): 49, player2(minmax): 49, draw: 2
Win count, player1(ql): 51, player2(minmax): 46, draw: 3
3800試合目
Win count, player1(ql): 44, player2(minmax): 54, draw: 2
Win count, player1(ql): 46, player2(minmax): 53, draw: 1
4000試合目
Win count, player1(ql): 45, player2(minmax): 49, draw: 6
Win count, player1(ql): 44, player2(minmax): 56, draw: 0
4200試合目
Win count, player1(ql): 49, player2(minmax): 50, draw: 1
Win count, player1(ql): 52, player2(minmax): 47, draw: 1
4400試合目
Win count, player1(ql): 49, player2(minmax): 50, draw: 1
Win count, player1(ql): 49, player2(minmax): 50, draw: 1
4600試合目
Win count, player1(ql): 46, player2(minmax): 52, draw: 2
Win count, player1(ql): 50, player2(minmax): 50, draw: 0
4800試合目
Win count, player1(ql): 47, player2(minmax): 51, draw: 2
Win count, player1(ql): 49, player2(minmax): 50, draw: 1
5000試合目
Win count, player1(ql): 50, player2(minmax): 49, draw: 1
Win count, player1(ql): 51, player2(minmax): 48, draw: 1
5200試合目
Win count, player1(ql): 47, player2(minmax): 51, draw: 2
Win count, player1(ql): 48, player2(minmax): 50, draw: 2
5400試合目
Win count, player1(ql): 52, player2(minmax): 46, draw: 2
Win count, player1(ql): 53, player2(minmax): 45, draw: 2
5600試合目
Win count, player1(ql): 53, player2(minmax): 45, draw: 2
Win count, player1(ql): 51, player2(minmax): 47, draw: 2
5800試合目
Win count, player1(ql): 48, player2(minmax): 49, draw: 3
Win count, player1(ql): 52, player2(minmax): 48, draw: 0
6000試合目
Win count, player1(ql): 50, player2(minmax): 48, draw: 2
Win count, player1(ql): 47, player2(minmax): 52, draw: 1
6200試合目
Win count, player1(ql): 48, player2(minmax): 52, draw: 0
Win count, player1(ql): 47, player2(minmax): 53, draw: 0
6400試合目
Win count, player1(ql): 44, player2(minmax): 55, draw: 1
Win count, player1(ql): 51, player2(minmax): 48, draw: 1
6600試合目
Win count, player1(ql): 49, player2(minmax): 49, draw: 2
Win count, player1(ql): 46, player2(minmax): 52, draw: 2
6800試合目
Win count, player1(ql): 48, player2(minmax): 51, draw: 1
Win count, player1(ql): 46, player2(minmax): 54, draw: 0
7000試合目
Win count, player1(ql): 46, player2(minmax): 51, draw: 3
Win count, player1(ql): 46, player2(minmax): 51, draw: 3
7200試合目
Win count, player1(ql): 53, player2(minmax): 45, draw: 2
Win count, player1(ql): 52, player2(minmax): 47, draw: 1
7400試合目
Win count, player1(ql): 47, player2(minmax): 51, draw: 2
Win count, player1(ql): 48, player2(minmax): 52, draw: 0
7600試合目
Win count, player1(ql): 49, player2(minmax): 48, draw: 3
Win count, player1(ql): 51, player2(minmax): 49, draw: 0
7800試合目
Win count, player1(ql): 49, player2(minmax): 51, draw: 0
Win count, player1(ql): 50, player2(minmax): 49, draw: 1
8000試合目
Win count, player1(ql): 50, player2(minmax): 50, draw: 0
Win count, player1(ql): 50, player2(minmax): 49, draw: 1
8200試合目
Win count, player1(ql): 48, player2(minmax): 50, draw: 2
Win count, player1(ql): 51, player2(minmax): 48, draw: 1
8400試合目
Win count, player1(ql): 49, player2(minmax): 51, draw: 0
Win count, player1(ql): 49, player2(minmax): 50, draw: 1
8600試合目
Win count, player1(ql): 50, player2(minmax): 47, draw: 3
Win count, player1(ql): 46, player2(minmax): 51, draw: 3
8800試合目
Win count, player1(ql): 50, player2(minmax): 48, draw: 2
Win count, player1(ql): 49, player2(minmax): 51, draw: 0
9000試合目
Win count, player1(ql): 48, player2(minmax): 52, draw: 0
Win count, player1(ql): 52, player2(minmax): 48, draw: 0
9200試合目
Win count, player1(ql): 49, player2(minmax): 50, draw: 1

→過学習

Win count, player1(ql): 8, player2(minmax): 92, draw: 0
9400試合目
Win count, player1(ql): 7, player2(minmax): 93, draw: 0
Win count, player1(ql): 4, player2(minmax): 96, draw: 0
9600試合目
Win count, player1(ql): 3, player2(minmax): 96, draw: 1
Win count, player1(ql): 5, player2(minmax): 95, draw: 0
9800試合目
Win count, player1(ql): 8, player2(minmax): 92, draw: 0
Win count, player1(ql): 4, player2(minmax): 96, draw: 0
10000試合目
Win count, player1(ql): 5, player2(minmax): 95, draw: 0
Win count, player1(ql): 5, player2(minmax): 95, draw: 0

"""

"""
experience replay(優先度付き2)

Win count, player1(ql): 1, player2(minmax): 0, draw: 0
0試合目
Win count, player1(ql): 16, player2(minmax): 72, draw: 12
Win count, player1(ql): 35, player2(minmax): 58, draw: 7
200試合目
Win count, player1(ql): 24, player2(minmax): 70, draw: 6
Win count, player1(ql): 31, player2(minmax): 63, draw: 6
400試合目
Win count, player1(ql): 36, player2(minmax): 58, draw: 6
Win count, player1(ql): 22, player2(minmax): 72, draw: 6
600試合目
Win count, player1(ql): 39, player2(minmax): 55, draw: 6
Win count, player1(ql): 27, player2(minmax): 64, draw: 9
800試合目
Win count, player1(ql): 31, player2(minmax): 61, draw: 8
Win count, player1(ql): 35, player2(minmax): 55, draw: 10
1000試合目
Win count, player1(ql): 33, player2(minmax): 60, draw: 7
Win count, player1(ql): 38, player2(minmax): 53, draw: 9
1200試合目
Win count, player1(ql): 45, player2(minmax): 45, draw: 10
Win count, player1(ql): 40, player2(minmax): 53, draw: 7
1400試合目
Win count, player1(ql): 30, player2(minmax): 59, draw: 11
Win count, player1(ql): 39, player2(minmax): 47, draw: 14
1600試合目
Win count, player1(ql): 33, player2(minmax): 56, draw: 11
Win count, player1(ql): 14, player2(minmax): 77, draw: 9
1800試合目
Win count, player1(ql): 14, player2(minmax): 79, draw: 7
Win count, player1(ql): 18, player2(minmax): 71, draw: 11
2000試合目
Win count, player1(ql): 7, player2(minmax): 84, draw: 9
Win count, player1(ql): 9, player2(minmax): 84, draw: 7
2200試合目
Win count, player1(ql): 9, player2(minmax): 85, draw: 6
Win count, player1(ql): 68, player2(minmax): 27, draw: 5
2400試合目
Win count, player1(ql): 64, player2(minmax): 31, draw: 5
Win count, player1(ql): 51, player2(minmax): 41, draw: 8
2600試合目
Win count, player1(ql): 69, player2(minmax): 26, draw: 5
Win count, player1(ql): 50, player2(minmax): 46, draw: 4
2800試合目
Win count, player1(ql): 54, player2(minmax): 36, draw: 10
Win count, player1(ql): 46, player2(minmax): 42, draw: 12
3000試合目
Win count, player1(ql): 61, player2(minmax): 32, draw: 7
Win count, player1(ql): 62, player2(minmax): 33, draw: 5
3200試合目
Win count, player1(ql): 52, player2(minmax): 43, draw: 5
Win count, player1(ql): 52, player2(minmax): 43, draw: 5
3400試合目
Win count, player1(ql): 58, player2(minmax): 34, draw: 8
Win count, player1(ql): 61, player2(minmax): 31, draw: 8
3600試合目
Win count, player1(ql): 37, player2(minmax): 51, draw: 12
Win count, player1(ql): 53, player2(minmax): 38, draw: 9
3800試合目
Win count, player1(ql): 52, player2(minmax): 41, draw: 7

→過学習

Win count, player1(ql): 11, player2(minmax): 82, draw: 7
4000試合目
Win count, player1(ql): 3, player2(minmax): 94, draw: 3
Win count, player1(ql): 4, player2(minmax): 85, draw: 11
4200試合目
Win count, player1(ql): 7, player2(minmax): 82, draw: 11
Win count, player1(ql): 3, player2(minmax): 93, draw: 4
4400試合目
Win count, player1(ql): 1, player2(minmax): 93, draw: 6
Win count, player1(ql): 1, player2(minmax): 91, draw: 8
4600試合目
Win count, player1(ql): 1, player2(minmax): 93, draw: 6
Win count, player1(ql): 0, player2(minmax): 94, draw: 6
4800試合目
Win count, player1(ql): 0, player2(minmax): 94, draw: 6
Win count, player1(ql): 0, player2(minmax): 95, draw: 5
5000試合目
Win count, player1(ql): 1, player2(minmax): 93, draw: 6
Win count, player1(ql): 3, player2(minmax): 91, draw: 6

"""

"""
experience replay 無しの学習(上手くいくとき)1パターン

in count, player1(ql): 0, player2(minmax): 1, draw: 0
0試合目
Win count, player1(ql): 52, player2(minmax): 47, draw: 1
Win count, player1(ql): 44, player2(minmax): 48, draw: 8
Win count, player1(ql): 69, player2(minmax): 26, draw: 5
Win count, player1(ql): 31, player2(minmax): 68, draw: 1
Win count, player1(ql): 19, player2(minmax): 81, draw: 0
500試合目
Win count, player1(ql): 24, player2(minmax): 76, draw: 0
Win count, player1(ql): 20, player2(minmax): 80, draw: 0
Win count, player1(ql): 29, player2(minmax): 70, draw: 1
Win count, player1(ql): 26, player2(minmax): 74, draw: 0
Win count, player1(ql): 63, player2(minmax): 35, draw: 2
1000試合目
Win count, player1(ql): 70, player2(minmax): 24, draw: 6
Win count, player1(ql): 65, player2(minmax): 23, draw: 12
Win count, player1(ql): 60, player2(minmax): 26, draw: 14
Win count, player1(ql): 72, player2(minmax): 13, draw: 15
Win count, player1(ql): 60, player2(minmax): 14, draw: 26
1500試合目
Win count, player1(ql): 62, player2(minmax): 29, draw: 9
Win count, player1(ql): 66, player2(minmax): 27, draw: 7
Win count, player1(ql): 61, player2(minmax): 20, draw: 19
Win count, player1(ql): 54, player2(minmax): 31, draw: 15
Win count, player1(ql): 65, player2(minmax): 26, draw: 9
2000試合目
Win count, player1(ql): 56, player2(minmax): 25, draw: 19
Win count, player1(ql): 66, player2(minmax): 27, draw: 7
Win count, player1(ql): 73, player2(minmax): 12, draw: 15
Win count, player1(ql): 73, player2(minmax): 13, draw: 14
Win count, player1(ql): 74, player2(minmax): 8, draw: 18
2500試合目
Win count, player1(ql): 64, player2(minmax): 18, draw: 18
Win count, player1(ql): 64, player2(minmax): 19, draw: 17
Win count, player1(ql): 64, player2(minmax): 14, draw: 22
Win count, player1(ql): 56, player2(minmax): 10, draw: 34
Win count, player1(ql): 60, player2(minmax): 10, draw: 30
3000試合目
Win count, player1(ql): 52, player2(minmax): 16, draw: 32
Win count, player1(ql): 55, player2(minmax): 16, draw: 29
Win count, player1(ql): 58, player2(minmax): 14, draw: 28
Win count, player1(ql): 52, player2(minmax): 11, draw: 37
Win count, player1(ql): 53, player2(minmax): 7, draw: 40

→過学習？？？？急激に勝率が悪くなる

3500試合目
Win count, player1(ql): 48, player2(minmax): 21, draw: 31
Win count, player1(ql): 17, player2(minmax): 75, draw: 8
Win count, player1(ql): 9, player2(minmax): 72, draw: 19
Win count, player1(ql): 11, player2(minmax): 87, draw: 2
Win count, player1(ql): 26, player2(minmax): 58, draw: 16
4000試合目
Win count, player1(ql): 9, player2(minmax): 86, draw: 5
Win count, player1(ql): 6, player2(minmax): 87, draw: 7
Win count, player1(ql): 25, player2(minmax): 53, draw: 22
Win count, player1(ql): 6, player2(minmax): 92, draw: 2
Win count, player1(ql): 9, player2(minmax): 90, draw: 1
"""
"""
experience replay 無しの学習(上手くいくとき)2例目

Win count, player1(ql): 24, player2(minmax): 72, draw: 4
Win count, player1(ql): 21, player2(minmax): 76, draw: 3
Win count, player1(ql): 40, player2(minmax): 54, draw: 6
Win count, player1(ql): 69, player2(minmax): 29, draw: 2
Win count, player1(ql): 68, player2(minmax): 31, draw: 1
Win count, player1(ql): 35, player2(minmax): 59, draw: 6
Win count, player1(ql): 16, player2(minmax): 79, draw: 5
Win count, player1(ql): 26, player2(minmax): 70, draw: 4
Win count, player1(ql): 74, player2(minmax): 24, draw: 2
Win count, player1(ql): 72, player2(minmax): 25, draw: 3
Win count, player1(ql): 76, player2(minmax): 21, draw: 3
Win count, player1(ql): 70, player2(minmax): 28, draw: 2
Win count, player1(ql): 74, player2(minmax): 25, draw: 1
Win count, player1(ql): 72, player2(minmax): 27, draw: 1
Win count, player1(ql): 78, player2(minmax): 21, draw: 1
Win count, player1(ql): 74, player2(minmax): 25, draw: 1
Win count, player1(ql): 73, player2(minmax): 27, draw: 0
Win count, player1(ql): 66, player2(minmax): 33, draw: 1
Win count, player1(ql): 49, player2(minmax): 40, draw: 11
Win count, player1(ql): 72, player2(minmax): 24, draw: 4

→過学習？？？？やはり急に悪くなる

Win count, player1(ql): 25, player2(minmax): 53, draw: 22
Win count, player1(ql): 5, player2(minmax): 77, draw: 18
Win count, player1(ql): 7, player2(minmax): 91, draw: 2
Win count, player1(ql): 12, player2(minmax): 81, draw: 7
Win count, player1(ql): 8, player2(minmax): 79, draw: 13
Win count, player1(ql): 7, player2(minmax): 88, draw: 5
Win count, player1(ql): 6, player2(minmax): 87, draw: 7
Win count, player1(ql): 28, player2(minmax): 59, draw: 13
Win count, player1(ql): 14, player2(minmax): 72, draw: 14
"""

"""
fuber_lossの場合→微妙

Win count, player1(ql): 0, player2(minmax): 1, draw: 0
0試合目
Win count, player1(ql): 27, player2(minmax): 65, draw: 8
Win count, player1(ql): 28, player2(minmax): 70, draw: 2
200試合目
Win count, player1(ql): 40, player2(minmax): 49, draw: 11
Win count, player1(ql): 32, player2(minmax): 66, draw: 2
400試合目
Win count, player1(ql): 30, player2(minmax): 60, draw: 10
Win count, player1(ql): 21, player2(minmax): 70, draw: 9
600試合目
Win count, player1(ql): 38, player2(minmax): 58, draw: 4
Win count, player1(ql): 38, player2(minmax): 54, draw: 8
800試合目
Win count, player1(ql): 31, player2(minmax): 63, draw: 6
Win count, player1(ql): 40, player2(minmax): 55, draw: 5
1000試合目
Win count, player1(ql): 40, player2(minmax): 50, draw: 10
Win count, player1(ql): 41, player2(minmax): 56, draw: 3
1200試合目
Win count, player1(ql): 37, player2(minmax): 57, draw: 6
Win count, player1(ql): 30, player2(minmax): 63, draw: 7
1400試合目
Win count, player1(ql): 32, player2(minmax): 60, draw: 8
Win count, player1(ql): 34, player2(minmax): 60, draw: 6
1600試合目
Win count, player1(ql): 25, player2(minmax): 67, draw: 8
Win count, player1(ql): 33, player2(minmax): 61, draw: 6
1800試合目
Win count, player1(ql): 31, player2(minmax): 60, draw: 9
Win count, player1(ql): 42, player2(minmax): 50, draw: 8
2000試合目
Win count, player1(ql): 28, player2(minmax): 65, draw: 7
Win count, player1(ql): 22, player2(minmax): 71, draw: 7
2200試合目
Win count, player1(ql): 46, player2(minmax): 48, draw: 6
Win count, player1(ql): 27, player2(minmax): 64, draw: 9
2400試合目
Win count, player1(ql): 33, player2(minmax): 62, draw: 5
Win count, player1(ql): 33, player2(minmax): 61, draw: 6
2600試合目
Win count, player1(ql): 34, player2(minmax): 61, draw: 5
Win count, player1(ql): 18, player2(minmax): 74, draw: 8
2800試合目
Win count, player1(ql): 33, player2(minmax): 58, draw: 9
Win count, player1(ql): 41, player2(minmax): 51, draw: 8
3000試合目
Win count, player1(ql): 41, player2(minmax): 53, draw: 6
Win count, player1(ql): 23, player2(minmax): 69, draw: 8
"""

"""
board:4*4

Results:
      learn:  q vs q /10000
      →
      battle: q vs random  /3000

Win count, player1(ql): 0, player2(ql): 0, draw: 1
Win count, player1(ql): 50, player2(ql): 38, draw: 13
Win count, player1(ql): 95, player2(ql): 84, draw: 22
Win count, player1(ql): 145, player2(ql): 127, draw: 29
Win count, player1(ql): 195, player2(ql): 169, draw: 37
Win count, player1(ql): 252, player2(ql): 203, draw: 46
Win count, player1(ql): 302, player2(ql): 240, draw: 59
Win count, player1(ql): 347, player2(ql): 284, draw: 70
Win count, player1(ql): 399, player2(ql): 319, draw: 83
Win count, player1(ql): 452, player2(ql): 358, draw: 91
Win count, player1(ql): 506, player2(ql): 397, draw: 98
Win count, player1(ql): 559, player2(ql): 427, draw: 115
Win count, player1(ql): 612, player2(ql): 464, draw: 125
Win count, player1(ql): 665, player2(ql): 497, draw: 139
Win count, player1(ql): 721, player2(ql): 532, draw: 148
Win count, player1(ql): 781, player2(ql): 560, draw: 160
Win count, player1(ql): 838, player2(ql): 597, draw: 166
Win count, player1(ql): 895, player2(ql): 634, draw: 172
Win count, player1(ql): 954, player2(ql): 665, draw: 182
Win count, player1(ql): 1005, player2(ql): 704, draw: 192
Win count, player1(ql): 1057, player2(ql): 741, draw: 203
Win count, player1(ql): 1098, player2(ql): 790, draw: 213
Win count, player1(ql): 1154, player2(ql): 828, draw: 219
Win count, player1(ql): 1207, player2(ql): 862, draw: 232
Win count, player1(ql): 1257, player2(ql): 901, draw: 243
Win count, player1(ql): 1302, player2(ql): 945, draw: 254
Win count, player1(ql): 1354, player2(ql): 982, draw: 265
Win count, player1(ql): 1408, player2(ql): 1018, draw: 275
Win count, player1(ql): 1471, player2(ql): 1046, draw: 284
Win count, player1(ql): 1523, player2(ql): 1081, draw: 297
Win count, player1(ql): 1572, player2(ql): 1120, draw: 309
Win count, player1(ql): 1625, player2(ql): 1157, draw: 319
Win count, player1(ql): 1684, player2(ql): 1190, draw: 327
Win count, player1(ql): 1737, player2(ql): 1227, draw: 337
Win count, player1(ql): 1797, player2(ql): 1262, draw: 342
Win count, player1(ql): 1850, player2(ql): 1297, draw: 354
Win count, player1(ql): 1899, player2(ql): 1337, draw: 365
Win count, player1(ql): 1950, player2(ql): 1371, draw: 380
Win count, player1(ql): 2007, player2(ql): 1406, draw: 388
Win count, player1(ql): 2064, player2(ql): 1444, draw: 393
Win count, player1(ql): 2120, player2(ql): 1480, draw: 401
Win count, player1(ql): 2167, player2(ql): 1522, draw: 412
Win count, player1(ql): 2217, player2(ql): 1563, draw: 421
Win count, player1(ql): 2271, player2(ql): 1599, draw: 431
Win count, player1(ql): 2327, player2(ql): 1630, draw: 444
Win count, player1(ql): 2377, player2(ql): 1669, draw: 455
Win count, player1(ql): 2431, player2(ql): 1706, draw: 464
Win count, player1(ql): 2481, player2(ql): 1743, draw: 477
Win count, player1(ql): 2530, player2(ql): 1779, draw: 492
Win count, player1(ql): 2589, player2(ql): 1809, draw: 503
Win count, player1(ql): 2650, player2(ql): 1840, draw: 511
Win count, player1(ql): 2709, player2(ql): 1874, draw: 518
Win count, player1(ql): 2760, player2(ql): 1910, draw: 531
Win count, player1(ql): 2819, player2(ql): 1938, draw: 544
Win count, player1(ql): 2874, player2(ql): 1973, draw: 554
Win count, player1(ql): 2928, player2(ql): 2010, draw: 563
Win count, player1(ql): 2987, player2(ql): 2043, draw: 571
Win count, player1(ql): 3036, player2(ql): 2086, draw: 579
Win count, player1(ql): 3097, player2(ql): 2115, draw: 589
Win count, player1(ql): 3154, player2(ql): 2149, draw: 598
Win count, player1(ql): 3209, player2(ql): 2186, draw: 606
Win count, player1(ql): 3264, player2(ql): 2223, draw: 614
Win count, player1(ql): 3319, player2(ql): 2260, draw: 622
Win count, player1(ql): 3382, player2(ql): 2291, draw: 628
Win count, player1(ql): 3433, player2(ql): 2331, draw: 637
Win count, player1(ql): 3494, player2(ql): 2361, draw: 646
Win count, player1(ql): 3547, player2(ql): 2397, draw: 657
Win count, player1(ql): 3599, player2(ql): 2432, draw: 670
Win count, player1(ql): 3656, player2(ql): 2463, draw: 682
Win count, player1(ql): 3712, player2(ql): 2500, draw: 689
Win count, player1(ql): 3772, player2(ql): 2533, draw: 696
Win count, player1(ql): 3827, player2(ql): 2568, draw: 706
Win count, player1(ql): 3887, player2(ql): 2598, draw: 716
Win count, player1(ql): 3944, player2(ql): 2628, draw: 729
Win count, player1(ql): 3998, player2(ql): 2663, draw: 740
Win count, player1(ql): 4050, player2(ql): 2705, draw: 746
Win count, player1(ql): 4111, player2(ql): 2735, draw: 755
Win count, player1(ql): 4169, player2(ql): 2766, draw: 766
Win count, player1(ql): 4229, player2(ql): 2801, draw: 771
Win count, player1(ql): 4284, player2(ql): 2837, draw: 780
Win count, player1(ql): 4338, player2(ql): 2874, draw: 789
Win count, player1(ql): 4386, player2(ql): 2914, draw: 801
Win count, player1(ql): 4439, player2(ql): 2945, draw: 817
Win count, player1(ql): 4500, player2(ql): 2976, draw: 825
Win count, player1(ql): 4560, player2(ql): 3009, draw: 832
Win count, player1(ql): 4613, player2(ql): 3044, draw: 844
Win count, player1(ql): 4663, player2(ql): 3082, draw: 856
Win count, player1(ql): 4713, player2(ql): 3123, draw: 865
Win count, player1(ql): 4766, player2(ql): 3159, draw: 876
Win count, player1(ql): 4818, player2(ql): 3192, draw: 891
Win count, player1(ql): 4870, player2(ql): 3228, draw: 903
Win count, player1(ql): 4922, player2(ql): 3267, draw: 912
Win count, player1(ql): 4973, player2(ql): 3304, draw: 924
Win count, player1(ql): 5033, player2(ql): 3331, draw: 937
Win count, player1(ql): 5090, player2(ql): 3367, draw: 944
Win count, player1(ql): 5142, player2(ql): 3405, draw: 954
Win count, player1(ql): 5187, player2(ql): 3449, draw: 965
Win count, player1(ql): 5255, player2(ql): 3477, draw: 969
Win count, player1(ql): 5313, player2(ql): 3510, draw: 978
Win count, player1(ql): 5361, player2(ql): 3553, draw: 987


Win count, player1(ql): 1, player2(randomplayer): 0, draw: 0
Win count, player1(ql): 55, player2(randomplayer): 38, draw: 8
Win count, player1(ql): 106, player2(randomplayer): 76, draw: 19
Win count, player1(ql): 153, player2(randomplayer): 115, draw: 33
Win count, player1(ql): 200, player2(randomplayer): 153, draw: 48
Win count, player1(ql): 256, player2(randomplayer): 190, draw: 55
Win count, player1(ql): 303, player2(randomplayer): 227, draw: 71
Win count, player1(ql): 354, player2(randomplayer): 265, draw: 82
Win count, player1(ql): 396, player2(randomplayer): 311, draw: 94
Win count, player1(ql): 455, player2(randomplayer): 341, draw: 105
Win count, player1(ql): 497, player2(randomplayer): 386, draw: 118
Win count, player1(ql): 551, player2(randomplayer): 419, draw: 131
Win count, player1(ql): 601, player2(randomplayer): 461, draw: 139
Win count, player1(ql): 645, player2(randomplayer): 498, draw: 158
Win count, player1(ql): 685, player2(randomplayer): 543, draw: 173
Win count, player1(ql): 736, player2(randomplayer): 581, draw: 184
Win count, player1(ql): 784, player2(randomplayer): 621, draw: 196
Win count, player1(ql): 829, player2(randomplayer): 663, draw: 209
Win count, player1(ql): 876, player2(randomplayer): 704, draw: 221
Win count, player1(ql): 931, player2(randomplayer): 739, draw: 231
Win count, player1(ql): 983, player2(randomplayer): 774, draw: 244
Win count, player1(ql): 1038, player2(randomplayer): 811, draw: 252
Win count, player1(ql): 1083, player2(randomplayer): 853, draw: 265
Win count, player1(ql): 1138, player2(randomplayer): 888, draw: 275
Win count, player1(ql): 1183, player2(randomplayer): 929, draw: 289
Win count, player1(ql): 1229, player2(randomplayer): 974, draw: 298
Win count, player1(ql): 1270, player2(randomplayer): 1021, draw: 310
Win count, player1(ql): 1316, player2(randomplayer): 1060, draw: 325
Win count, player1(ql): 1358, player2(randomplayer): 1109, draw: 334
Win count, player1(ql): 1414, player2(randomplayer): 1144, draw: 343


"""
"""
board:4*4

Results:
      learn:  q vs q /10000
      →
      battle: q vs mimmax  /1500

Win count, player1(ql): 0, player2(ql): 1, draw: 0
Win count, player1(ql): 51, player2(ql): 41, draw: 9
Win count, player1(ql): 100, player2(ql): 83, draw: 18
Win count, player1(ql): 152, player2(ql): 124, draw: 25
Win count, player1(ql): 209, player2(ql): 159, draw: 33
Win count, player1(ql): 259, player2(ql): 197, draw: 45
Win count, player1(ql): 314, player2(ql): 228, draw: 59
Win count, player1(ql): 374, player2(ql): 259, draw: 68
Win count, player1(ql): 424, player2(ql): 295, draw: 82
Win count, player1(ql): 482, player2(ql): 328, draw: 91
Win count, player1(ql): 538, player2(ql): 363, draw: 100
Win count, player1(ql): 596, player2(ql): 394, draw: 111
Win count, player1(ql): 640, player2(ql): 432, draw: 129
Win count, player1(ql): 694, player2(ql): 472, draw: 135
Win count, player1(ql): 741, player2(ql): 511, draw: 149
Win count, player1(ql): 788, player2(ql): 550, draw: 163
Win count, player1(ql): 842, player2(ql): 586, draw: 173
Win count, player1(ql): 891, player2(ql): 626, draw: 184
Win count, player1(ql): 940, player2(ql): 664, draw: 197
Win count, player1(ql): 993, player2(ql): 699, draw: 209
Win count, player1(ql): 1049, player2(ql): 732, draw: 220
Win count, player1(ql): 1108, player2(ql): 767, draw: 226
Win count, player1(ql): 1163, player2(ql): 799, draw: 239
Win count, player1(ql): 1208, player2(ql): 841, draw: 252
Win count, player1(ql): 1263, player2(ql): 876, draw: 262
Win count, player1(ql): 1325, player2(ql): 905, draw: 271
Win count, player1(ql): 1376, player2(ql): 942, draw: 283
Win count, player1(ql): 1428, player2(ql): 978, draw: 295
Win count, player1(ql): 1488, player2(ql): 1005, draw: 308
Win count, player1(ql): 1542, player2(ql): 1037, draw: 322
Win count, player1(ql): 1598, player2(ql): 1072, draw: 331
Win count, player1(ql): 1653, player2(ql): 1109, draw: 339
Win count, player1(ql): 1703, player2(ql): 1150, draw: 348
Win count, player1(ql): 1761, player2(ql): 1182, draw: 358
Win count, player1(ql): 1819, player2(ql): 1219, draw: 363
Win count, player1(ql): 1868, player2(ql): 1260, draw: 373
Win count, player1(ql): 1920, player2(ql): 1298, draw: 383
Win count, player1(ql): 1973, player2(ql): 1334, draw: 394
Win count, player1(ql): 2024, player2(ql): 1373, draw: 404
Win count, player1(ql): 2085, player2(ql): 1403, draw: 413
Win count, player1(ql): 2149, player2(ql): 1435, draw: 417
Win count, player1(ql): 2203, player2(ql): 1473, draw: 425
Win count, player1(ql): 2252, player2(ql): 1511, draw: 438
Win count, player1(ql): 2304, player2(ql): 1549, draw: 448
Win count, player1(ql): 2365, player2(ql): 1580, draw: 456
Win count, player1(ql): 2418, player2(ql): 1613, draw: 470
Win count, player1(ql): 2472, player2(ql): 1650, draw: 479
Win count, player1(ql): 2530, player2(ql): 1682, draw: 489
Win count, player1(ql): 2588, player2(ql): 1711, draw: 502
Win count, player1(ql): 2643, player2(ql): 1747, draw: 511
Win count, player1(ql): 2689, player2(ql): 1791, draw: 521
Win count, player1(ql): 2743, player2(ql): 1831, draw: 527
Win count, player1(ql): 2798, player2(ql): 1864, draw: 539
Win count, player1(ql): 2856, player2(ql): 1894, draw: 551
Win count, player1(ql): 2913, player2(ql): 1927, draw: 561
Win count, player1(ql): 2965, player2(ql): 1966, draw: 570
Win count, player1(ql): 3018, player2(ql): 2003, draw: 580
Win count, player1(ql): 3080, player2(ql): 2033, draw: 588
Win count, player1(ql): 3134, player2(ql): 2067, draw: 600
Win count, player1(ql): 3188, player2(ql): 2100, draw: 613
Win count, player1(ql): 3239, player2(ql): 2137, draw: 625
Win count, player1(ql): 3293, player2(ql): 2168, draw: 640
Win count, player1(ql): 3349, player2(ql): 2204, draw: 648
Win count, player1(ql): 3409, player2(ql): 2241, draw: 651
Win count, player1(ql): 3460, player2(ql): 2274, draw: 667
Win count, player1(ql): 3519, player2(ql): 2304, draw: 678
Win count, player1(ql): 3573, player2(ql): 2340, draw: 688
Win count, player1(ql): 3630, player2(ql): 2375, draw: 696
Win count, player1(ql): 3685, player2(ql): 2409, draw: 707
Win count, player1(ql): 3740, player2(ql): 2444, draw: 717
Win count, player1(ql): 3794, player2(ql): 2483, draw: 724
Win count, player1(ql): 3846, player2(ql): 2522, draw: 733
Win count, player1(ql): 3900, player2(ql): 2561, draw: 740
Win count, player1(ql): 3960, player2(ql): 2590, draw: 751
Win count, player1(ql): 4013, player2(ql): 2626, draw: 762
Win count, player1(ql): 4068, player2(ql): 2659, draw: 774
Win count, player1(ql): 4125, player2(ql): 2691, draw: 785
Win count, player1(ql): 4183, player2(ql): 2726, draw: 792
Win count, player1(ql): 4237, player2(ql): 2762, draw: 802
Win count, player1(ql): 4288, player2(ql): 2795, draw: 818
Win count, player1(ql): 4346, player2(ql): 2830, draw: 825
Win count, player1(ql): 4399, player2(ql): 2865, draw: 837
Win count, player1(ql): 4455, player2(ql): 2898, draw: 848
Win count, player1(ql): 4506, player2(ql): 2938, draw: 857
Win count, player1(ql): 4563, player2(ql): 2968, draw: 870
Win count, player1(ql): 4613, player2(ql): 3012, draw: 876
Win count, player1(ql): 4664, player2(ql): 3046, draw: 891
Win count, player1(ql): 4723, player2(ql): 3081, draw: 897
Win count, player1(ql): 4777, player2(ql): 3115, draw: 909
Win count, player1(ql): 4829, player2(ql): 3149, draw: 923
Win count, player1(ql): 4883, player2(ql): 3188, draw: 930
Win count, player1(ql): 4940, player2(ql): 3219, draw: 942
Win count, player1(ql): 4998, player2(ql): 3248, draw: 955
Win count, player1(ql): 5048, player2(ql): 3286, draw: 967
Win count, player1(ql): 5105, player2(ql): 3318, draw: 978
Win count, player1(ql): 5161, player2(ql): 3354, draw: 986
Win count, player1(ql): 5224, player2(ql): 3381, draw: 996
Win count, player1(ql): 5271, player2(ql): 3422, draw: 1008
Win count, player1(ql): 5323, player2(ql): 3463, draw: 1015
Win count, player1(ql): 5377, player2(ql): 3497, draw: 1027


Win count, player1(ql): 0, player2(minmax): 1, draw: 0
Win count, player1(ql): 48, player2(minmax): 39, draw: 14
Win count, player1(ql): 92, player2(minmax): 86, draw: 23
Win count, player1(ql): 134, player2(minmax): 131, draw: 36
Win count, player1(ql): 173, player2(minmax): 181, draw: 47
Win count, player1(ql): 213, player2(minmax): 228, draw: 60
Win count, player1(ql): 250, player2(minmax): 279, draw: 72
Win count, player1(ql): 296, player2(minmax): 316, draw: 89
Win count, player1(ql): 335, player2(minmax): 358, draw: 108
Win count, player1(ql): 371, player2(minmax): 406, draw: 124
Win count, player1(ql): 411, player2(minmax): 449, draw: 141
Win count, player1(ql): 445, player2(minmax): 502, draw: 154
Win count, player1(ql): 479, player2(minmax): 561, draw: 161
Win count, player1(ql): 510, player2(minmax): 617, draw: 174
Win count, player1(ql): 553, player2(minmax): 655, draw: 193
Win count, player1(ql): 598, player2(minmax): 701, draw: 202

"""

"""
board:4*4

Results:
        learn: q vs random /10000

Win count, player1(ql): 1, player2(randomplayer): 0, draw: 0
Win count, player1(ql): 52, player2(randomplayer): 39, draw: 10
Win count, player1(ql): 101, player2(randomplayer): 76, draw: 24
Win count, player1(ql): 148, player2(randomplayer): 121, draw: 32
Win count, player1(ql): 193, player2(randomplayer): 162, draw: 46
Win count, player1(ql): 245, player2(randomplayer): 199, draw: 57
Win count, player1(ql): 293, player2(randomplayer): 241, draw: 67
Win count, player1(ql): 340, player2(randomplayer): 283, draw: 78
Win count, player1(ql): 393, player2(randomplayer): 320, draw: 88
Win count, player1(ql): 442, player2(randomplayer): 360, draw: 99
Win count, player1(ql): 483, player2(randomplayer): 405, draw: 113
Win count, player1(ql): 524, player2(randomplayer): 449, draw: 128
Win count, player1(ql): 578, player2(randomplayer): 487, draw: 136
Win count, player1(ql): 638, player2(randomplayer): 518, draw: 145
Win count, player1(ql): 691, player2(randomplayer): 556, draw: 154
Win count, player1(ql): 750, player2(randomplayer): 592, draw: 159
Win count, player1(ql): 795, player2(randomplayer): 634, draw: 172
Win count, player1(ql): 840, player2(randomplayer): 677, draw: 184
Win count, player1(ql): 893, player2(randomplayer): 715, draw: 193
Win count, player1(ql): 943, player2(randomplayer): 752, draw: 206
Win count, player1(ql): 995, player2(randomplayer): 791, draw: 215
Win count, player1(ql): 1038, player2(randomplayer): 831, draw: 232
Win count, player1(ql): 1077, player2(randomplayer): 886, draw: 238
Win count, player1(ql): 1116, player2(randomplayer): 934, draw: 251
Win count, player1(ql): 1162, player2(randomplayer): 973, draw: 266
Win count, player1(ql): 1208, player2(randomplayer): 1016, draw: 277
Win count, player1(ql): 1263, player2(randomplayer): 1048, draw: 290
Win count, player1(ql): 1315, player2(randomplayer): 1089, draw: 297
Win count, player1(ql): 1365, player2(randomplayer): 1134, draw: 302
Win count, player1(ql): 1423, player2(randomplayer): 1166, draw: 312
Win count, player1(ql): 1479, player2(randomplayer): 1199, draw: 323
Win count, player1(ql): 1530, player2(randomplayer): 1239, draw: 332
Win count, player1(ql): 1580, player2(randomplayer): 1280, draw: 341
Win count, player1(ql): 1633, player2(randomplayer): 1313, draw: 355
Win count, player1(ql): 1674, player2(randomplayer): 1360, draw: 367
Win count, player1(ql): 1716, player2(randomplayer): 1407, draw: 378
Win count, player1(ql): 1768, player2(randomplayer): 1443, draw: 390
Win count, player1(ql): 1817, player2(randomplayer): 1482, draw: 402
Win count, player1(ql): 1859, player2(randomplayer): 1527, draw: 415
Win count, player1(ql): 1906, player2(randomplayer): 1569, draw: 426
Win count, player1(ql): 1958, player2(randomplayer): 1608, draw: 435
Win count, player1(ql): 2006, player2(randomplayer): 1650, draw: 445
Win count, player1(ql): 2058, player2(randomplayer): 1683, draw: 460
Win count, player1(ql): 2105, player2(randomplayer): 1729, draw: 467
Win count, player1(ql): 2159, player2(randomplayer): 1765, draw: 477
Win count, player1(ql): 2208, player2(randomplayer): 1803, draw: 490
Win count, player1(ql): 2253, player2(randomplayer): 1845, draw: 503
Win count, player1(ql): 2298, player2(randomplayer): 1884, draw: 519
Win count, player1(ql): 2346, player2(randomplayer): 1923, draw: 532
Win count, player1(ql): 2395, player2(randomplayer): 1963, draw: 543
Win count, player1(ql): 2444, player2(randomplayer): 2001, draw: 556
Win count, player1(ql): 2490, player2(randomplayer): 2042, draw: 569
Win count, player1(ql): 2536, player2(randomplayer): 2083, draw: 582
Win count, player1(ql): 2589, player2(randomplayer): 2123, draw: 589
Win count, player1(ql): 2635, player2(randomplayer): 2166, draw: 600
Win count, player1(ql): 2679, player2(randomplayer): 2211, draw: 611
Win count, player1(ql): 2736, player2(randomplayer): 2246, draw: 619
Win count, player1(ql): 2781, player2(randomplayer): 2294, draw: 626
Win count, player1(ql): 2830, player2(randomplayer): 2332, draw: 639
Win count, player1(ql): 2872, player2(randomplayer): 2373, draw: 656
Win count, player1(ql): 2922, player2(randomplayer): 2412, draw: 667
Win count, player1(ql): 2970, player2(randomplayer): 2456, draw: 675
Win count, player1(ql): 3016, player2(randomplayer): 2499, draw: 686
Win count, player1(ql): 3065, player2(randomplayer): 2536, draw: 700
Win count, player1(ql): 3124, player2(randomplayer): 2569, draw: 708
Win count, player1(ql): 3181, player2(randomplayer): 2605, draw: 715
Win count, player1(ql): 3237, player2(randomplayer): 2640, draw: 724
Win count, player1(ql): 3278, player2(randomplayer): 2681, draw: 742
Win count, player1(ql): 3325, player2(randomplayer): 2725, draw: 751
Win count, player1(ql): 3369, player2(randomplayer): 2768, draw: 764
Win count, player1(ql): 3419, player2(randomplayer): 2804, draw: 778
Win count, player1(ql): 3470, player2(randomplayer): 2848, draw: 783
Win count, player1(ql): 3520, player2(randomplayer): 2890, draw: 791
Win count, player1(ql): 3562, player2(randomplayer): 2936, draw: 803
Win count, player1(ql): 3611, player2(randomplayer): 2976, draw: 814
Win count, player1(ql): 3658, player2(randomplayer): 3018, draw: 825
Win count, player1(ql): 3708, player2(randomplayer): 3060, draw: 833
Win count, player1(ql): 3752, player2(randomplayer): 3104, draw: 845
Win count, player1(ql): 3802, player2(randomplayer): 3142, draw: 857
Win count, player1(ql): 3843, player2(randomplayer): 3192, draw: 866
Win count, player1(ql): 3890, player2(randomplayer): 3235, draw: 876
Win count, player1(ql): 3938, player2(randomplayer): 3278, draw: 885
Win count, player1(ql): 3985, player2(randomplayer): 3321, draw: 895
Win count, player1(ql): 4042, player2(randomplayer): 3356, draw: 903
Win count, player1(ql): 4087, player2(randomplayer): 3401, draw: 913
Win count, player1(ql): 4133, player2(randomplayer): 3446, draw: 922
Win count, player1(ql): 4183, player2(randomplayer): 3485, draw: 933
Win count, player1(ql): 4237, player2(randomplayer): 3526, draw: 938
Win count, player1(ql): 4284, player2(randomplayer): 3569, draw: 948
Win count, player1(ql): 4335, player2(randomplayer): 3603, draw: 963
Win count, player1(ql): 4379, player2(randomplayer): 3652, draw: 970
Win count, player1(ql): 4427, player2(randomplayer): 3695, draw: 979
Win count, player1(ql): 4474, player2(randomplayer): 3737, draw: 990
Win count, player1(ql): 4526, player2(randomplayer): 3774, draw: 1001
Win count, player1(ql): 4572, player2(randomplayer): 3814, draw: 1015
Win count, player1(ql): 4627, player2(randomplayer): 3851, draw: 1023
Win count, player1(ql): 4677, player2(randomplayer): 3891, draw: 1033
Win count, player1(ql): 4717, player2(randomplayer): 3935, draw: 1049
Win count, player1(ql): 4771, player2(randomplayer): 3972, draw: 1058
Win count, player1(ql): 4823, player2(randomplayer): 4008, draw: 1070

"""

"""
board:4*4

Results:
      learn:  q vs mimmax /20000


Win count, player1(ql): 0, player2(minmax): 1, draw: 0
Win count, player1(ql): 51, player2(minmax): 42, draw: 8
Win count, player1(ql): 94, player2(minmax): 97, draw: 10
Win count, player1(ql): 134, player2(minmax): 151, draw: 16
Win count, player1(ql): 177, player2(minmax): 201, draw: 23
Win count, player1(ql): 215, player2(minmax): 251, draw: 35
Win count, player1(ql): 260, player2(minmax): 301, draw: 40
Win count, player1(ql): 303, player2(minmax): 350, draw: 48
Win count, player1(ql): 348, player2(minmax): 397, draw: 56
Win count, player1(ql): 394, player2(minmax): 442, draw: 65
Win count, player1(ql): 430, player2(minmax): 496, draw: 75
Win count, player1(ql): 472, player2(minmax): 547, draw: 82
Win count, player1(ql): 524, player2(minmax): 589, draw: 88
Win count, player1(ql): 567, player2(minmax): 639, draw: 95
Win count, player1(ql): 609, player2(minmax): 689, draw: 103
Win count, player1(ql): 655, player2(minmax): 734, draw: 112
Win count, player1(ql): 701, player2(minmax): 780, draw: 120
Win count, player1(ql): 746, player2(minmax): 828, draw: 127
Win count, player1(ql): 797, player2(minmax): 869, draw: 135
Win count, player1(ql): 834, player2(minmax): 926, draw: 141
Win count, player1(ql): 885, player2(minmax): 969, draw: 147
Win count, player1(ql): 930, player2(minmax): 1012, draw: 159
Win count, player1(ql): 973, player2(minmax): 1064, draw: 164
Win count, player1(ql): 1020, player2(minmax): 1109, draw: 172
Win count, player1(ql): 1066, player2(minmax): 1157, draw: 178
Win count, player1(ql): 1113, player2(minmax): 1197, draw: 191
Win count, player1(ql): 1151, player2(minmax): 1252, draw: 198
Win count, player1(ql): 1196, player2(minmax): 1301, draw: 204
Win count, player1(ql): 1237, player2(minmax): 1351, draw: 213
Win count, player1(ql): 1269, player2(minmax): 1411, draw: 221
Win count, player1(ql): 1320, player2(minmax): 1454, draw: 227
Win count, player1(ql): 1359, player2(minmax): 1508, draw: 234
Win count, player1(ql): 1405, player2(minmax): 1551, draw: 245
Win count, player1(ql): 1454, player2(minmax): 1596, draw: 251
Win count, player1(ql): 1499, player2(minmax): 1643, draw: 259
Win count, player1(ql): 1533, player2(minmax): 1702, draw: 266
Win count, player1(ql): 1579, player2(minmax): 1747, draw: 275
Win count, player1(ql): 1623, player2(minmax): 1797, draw: 281
Win count, player1(ql): 1670, player2(minmax): 1840, draw: 291
Win count, player1(ql): 1711, player2(minmax): 1890, draw: 300
Win count, player1(ql): 1751, player2(minmax): 1940, draw: 310
Win count, player1(ql): 1796, player2(minmax): 1989, draw: 316
Win count, player1(ql): 1836, player2(minmax): 2040, draw: 325
Win count, player1(ql): 1874, player2(minmax): 2090, draw: 337
Win count, player1(ql): 1912, player2(minmax): 2149, draw: 340
Win count, player1(ql): 1961, player2(minmax): 2195, draw: 345
Win count, player1(ql): 2003, player2(minmax): 2248, draw: 350
Win count, player1(ql): 2042, player2(minmax): 2298, draw: 361
Win count, player1(ql): 2088, player2(minmax): 2346, draw: 367
Win count, player1(ql): 2130, player2(minmax): 2399, draw: 372
Win count, player1(ql): 2170, player2(minmax): 2453, draw: 378
Win count, player1(ql): 2212, player2(minmax): 2502, draw: 387
Win count, player1(ql): 2252, player2(minmax): 2551, draw: 398
Win count, player1(ql): 2297, player2(minmax): 2598, draw: 406
Win count, player1(ql): 2345, player2(minmax): 2645, draw: 411
Win count, player1(ql): 2393, player2(minmax): 2690, draw: 418
Win count, player1(ql): 2430, player2(minmax): 2742, draw: 429
Win count, player1(ql): 2476, player2(minmax): 2788, draw: 437
Win count, player1(ql): 2515, player2(minmax): 2840, draw: 446
Win count, player1(ql): 2555, player2(minmax): 2887, draw: 459
Win count, player1(ql): 2595, player2(minmax): 2939, draw: 467
Win count, player1(ql): 2646, player2(minmax): 2981, draw: 474
Win count, player1(ql): 2686, player2(minmax): 3036, draw: 479
Win count, player1(ql): 2731, player2(minmax): 3079, draw: 491
Win count, player1(ql): 2768, player2(minmax): 3133, draw: 500
Win count, player1(ql): 2815, player2(minmax): 3178, draw: 508
Win count, player1(ql): 2854, player2(minmax): 3231, draw: 516
Win count, player1(ql): 2896, player2(minmax): 3286, draw: 519
Win count, player1(ql): 2933, player2(minmax): 3339, draw: 529
Win count, player1(ql): 2971, player2(minmax): 3396, draw: 534
Win count, player1(ql): 3022, player2(minmax): 3437, draw: 542
Win count, player1(ql): 3065, player2(minmax): 3487, draw: 549
Win count, player1(ql): 3112, player2(minmax): 3529, draw: 560
Win count, player1(ql): 3163, player2(minmax): 3570, draw: 568
Win count, player1(ql): 3202, player2(minmax): 3621, draw: 578
Win count, player1(ql): 3246, player2(minmax): 3670, draw: 585
Win count, player1(ql): 3295, player2(minmax): 3715, draw: 591
Win count, player1(ql): 3336, player2(minmax): 3765, draw: 600
Win count, player1(ql): 3374, player2(minmax): 3819, draw: 608
Win count, player1(ql): 3421, player2(minmax): 3867, draw: 613
Win count, player1(ql): 3462, player2(minmax): 3920, draw: 619
Win count, player1(ql): 3506, player2(minmax): 3966, draw: 629
Win count, player1(ql): 3547, player2(minmax): 4015, draw: 639
Win count, player1(ql): 3585, player2(minmax): 4070, draw: 646
Win count, player1(ql): 3624, player2(minmax): 4119, draw: 658
Win count, player1(ql): 3675, player2(minmax): 4160, draw: 666
Win count, player1(ql): 3710, player2(minmax): 4216, draw: 675
Win count, player1(ql): 3756, player2(minmax): 4264, draw: 681
Win count, player1(ql): 3806, player2(minmax): 4310, draw: 685
Win count, player1(ql): 3854, player2(minmax): 4356, draw: 691
Win count, player1(ql): 3908, player2(minmax): 4393, draw: 700
Win count, player1(ql): 3948, player2(minmax): 4444, draw: 709
Win count, player1(ql): 3985, player2(minmax): 4497, draw: 719
Win count, player1(ql): 4032, player2(minmax): 4541, draw: 728
Win count, player1(ql): 4079, player2(minmax): 4591, draw: 731
Win count, player1(ql): 4119, player2(minmax): 4642, draw: 740
Win count, player1(ql): 4173, player2(minmax): 4684, draw: 744
Win count, player1(ql): 4217, player2(minmax): 4729, draw: 755
Win count, player1(ql): 4264, player2(minmax): 4772, draw: 765
Win count, player1(ql): 4304, player2(minmax): 4826, draw: 771
Win count, player1(ql): 4348, player2(minmax): 4874, draw: 779
Win count, player1(ql): 4397, player2(minmax): 4915, draw: 789
Win count, player1(ql): 4447, player2(minmax): 4958, draw: 796
Win count, player1(ql): 4488, player2(minmax): 5011, draw: 802
Win count, player1(ql): 4522, player2(minmax): 5066, draw: 813
Win count, player1(ql): 4565, player2(minmax): 5120, draw: 816
Win count, player1(ql): 4617, player2(minmax): 5163, draw: 821
Win count, player1(ql): 4656, player2(minmax): 5216, draw: 829
Win count, player1(ql): 4698, player2(minmax): 5264, draw: 839
Win count, player1(ql): 4740, player2(minmax): 5310, draw: 851
Win count, player1(ql): 4786, player2(minmax): 5359, draw: 856
Win count, player1(ql): 4831, player2(minmax): 5408, draw: 862
Win count, player1(ql): 4871, player2(minmax): 5462, draw: 868
Win count, player1(ql): 4903, player2(minmax): 5520, draw: 878
Win count, player1(ql): 4953, player2(minmax): 5560, draw: 888
Win count, player1(ql): 5003, player2(minmax): 5602, draw: 896
Win count, player1(ql): 5044, player2(minmax): 5651, draw: 906
Win count, player1(ql): 5086, player2(minmax): 5697, draw: 918
Win count, player1(ql): 5128, player2(minmax): 5746, draw: 927
Win count, player1(ql): 5172, player2(minmax): 5795, draw: 934
Win count, player1(ql): 5220, player2(minmax): 5845, draw: 936
Win count, player1(ql): 5271, player2(minmax): 5887, draw: 943
Win count, player1(ql): 5313, player2(minmax): 5939, draw: 949
Win count, player1(ql): 5353, player2(minmax): 5990, draw: 958
Win count, player1(ql): 5403, player2(minmax): 6033, draw: 965
Win count, player1(ql): 5448, player2(minmax): 6083, draw: 970
Win count, player1(ql): 5492, player2(minmax): 6131, draw: 978
Win count, player1(ql): 5533, player2(minmax): 6180, draw: 988
Win count, player1(ql): 5576, player2(minmax): 6231, draw: 994
Win count, player1(ql): 5625, player2(minmax): 6274, draw: 1002
Win count, player1(ql): 5668, player2(minmax): 6322, draw: 1011
Win count, player1(ql): 5707, player2(minmax): 6369, draw: 1025
Win count, player1(ql): 5745, player2(minmax): 6423, draw: 1033
Win count, player1(ql): 5789, player2(minmax): 6477, draw: 1035
Win count, player1(ql): 5827, player2(minmax): 6530, draw: 1044
Win count, player1(ql): 5863, player2(minmax): 6586, draw: 1052
Win count, player1(ql): 5906, player2(minmax): 6636, draw: 1059
Win count, player1(ql): 5943, player2(minmax): 6687, draw: 1071
Win count, player1(ql): 5985, player2(minmax): 6736, draw: 1080
Win count, player1(ql): 6036, player2(minmax): 6780, draw: 1085
Win count, player1(ql): 6081, player2(minmax): 6823, draw: 1097
Win count, player1(ql): 6119, player2(minmax): 6878, draw: 1104
Win count, player1(ql): 6160, player2(minmax): 6933, draw: 1108
Win count, player1(ql): 6210, player2(minmax): 6974, draw: 1117
Win count, player1(ql): 6258, player2(minmax): 7014, draw: 1129
Win count, player1(ql): 6300, player2(minmax): 7067, draw: 1134
Win count, player1(ql): 6348, player2(minmax): 7114, draw: 1139
Win count, player1(ql): 6389, player2(minmax): 7167, draw: 1145
Win count, player1(ql): 6430, player2(minmax): 7218, draw: 1153
Win count, player1(ql): 6471, player2(minmax): 7271, draw: 1159
Win count, player1(ql): 6522, player2(minmax): 7312, draw: 1167
Win count, player1(ql): 6566, player2(minmax): 7364, draw: 1171
Win count, player1(ql): 6611, player2(minmax): 7410, draw: 1180
Win count, player1(ql): 6650, player2(minmax): 7463, draw: 1188
Win count, player1(ql): 6696, player2(minmax): 7512, draw: 1193
Win count, player1(ql): 6734, player2(minmax): 7567, draw: 1200
Win count, player1(ql): 6778, player2(minmax): 7614, draw: 1209
Win count, player1(ql): 6822, player2(minmax): 7667, draw: 1212
Win count, player1(ql): 6864, player2(minmax): 7717, draw: 1220
Win count, player1(ql): 6908, player2(minmax): 7770, draw: 1223
Win count, player1(ql): 6948, player2(minmax): 7824, draw: 1229
Win count, player1(ql): 6991, player2(minmax): 7873, draw: 1237
Win count, player1(ql): 7034, player2(minmax): 7921, draw: 1246
Win count, player1(ql): 7070, player2(minmax): 7977, draw: 1254
Win count, player1(ql): 7113, player2(minmax): 8023, draw: 1265
Win count, player1(ql): 7160, player2(minmax): 8068, draw: 1273
Win count, player1(ql): 7204, player2(minmax): 8117, draw: 1280
Win count, player1(ql): 7248, player2(minmax): 8168, draw: 1285
Win count, player1(ql): 7291, player2(minmax): 8220, draw: 1290
Win count, player1(ql): 7342, player2(minmax): 8263, draw: 1296
Win count, player1(ql): 7384, player2(minmax): 8314, draw: 1303
Win count, player1(ql): 7433, player2(minmax): 8356, draw: 1312
Win count, player1(ql): 7478, player2(minmax): 8400, draw: 1323
Win count, player1(ql): 7520, player2(minmax): 8451, draw: 1330
Win count, player1(ql): 7565, player2(minmax): 8499, draw: 1337
Win count, player1(ql): 7611, player2(minmax): 8551, draw: 1339
Win count, player1(ql): 7655, player2(minmax): 8599, draw: 1347
Win count, player1(ql): 7697, player2(minmax): 8648, draw: 1356
Win count, player1(ql): 7734, player2(minmax): 8702, draw: 1365
Win count, player1(ql): 7773, player2(minmax): 8756, draw: 1372
Win count, player1(ql): 7818, player2(minmax): 8803, draw: 1380
Win count, player1(ql): 7868, player2(minmax): 8846, draw: 1387
Win count, player1(ql): 7917, player2(minmax): 8889, draw: 1395
Win count, player1(ql): 7961, player2(minmax): 8937, draw: 1403
Win count, player1(ql): 8005, player2(minmax): 8980, draw: 1416
Win count, player1(ql): 8053, player2(minmax): 9027, draw: 1421
Win count, player1(ql): 8105, player2(minmax): 9064, draw: 1432
Win count, player1(ql): 8147, player2(minmax): 9115, draw: 1439
Win count, player1(ql): 8191, player2(minmax): 9163, draw: 1447
Win count, player1(ql): 8237, player2(minmax): 9209, draw: 1455
Win count, player1(ql): 8281, player2(minmax): 9261, draw: 1459
Win count, player1(ql): 8327, player2(minmax): 9309, draw: 1465
Win count, player1(ql): 8373, player2(minmax): 9357, draw: 1471
Win count, player1(ql): 8419, player2(minmax): 9404, draw: 1478
Win count, player1(ql): 8458, player2(minmax): 9456, draw: 1487
Win count, player1(ql): 8501, player2(minmax): 9505, draw: 1495
Win count, player1(ql): 8544, player2(minmax): 9555, draw: 1502
Win count, player1(ql): 8580, player2(minmax): 9615, draw: 1506
Win count, player1(ql): 8616, player2(minmax): 9673, draw: 1512
Win count, player1(ql): 8661, player2(minmax): 9723, draw: 1517
"""


""" 
board:8*8

Results:
      learn:  q vs random /1500

Win count, player1(ql): 1, player2(randomplayer): 0, draw: 0
Win count, player1(ql): 46, player2(randomplayer): 51, draw: 4
Win count, player1(ql): 98, player2(randomplayer): 93, draw: 10
Win count, player1(ql): 151, player2(randomplayer): 138, draw: 12
Win count, player1(ql): 199, player2(randomplayer): 188, draw: 14
Win count, player1(ql): 250, player2(randomplayer): 232, draw: 19
Win count, player1(ql): 303, player2(randomplayer): 279, draw: 19
Win count, player1(ql): 351, player2(randomplayer): 330, draw: 20
Win count, player1(ql): 400, player2(randomplayer): 377, draw: 24
Win count, player1(ql): 445, player2(randomplayer): 428, draw: 28
Win count, player1(ql): 497, player2(randomplayer): 471, draw: 33
Win count, player1(ql): 534, player2(randomplayer): 526, draw: 41
Win count, player1(ql): 585, player2(randomplayer): 572, draw: 44
Win count, player1(ql): 638, player2(randomplayer): 614, draw: 49
Win count, player1(ql): 695, player2(randomplayer): 655, draw: 51
Win count, player1(ql): 742, player2(randomplayer): 707, draw: 52

"""

