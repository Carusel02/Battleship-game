import os
import random
import time
from random import randint

import pygame
from pygame import mixer

from battleship.board import Board
from battleship.constants import *


def guess_bot(board: "Board") -> tuple[int, int]:
    row = randint(0, 9)
    column = randint(0, 9)
    if not board.has_more_turns:
        return None, None

    while board.matrix[row][column] == MISS:
        row = randint(0, 9)
        column = randint(0, 9)
    return row, column


def load_images(path):
    images = []
    for file_name in os.listdir(path):
        image = pygame.image.load(path + os.sep + file_name)
        images.append(image)
    return images


def play_music(sound_file, volume=LOW_VOLUME, indefinitely=False):
    def decorator(menu_function):
        def wrapper(*args, **kwargs):
            mixer.music.load(sound_file)
            mixer.music.set_volume(volume)
            mixer.music.play(-1 if indefinitely else 0)
            menu_function(*args)
            mixer.music.stop()

        return wrapper

    return decorator


class ItemMenu:
    def __init__(self, menu):
        self.menu = menu
        self.screen = pygame.display.get_surface()

    def show(self):
        raise NotImplementedError("You need to implement `show` method.")


class StartMenu(ItemMenu):
    @play_music("sound/menu_sound.mp3", indefinitely=True)
    def show(self):
        while True:
            for action in pygame.event.get():
                if action.type == pygame.QUIT:
                    return
                if action.type == pygame.KEYDOWN:
                    if action.key == pygame.K_s:
                        self.menu.set_active(GameMenu)
                        return
                    if action.key == pygame.K_q:
                        self.menu.exit = True
                        return
            self.screen.fill(BACKGROUND_COLOR)
            font = pygame.font.Font("font/pixelated.ttf", 40)
            start = font.render("PRESS                FOR START", True, FONT_COLOR)
            quit = font.render("PRESS                FOR QUIT", True, FONT_COLOR)
            font2 = pygame.font.Font("font/pixelated.ttf", 70)
            title = font2.render("WORLD DOMINATION", True, (74, 198, 183))
            self.screen.blit(start, (330, 570))
            self.screen.blit(quit, (330, 670))
            self.screen.blit(title, (220, 320))
            vector_image = load_images("images")
            battle_ship = pygame.transform.scale(vector_image[0], (500, 300))
            self.screen.blit(battle_ship, (320, 0))

            # Display names
            name_font = pygame.font.Font("font/pixelated.ttf", 20)
            diana = name_font.render("DIANA MARIA STEFAN", True, FONT_COLOR)
            mary = name_font.render("MARIA CRISTINA COSTEA", True, FONT_COLOR)
            marius = name_font.render("MARIUS DANIEL MARIN", True, FONT_COLOR)
            stefan = name_font.render("STEFAN VALENTIN IONESCU", True, FONT_COLOR)
            self.screen.blit(diana, (10, 5))
            self.screen.blit(marius, (10, 760))
            self.screen.blit(mary, (900, 5))
            self.screen.blit(stefan, (865, 760))

            keycap_s = pygame.image.load("images/keycapS.png")
            keycap_q = pygame.image.load("images/keycapQ.png")
            self.screen.blit(pygame.transform.scale(keycap_s, (60, 60)), (530, 570))
            self.screen.blit(pygame.transform.scale(keycap_q, (60, 60)), (530, 670))
            time.sleep(0.3)
            pygame.display.update()
            self.screen.blit(
                pygame.transform.scale(keycap_s, (70, 70)), (530 - 5, 570 - 5)
            )
            self.screen.blit(
                pygame.transform.scale(keycap_q, (70, 70)), (530 - 5, 670 - 5)
            )
            time.sleep(0.3)
            pygame.display.update()
            self.screen.blit(
                pygame.transform.scale(keycap_s, (80, 80)), (530 - 10, 570 - 10)
            )
            self.screen.blit(
                pygame.transform.scale(keycap_q, (80, 80)), (530 - 10, 670 - 10)
            )
            time.sleep(0.3)
            pygame.display.update()


