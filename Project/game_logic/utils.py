import pygame
from .constants import *
import math


def get_hexagon_points(center_x, center_y, side_length):
    hexagon_points = []
    for i in range(6):
        angle = math.radians(60 * i - 30)
        x = center_x + side_length * math.cos(angle)
        y = center_y + side_length * math.sin(angle)
        hexagon_points.append((x, y))
    return hexagon_points


def draw_hexagon(center_x, center_y, side_length, window, color, width=0):
    hexagon_points = get_hexagon_points(center_x, center_y, side_length)
    pygame.draw.polygon(window, color, hexagon_points, width)


def in_hexagon(center_x, center_y, x, y):
    hexagon_points = get_hexagon_points(center_x, center_y, HEX_LENGTH)
    for i in range(6):
        x1, y1 = hexagon_points[i]
        x2, y2 = hexagon_points[(i + 1) % 6]
        if (x - x1) * (y2 - y1) - (y - y1) * (x2 - x1) > 0:
            return False

    return True


def get_center(row, col):
    x, y = FIRST_HEX
    x = x + col * HEX_LENGTH * (3 ** 0.5)
    y = y + row * HEX_LENGTH * 3 / 2

    if row % 2 == 1:
        x = x + HEX_LENGTH * (3 ** 0.5) / 2

    return x, y


def get_matrix_position(x, y):
    pos = (-1, -1)
    for row in range(ROWS):
        for col in range(COLS):
            center_x, center_y = get_center(row, col)
            if in_hexagon(center_x, center_y, x, y):
                pos = (row, col)
    return pos


def outside_matrix(row, col):
    return row < 0 or row >= ROWS or col < 0 or col >= COLS


def on_border_matrix(row, col):
    return row == 0 or col == 0 or row == ROWS-1 or col == COLS-1