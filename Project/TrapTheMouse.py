import sys
from game_logic.game_controller import Game


def main():
    game_modes = ['easy', 'normal', 'hard', 'friend']
    if len(sys.argv) != 2:
        print("Invalid arguments")
        exit()

    mode = sys.argv[1]
    if mode not in game_modes:
        print("Invalid game mode")
        exit()

    my_game = Game()
    my_game.play(mode)

    print('Thanks for playing!')


if __name__ == "__main__":
    main()
