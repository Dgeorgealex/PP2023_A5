import random
from game_logic.state import State


class MiniMax:
    def __init__(self, mode):
        if mode == 'easy':
            self.depth = 2
        elif mode == 'normal':
            self.depth = 3
        else:
            self.depth = 6

    def get_best_move(self, state):
        _, best_move = self.minimax(state, True, self.depth)
        return best_move

    def minimax(self, state,  max_state, depth):
        if depth == 0 or state.winning_state() or state.losing_state():
            return state.evaluate(), None

        moves = state.possible_moves()
        if max_state:
            best_value = -10000
            best_move = None
            for move in moves:
                next_state = state.copy()
                next_state.move(move[0], move[1])
                tmp, _ = self.minimax(next_state, False, depth-1)

                if tmp > best_value:
                    best_value = tmp
                    best_move = move

        else:
            best_value = 10000
            best_move = None
            for move in moves:
                next_state = state.copy()
                next_state.move(move[0], move[1])
                tmp, _ = self.minimax(next_state, True, depth-1)

                if tmp < best_value:
                    best_value = tmp
                    best_move = move

        return best_value, best_move
