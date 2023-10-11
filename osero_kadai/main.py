from models.tmp_game import GameFactory, ModeGame, ModeTurn
def set_up():
    while True:            
        mode: GameMode = ModeGame.value_of(input('モードを選択してね:cpu or friends'))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
        turn_main_player: TurnMode = ModeTurn.value_of(input('先攻・後攻を選んでね:先攻 or 後攻---'))

        try:
            game = GameFactory.create(mode, turn_main_player)
            break

        except ValueError as e:
            print(e)
    return game

def main():

    game = set_up()

    while game.is_continue:

        game.is_available_put

        game.display_board
        try:
            game.put_stone
        except ValueError as e:
            print(str(e))
            continue

        game.update_board
        game.change_turn
           
    game.display_final_score

if __name__ == "__main__":
    main()