class GameMenu(ItemMenu):
    def __init__(self, menu):
        super().__init__(menu)
        self.cpu_board = Board(MATRIX_X, MATRIX_Y, is_bot=True)
        self.board = Board(MATRIX_X + COMPUTER_BOARD_LEFT_MARGIN, MATRIX_Y)
        self.font = pygame.font.Font("font/pixelated.ttf", FONT_SIZE)

    def show(self):
        score = ""
        bots_turn = False
        while True:
            for action in pygame.event.get():
                if not bots_turn:
                    if action.type == pygame.KEYDOWN:
                        if action.key in [
                            pygame.K_RIGHT,
                            pygame.K_LEFT,
                            pygame.K_UP,
                            pygame.K_DOWN,
                        ]:
                            self.cpu_board.handle_movement(action.key)
                        elif action.key == pygame.K_x:
                            score, bots_turn = self.user_shoots()

            if bots_turn:
                score, bots_turn = self.bot_shoots()
            if self.board.ships_left == 0 or self.cpu_board.ships_left == 0:
                self.menu.set_active(
                    LostGameMenu if self.board.ships_left == 0 else WinGameMenu
                )
                return
            self.display(score)

    def user_shoots(self) -> tuple[str, bool]:
        score = self.cpu_board.guess()
        return score, score == "NO"

    def bot_shoots(self) -> tuple[str, bool]:
        self.board.cursor.move(*guess_bot(self.board))
        score = self.board.guess()
        return score, score == "YES"

    def display(self, score: str) -> None:
        self.screen.fill(BACKGROUND_COLOR)
        self._display_boards()
        self._display_scores(score)
        pygame.display.update()

    def _display_boards(self) -> None:
        self.board.render()
        self.cpu_board.render()

    def _display_scores(self, score: int) -> None:
        self.screen.blit(
            self.font.render(f"Hit : {score}", True, FONT_COLOR), HIT_POSITION
        )

        score_user = self.font.render(
            f"Score user: {str(len(self.cpu_board.ships) - self.cpu_board.ships_left)}",
            True,
            FONT_COLOR,
        )
        score_cpu = self.font.render(
            f"Score opponent: {str(len(self.board.ships) - self.board.ships_left)}",
            True,
            FONT_COLOR,
        )
        self.screen.blit(score_user, USER_SCORE_POSITION)
        self.screen.blit(score_cpu, CPU_SCORE_POSITION)

        heading_left = self.font.render("Opponent's map", True, FONT_COLOR)
        heading_right = self.font.render("Your map", True, FONT_COLOR)
        self.screen.blit(heading_left, HEADING_LEFT_POSITION)
        self.screen.blit(heading_right, HEADING_RIGHT_POSITION)


class EndGameMenu(ItemMenu):
    def show(self):
        image1 = pygame.transform.scale(self.image, (520, 338))
        image2 = pygame.transform.scale(self.image, (560, 364))
        image3 = pygame.transform.scale(self.image, (600, 390))

        for _ in range(5):
            self.screen.fill(BACKGROUND_COLOR)
            pygame.display.update()
            self.screen.blit(image1, (340, 231))
            pygame.display.update()
            time.sleep(0.3)
            self.screen.fill(BACKGROUND_COLOR)
            self.screen.blit(image2, (320, 218))
            pygame.display.update()
            time.sleep(0.3)
            self.screen.fill(BACKGROUND_COLOR)
            self.screen.blit(image3, (300, 205))
            pygame.display.update()
            time.sleep(0.3)

        self.menu.set_active(StartMenu)


class WinGameMenu(EndGameMenu):
    def __init__(self, menu):
        super().__init__(menu)
        self.image = pygame.image.load("images/win.png")

    @play_music("sound/win_game.wav")
    def show(self):
        super().show()


class LostGameMenu(EndGameMenu):
    def __init__(self, menu):
        super().__init__(menu)
        self.image = pygame.image.load("images/game_over.png")

    @play_music("sound/lost_game.wav", indefinitely=True)
    def show(self):
        super().show()


class DisplayMenu:
    def __init__(self):
        self.active = StartMenu
        self.screen = pygame.display.set_mode(RESOLUTION)
        self.menus = [
            StartMenu(self),
            GameMenu(self),
            WinGameMenu(self),
            LostGameMenu(self),
        ]
        self.exit = False

    def show(self):
        for menu in self.menus:
            if menu.__class__ == self.active:
                menu.show()

    def set_active(self, menu):
        self.active = menu
