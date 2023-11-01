from models.tmp_game import GameFactory, ModeGame, ModeTurn
<<<<<<< Updated upstream
=======
from models.reversi_board import ReversiBoard
def set_up():
    while True:            
        mode: GameMode = ModeGame.value_of(input('モードを選択してね:cpu or friends'))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
        turn_main_player: TurnMode = ModeTurn.value_of(input('先攻・後攻を選んでね:先攻 or 後攻---'))
>>>>>>> Stashed changes


def main():

    game = GameFactory.create(ModeGame.set_up(), ModeTurn.set_up())

    for _ in range(10):

        while game.is_continue:

            game.is_available_put

            #game.display_board

            try:
                game.put_stone
            except ValueError as e:
                print(str(e))
                continue

            game.update_board
            game.change_turn
            game.learn
            #print(game.players.later.q._values)
        game.display_final_score
        game.initialize

<<<<<<< Updated upstream
        game.update_board
        game.change_turn

    game.show_score
=======
>>>>>>> Stashed changes

if __name__ == "__main__":
    main()

    #