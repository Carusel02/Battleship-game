from enum import Enum
from random import randint

import pygame

from battleship.constants import CELL_SIZE, SHIPS, ShipType


class Ship:
    def __init__(self, type: ShipType, is_visible: bool = False) -> None:
        self.surface = pygame.display.get_surface()
        ship_data = SHIPS[type]
        self.image = pygame.transform.scale(
            pygame.image.load(ship_data["image_path"]), ship_data["resolution"]
        )

        self.is_visible = is_visible
        self.parts = ship_data["parts"]

        self.x_offset = ship_data["x_offset"]
        self.y_offset = ship_data["y_offset"]
        self.marker = ship_data["marker"]

        self.positions = ship_data["positions"]
        self.columns = ship_data["columns"]
        self.rows = ship_data["rows"]

    def render(self):
        if self.is_dead or self.is_visible:
            self.surface.blit(
                self.image, (self.x + self.x_offset, self.y + self.y_offset)
            )

    def place(self, x: float, y: float, board: "Board") -> None:
        self.x = x
        self.y = y

    @property
    def is_dead(self):
        return self.parts == 0

    def hit(self):
        if not self.is_dead:
            self.parts -= 1

    def get_row_and_column(self, board: "Board") -> tuple[int, int]:
        column = randint(0, self.columns)
        row = randint(0, self.rows)

        while not board.can_place_ship(row, column, self):
            column = randint(0, self.columns)
            row = randint(0, self.rows)
        return row, column
