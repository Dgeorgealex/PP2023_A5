MOUSE = 1
"""Integer value representing mouse
"""
WALLS = 0
"""Integer value representing walls
"""

ROWS = 11
"""Number of rows in the map
"""
COLS = 11
"""Number og columns in the map
"""

WIDTH = 740
"""Width of the game window
"""
HEIGHT = 650
"""Height of the game window
"""

FPS = 60
"""Frames per second
"""

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (102, 255, 102)
ORANGE = (255, 153, 51)
BROWN = (153, 102, 51)

HEX_LENGTH = 30
"""The side length of a hexagon from the map
"""
FIRST_HEX = (100, 100)
"""The position of the hexagon in the top left corner on the game window
"""

MOUSE_DIRECTIONS_ODD = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (0, -1))
"""The directions a mouse can move when of a odd row
"""
MOUSE_DIRECTIONS_EVEN = ((-1, -1), (-1, 0), (0, 1), (1, 0), (1, -1), (0, -1))
"""The directions a mouse can mode when on a even row
"""

COOLING = 0.1
"""Cooling factor, helps when computing the evaluation function
"""
EPS = 0.00000000001
"""Error - also helps when computing evaluation function 
"""

WHO_IS_AI = MOUSE
"""Can be set to MOUSE of WALLS. It represents the player that the AI will be
"""
