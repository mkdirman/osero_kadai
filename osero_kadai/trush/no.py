from qlearning.game import GameFactory, ModeGame, ModeTurn
from qlearning.board import ReversiBoard

def set_up():
    while True:            
        mode: GameMode = ModeGame.value_of(input('モードを選択してね:random or friends'))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
        turn_main_player: TurnMode = ModeTurn.value_of(input('先攻・後攻を選んでね:first or later---'))

        try:
            game = GameFactory.create(mode, turn_main_player)
            break

        except ValueError as e:
            print(e)
    return game

def q_main(num_game=1001):

    game = set_up()

    for m in range(num_game):


        while game.is_continue:

            game.is_available_put

            #game.display_board

            try:
                game.put_stone
            except ValueError as e:
                print(str(e))
                continue
            game.update_board
            game.learn
            game.change_turn
            #print(game.players.later.q._values)
        game.display_final_score
        game.initialize

    

        if (m%100)==0:
            print(game.count_win/100)
            game.count_win=0


#if __name__ == "__main__":
q_main()

    