import random
from game_logic.constants import WHO_IS_AI, MOUSE, WALLS
INF = 10000000


class MiniMax:
    """Class that represents a MiniMax object

    Attributes:
        depth : int
            The depth of the minimax tree

    Methods:
        get_best_move(state):
            Returns the best move found by the minimax algorithm

        minimax(state, alfa, beta, max_state, depth):
            Recursive minimax search, returns the MAX or the MIN value

    """
    def __init__(self, mode):
        """Initializes the MinMax class by setting the depth value based on the mode
        :param mode: string
            easy, normal or hard
        """
        if mode == 'easy':
            self.depth = 2
        elif mode == 'normal':
            self.depth = 3
        else:
            self.depth = 4
        if WHO_IS_AI == WALLS:
            self.depth -= 1

    def get_best_move(self, state):
        """Runs the minimax algorithm and returns the best move found

        :param state: State
            the current state of the game
        :return:
            Tuple containing the best found by the MiniMax algorithm
        """
        _, best_move = self.minimax(state, -INF, INF, True, self.depth)
        return best_move

    def minimax(self, state, alfa, beta, max_state, depth):
        """

        :param state: State
            The current state of the game
        :param alfa: int
            alfa from alfa beta pruning
        :param beta: int
            beta from alga beta pruning
        :param max_state: bool
            True if the layer is Max, False if it is Min
        :param depth: int
            The current depth of the search
        :return:
            Tuple containing the best move found and the evaluation function value
        """
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
