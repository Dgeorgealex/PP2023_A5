import pygame
from .constants import *
import math
from collections import deque


def get_hexagon_points(center_x, center_y, side_length):
    """Computes the points coordinate values of a hexagon knowing the coordinates of the center and the side length
    :param center_x: float
        The x coordinate of the center
    :param center_y: float
        The y coordinate of the center
    :param side_length: int
        The side length of the hexagon
    :return: a list of tuples of floats
        The coordinate values of the hexagon points
    """
    hexagon_points = []
    for i in range(6):
        angle = math.radians(60 * i - 30)
        x = center_x + side_length * math.cos(angle)
        y = center_y + side_length * math.sin(angle)
        hexagon_points.append((x, y))
    return hexagon_points


def draw_hexagon(center_x, center_y, side_length, window, color, width=0):
    """Function that draws the hexagon using pygame
    :param center_x: float
        The x coordinate of the center
    :param center_y: float
        The y coordinate of the center
    :param side_length: int
        The side length
    :param window: pygame.Surface
        The window on which the function must draw
    :param color: tuple of int
        The color of the hexagon
    :param width:
        The width of the border
    """
    hexagon_points = get_hexagon_points(center_x, center_y, side_length)
    pygame.draw.polygon(window, color, hexagon_points, width)


def in_hexagon(center_x, center_y, x, y):
    """Checks if a point is inside a hexagon. Used to get the row and col of the player mouse
    :param center_x: float
        The x coordinate of the center
    :param center_y: float
        The y coordinate of the center
    :param x: int
        The x coordinate of the mouse
    :param y: int
        The y coordinate of the mouse
    :return: bool
        True if the mouse is inside the hexagon, False otherwise
    """
    hexagon_points = get_hexagon_points(center_x, center_y, HEX_LENGTH)
    for i in range(6):
        x1, y1 = hexagon_points[i]
        x2, y2 = hexagon_points[(i + 1) % 6]
        if (x - x1) * (y2 - y1) - (y - y1) * (x2 - x1) > 0:
            return False

    return True


def get_center(row, col):
    """A functon to compute the center coordinates of the hexagon on a specific row and column
    :param row: int
        The row of the hexagon
    :param col: int
        The column of the hexagon
    :return: tuple of floats
        The coordinates of the center
    """
    x, y = FIRST_HEX
    x = x + col * HEX_LENGTH * (3 ** 0.5)
    y = y + row * HEX_LENGTH * 3 / 2

    if row % 2 == 1:
        x = x + HEX_LENGTH * (3 ** 0.5) / 2

    return x, y


def get_matrix_position(x, y):
    """Used to return the row and column of the player mouse position. Checks all the hexagons in the map
    :param x: int
        The x coordinate of the player mouse
    :param y: int
        The y coordinate of the player mouse
    :return: tuple of ints
        The row and column of the user mouse. If the user click outside the map it will return (-1, -1)
    """
    pos = (-1, -1)
    for row in range(ROWS):
        for col in range(COLS):
            center_x, center_y = get_center(row, col)
            if in_hexagon(center_x, center_y, x, y):
                pos = (row, col)
    return pos


def outside_matrix(row, col):
    """Checks if the position is inside the map (11, 11) matrix
    :param row: int
    :param col: int
    :return: bool
    """
    return row < 0 or row >= ROWS or col < 0 or col >= COLS


def on_border_matrix(row, col):
    """
    Checks if the position is on the border of the map (11, 11) matrix
    :param row: int
    :param col: int
    :return: bool
    """
    return row == 0 or col == 0 or row == ROWS-1 or col == COLS-1


class Queue:
    """A class that defines a queue implementation. Used for implementing a Lee algorithm (BFS)
    Attributes:
        elements : array of tuples of int
            The positions that are currently in the queue

    Methods:
        is_empty() :
            Checks if the queue is empty
        size() :
            Returns the size of the queue
        push() :
            Adds an element to the queue
        pop() :
            Erases an element from the queue
    """
    def __init__(self):
        self.elements = deque()

    def is_empty(self):
        return len(self.elements) == 0

    def size(self):
        return len(self.elements)

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        return self.elements.popleft()

