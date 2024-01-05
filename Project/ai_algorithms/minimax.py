import random
from game_logic.constants import WHO_IS_AI, MOUSE, WALLS
INF = 10000000


class MiniMax:
    def __init__(self, mode):
        if mode == 'easy':
            self.depth = 2
        elif mode == 'normal':
            self.depth = 3
        else:
            self.depth = 4
        if WHO_IS_AI == WALLS:
            self.depth -= 1

    def get_best_move(self, state):
        _, best_move = self.minimax(state, -INF, INF, True, self.depth)
        return best_move

    def minimax(self, state, alfa, beta, max_state, depth):
        if depth == 0 or state.winning_state() or state.losing_state():
            return state.evaluate(), None

        moves = state.possible_moves()
        random.shuffle(moves)

        if max_state:
            best_value = -INF
            best_move = None
            for move in moves:
                next_state = state.copy()
                next_state.move(move[0], move[1])
                tmp, _ = self.minimax(next_state, alfa, beta, False, depth-1)

                if best_value < tmp:
                    best_value = tmp
                    best_move = move

                alfa = max(alfa, best_value)

                if alfa >= beta:
                    break

        else:
            best_value = INF
            best_move = None
            for move in moves:
                next_state = state.copy()
                next_state.move(move[0], move[1])
                tmp, _ = self.minimax(next_state, alfa, beta, True, depth-1)

                if best_value > tmp:
                    best_value = tmp
                    best_move = move

                beta = min(beta, best_value)

                if alfa >= beta:
                    break

        if depth == self.depth:
            print(best_value)

        return best_value, best_move
