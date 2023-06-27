
from models.GameModel import Game

game=Game()


def main():
    game.set_up_game

    while game.is_continue:

        game.is_available

        game.show_board
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


