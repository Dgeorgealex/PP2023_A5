import numpy as np
from .constants import *
from . import utils

import math
import pygame


class State:
    """Class that represents a state of the game

    Attributes:
        game_matrix : "matrix"
            The current state of the game 0 - free, 1 - wall, 2- moue
        turn : int
            The current turn (WALLS or MOUSE)
        mouse_pos : tuple of int
            The current position of the mouse (row, col)

    Methods:
        copy():
            Creates a copy of the current state.
        _init_mouse_and_walls():
            Initializes the mouse and walls in the initial game state
        draw_state(window):
            Draws the current state on the specified game window
        winning_state():
            Checks if the game is in a winning state for the mouse.
        losing_state():
            Checks if the game is in a losing state for the mouse.
        possible_moves():
            Returns a list of possible moves for the current player
        move(row, col):
            Performs a move on the game board.
        evaluate():
            Returns the current state for the AI player.
        shortest_path():
            Computes the score of the current state using a heuristic based on the shortest paths
        """
    def __init__(self):
        """Initializes the current state
        """
        self.game_matrix = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        self._init_mouse_and_walls()
        self.turn = WALLS
        self.mouse_pos = (5, 5)

    def copy(self):
        """Returns a copy of the current state
        :return: State
        """
        new_instance = State()
        new_instance.game_matrix = [row[:] for row in self.game_matrix]
        new_instance.turn = self.turn
        new_instance.mouse_pos = self.mouse_pos
        return new_instance

    def _init_mouse_and_walls(self):
        """Initializes the mouse and walls positions at the beginning of the game
        """
        self.game_matrix[5][5] = 2
        nr_walls = np.random.randint(5, 10)
        for _ in range(nr_walls):
            row = np.random.randint(0, ROWS)
            col = np.random.randint(0, COLS)
            if self.game_matrix[row][col] == 0:
                self.game_matrix[row][col] = 1

    def draw_state(self, window):
        """Draws the current state on the

        :param window: pygame.Surface
            The game window
        """
        window.fill(WHITE)
        for row in range(11):
            for col in range(11):
                x, y = utils.get_center(row, col)

                utils.draw_hexagon(x, y, HEX_LENGTH, window, GREEN)
                utils.draw_hexagon(x, y, HEX_LENGTH, window, BLACK, 2)

                if self.game_matrix[row][col] == 1:
                    utils.draw_hexagon(x, y, HEX_LENGTH, window, BROWN)
                    utils.draw_hexagon(x, y, HEX_LENGTH, window, BLACK, 2)

                if self.game_matrix[row][col] == 2:
                    utils.draw_hexagon(x, y, HEX_LENGTH - 10, window, ORANGE)

    def winning_state(self):
        """Check if the current state is a winning state
        :return: bool
            True if the mouse wins, False if the mouse does not win
        """
        if self.turn == MOUSE and utils.on_border_matrix(self.mouse_pos[0], self.mouse_pos[1]):
            return True
        return False

    def losing_state(self):
        """Check if the current state is a losing state
        :return: bool
            True if the mouse loses, False if the mouse does not lose
        """
        if self.turn == MOUSE:
            moves = self.possible_moves()
            if len(moves) == 0:
                return True
        return False

    def possible_moves(self):
        """Returns the possible moves of the current player (MOUSE or WALLS)
        :return: list of tuples of int
            The possible moves
        """
        moves = []
        if self.turn == MOUSE:
            if self.mouse_pos[0] % 2 == 1:
                mouse_directions = MOUSE_DIRECTIONS_ODD
            else:
                mouse_directions = MOUSE_DIRECTIONS_EVEN

            for (dx, dy) in mouse_directions:
                m_row, m_col = self.mouse_pos[0] + dx, self.mouse_pos[1] + dy
                if not utils.outside_matrix(m_row, m_col) and self.game_matrix[m_row][m_col] == 0:
                    moves.append((m_row, m_col))

        else:
            for row in range(ROWS):
                for col in range(COLS):
                    if self.game_matrix[row][col] == 0:
                        moves.append((row, col))

        return moves

    def move(self, row, col):
        """Check if the move is valid for the current player(MOUSE or WALLS) and if it is it changes the state
        :param row: int
            The row of the move
        :param col: int
            The column of the row
        :return: bool
            True is the move is valid ant the state changed, False otherwise
        """
        moves = self.possible_moves()
        if (row, col) not in moves:
            return False

        if self.turn == WALLS:
            self.game_matrix[row][col] = 1
            self.turn = MOUSE

        else:
            m_row, m_col = self.mouse_pos
            self.game_matrix[m_row][m_col] = 0
            self.game_matrix[row][col] = 2
            self.turn = WALLS
            self.mouse_pos = (row, col)

        return True

    def evaluate(self):
        """Depending on whose turn it is (MOUSE or WALLS) it returns the value of the state
        :return: float
            The value of the state
        """
        if WHO_IS_AI == MOUSE:
            return self.shortest_path()
        else:
            return -self.shortest_path()

    def shortest_path(self):
        """The heuristic called for computing the value of the state.
        It is based on the lengths of the shortest paths from the mouse to the borders
        :return: float
            The value of the state
        """
        q = utils.Queue()
        q.push(self.mouse_pos)
        a = [row[:] for row in self.game_matrix]

        for row in range(ROWS):
            for col in range(COLS):
                if a[row][col] == 1:
                    a[row][col] = -1
                elif a[row][col] == 2:
                    a[row][col] = 1

        while not q.is_empty():
            row, col = q.pop()

            if row % 2 == 1:
                directions = MOUSE_DIRECTIONS_ODD
            else:
                directions = MOUSE_DIRECTIONS_EVEN

            for dx, dy in directions:
                new_row = row + dx
                new_col = col + dy
                if utils.outside_matrix(new_row, new_col):
                    continue
                elif a[new_row][new_col] == 0:
                    a[new_row][new_col] = a[row][col] + 1
                    q.push((new_row, new_col))

        score = 0
        for row in range(ROWS):
            for col in range(COLS):
                if utils.on_border_matrix(row, col) and a[row][col] > 0:
                    if a[row][col] > 10:
                        score += COOLING ** 10
                    else:
                        score = score + COOLING ** (a[row][col] - 1)

        nr = 0
        for row in range(ROWS):
            for col in range(COLS):
                if a[row][col] > 0:
                    nr += 1
        score += nr * (COOLING ** 15)

        return score
