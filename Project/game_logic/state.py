import numpy as np
from .constants import *
from . import utils

import math
import pygame


class State:
    def __init__(self):
        self.game_matrix = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        self._init_mouse_and_walls()
        self.turn = WALLS
        self.mouse_pos = (5, 5)

    def _init_mouse_and_walls(self):
        self.game_matrix[5][5] = 2
        nr_walls = np.random.randint(5, 21)
        for _ in range(nr_walls):
            row = np.random.randint(0, ROWS)
            col = np.random.randint(0, COLS)
            if self.game_matrix[row][col] == 0:
                self.game_matrix[row][col] = 1

    def draw_state(self, window):
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
        if self.turn == MOUSE and utils.on_border_matrix(self.mouse_pos[0], self.mouse_pos[1]):
            self.game_matrix[self.mouse_pos[0]][self.mouse_pos[1]] = 0
            return True
        return False

    def losing_state(self):
        if self.turn == MOUSE:
            moves = self.possible_moves()
            if len(moves) == 0:
                return True
        return False

    def possible_moves(self):
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
