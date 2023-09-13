from models.tmp_game import GameFactory, ModeGame, ModeTurn


def main():

    game = GameFactory.create(ModeGame.set_up(), ModeTurn.set_up())

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

    game.show_score

if __name__ == "__main__":
    main()

