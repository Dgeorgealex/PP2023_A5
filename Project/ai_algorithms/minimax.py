import random

from game_logic.state import State

class MiniMax:
    def __init__(self, mode):
        pass

    def get_best_move(self, state):
        moves = state.possible_moves()
        return random.choice(moves)