# Game settings
RESOLUTION = (1200, 800)
BACKGROUND_COLOR = (0, 0, 50)
FONT_SIZE = 30
FONT_COLOR = (255, 255, 255)
CELL_SIZE = 48.2
CELL_WIDTH = 15
CELL_HEIGHT = 10

HIT_POSITION = (975, 675)
USER_SCORE_POSITION = (70, 650)
CPU_SCORE_POSITION = (70, 700)
HEADING_LEFT_POSITION = (180, 50)
HEADING_RIGHT_POSITION = (780, 50)

# Volume consants
LOW_VOLUME = 0.01
MEDIUM_VOLUME = 0.1
HIGH_VOLUME = 0.3


# Matrix constants
MATRIX_X = 70
MATRIX_Y = 100
MATRIX_RESOLUTION = (498.6, 495)

# Misc
MARKER_RESOLUTION = (40, 40)
COMPUTER_BOARD_LEFT_MARGIN = 548.6

from enum import Enum


class ShipType(Enum):
    MEDIUM = 1
    BIG = 2
    SMALL = 3


SHIPS = {
    ShipType.MEDIUM: {
        "marker": 1,
        "rows": 6,
        "columns": 9,
        "image_path": "images/ship1.png",
        "resolution": (180, 40),
        "parts": 4,
        "y_offset": 0,
        "x_offset": 15,
        "positions": [(0, 0), (0, 1), (0, 2), (0, 3)],
    },
    ShipType.BIG: {
        "marker": 2,
        "rows": 7,
        "columns": 8,
        "image_path": "images/ship2.png",
        "resolution": (150, 110),
        "parts": 6,
        "y_offset": 0,
        "x_offset": 10,
        "positions": [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)],
    },
    ShipType.SMALL: {
        "marker": 3,
        "rows": 7,
        "columns": 9,
        "image_path": "images/ship3.png",
        "resolution": (120, 40),
        "parts": 3,
        "y_offset": 0,
        "x_offset": 15,
        "positions": [(0, 0), (0, 1), (0, 2)],
    },
}

HIT = -2
MISS = -1
EMPTY = 0
