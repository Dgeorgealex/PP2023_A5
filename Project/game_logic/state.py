import numpy as np
from .constants import *
class State:
    def __init__(self):
        self.game_matrix = np.zeros((ROWS, COLS), dtype=int)
        self._init_mouse_and_walls()
        self.turn = WALLS

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


