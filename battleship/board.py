import pygame

from battleship.constants import (CELL_HEIGHT, CELL_SIZE, CELL_WIDTH, EMPTY,
                                  HIT, MARKER_RESOLUTION, MATRIX_RESOLUTION,
                                  MISS, ShipType)
from battleship.debug import debug
from battleship.ship import Ship


class Cursor:
    def __init__(self, x: float, y: float, image_path: str):
        self.surface = pygame.display.get_surface()
        self.x = x + CELL_WIDTH
        self.y = y + CELL_HEIGHT
        # These values are topleft corner of a Board
        # We will use them to draw cursor on Board
        self._initial_x = self.x
        self._initial_y = self.y
        self.image = pygame.transform.scale(
            pygame.image.load(image_path), MARKER_RESOLUTION
        )
        self.row = 0
        self.column = 0

    def render(self):
        self.surface.blit(self.image, (self.x, self.y))

    def move(self, row, column):
        self.row = row
        self.y = self._initial_y + row * CELL_SIZE

        self.column = column
        self.x = self._initial_x + column * CELL_SIZE

    def down(self):
        if self.row < 9:
            self.move(self.row + 1, self.column)

    def up(self):
        if self.row > 0:
            self.move(self.row - 1, self.column)

    def left(self):
        if self.column > 0:
            self.move(self.row, self.column - 1)

    def right(self):
        if self.column < 9:
            self.move(self.row, self.column + 1)


class Board:
    def __init__(self, x: float, y: float, is_bot: bool = False):
        self.surface = pygame.display.get_surface()
        self.miss_sound = pygame.mixer.Sound("sound/cross_sound.wav")
        self.miss_sound.set_volume(0.1)
        self.hit_sound = pygame.mixer.Sound("sound/hit_yes.mp3")
        self.hit_sound.set_volume(0.3)
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(
            pygame.image.load("images/matrix_background.png"), MATRIX_RESOLUTION
        )
        self._matrix = [[EMPTY for i in range(10)] for j in range(10)]
        self.ships = [
            Ship(ShipType.BIG),
            Ship(ShipType.MEDIUM),
            Ship(ShipType.SMALL),
        ]
        self.place_ships()
        self.cursor = Cursor(self.x, self.y, "images/cancel.png")
        self.not_here = pygame.transform.scale(
            pygame.image.load("images/nothing_here.png"), MARKER_RESOLUTION
        )
        self.hit_here = pygame.transform.scale(
            pygame.image.load(
                "images/square.png" if is_bot else "images/square_bot.png"
            ),
            MARKER_RESOLUTION,
        )

    @property
    def matrix(self):
        return self._matrix

    @property
    def ships_left(self):
        return list(map(lambda ship: ship.is_dead, self.ships)).count(False)

    @property
    def has_more_turns(self):
        for row in self._matrix:
            for el in row:
                if el == EMPTY:
                    return True
        return False

    def handle_movement(self, key: int) -> None:
        if key == pygame.K_RIGHT:
            self.cursor.right()
        elif key == pygame.K_LEFT:
            self.cursor.left()
        elif key == pygame.K_DOWN:
            self.cursor.down()
        elif key == pygame.K_UP:
            self.cursor.up()

    def place_ships(self):
        for ship in self.ships:
            row, column = ship.get_row_and_column(self)
            ship_x = self.x + column * CELL_SIZE
            ship_y = self.y + row * CELL_SIZE
            ship.place(ship_x, ship_y, self)
            self.place(row, column, ship)

    def can_place_ship(self, row: int, column: int, ship: Ship) -> bool:
        for row_offset, column_offset in ship.positions:
            try:
                if self._matrix[row + row_offset][column + column_offset]:
                    return False
            except IndexError:
                return False
        return True

    def place(self, row: int, column: int, ship: Ship):
        for row_offset, column_offset in ship.positions:
            self._matrix[row + row_offset][column + column_offset] = ship.marker

    def render(self):
        self.surface.blit(self.image, (self.x, self.y))
        self._render_matrix()

        for ship in self.ships:
            ship.render()

        self.cursor.render()

    def _render_matrix(self):
        for i, row in enumerate(self._matrix):
            for j, element in enumerate(row):
                if element == MISS:
                    self.surface.blit(
                        self.not_here,
                        (
                            self.x + CELL_SIZE * j + CELL_WIDTH,
                            self.y + CELL_SIZE * i + CELL_HEIGHT,
                        ),
                    )
                elif element == HIT:
                    self.surface.blit(
                        self.hit_here,
                        (
                            self.x + CELL_SIZE * j + CELL_WIDTH,
                            self.y + CELL_SIZE * i + CELL_HEIGHT,
                        ),
                    )

    def get_value_at_cursor(self):
        return self._matrix[self.cursor.row][self.cursor.column]

    def set_value_at_cursor(self, value: int) -> None:
        self._matrix[self.cursor.row][self.cursor.column] = value

    def guess(self) -> str:
        cursor_value = self.get_value_at_cursor()
        if cursor_value == EMPTY:
            self.set_value_at_cursor(MISS)
            self.miss_sound.play()
            return "NO"
        if cursor_value == MISS:
            return ""
        # This is scenario when there is a hit
        try:
            ship = next(filter(lambda s: s.marker == cursor_value, self.ships))
            ship.hit()
        except StopIteration:
            return ""
        self.set_value_at_cursor(HIT)
        self.hit_sound.play()
        return "YES"
