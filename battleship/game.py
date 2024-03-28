import pygame

from battleship.menu import DisplayMenu


class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()

        pygame.display.set_caption("World Domination")
        pygame.display.set_icon(pygame.image.load("images/icon.png"))
        self.clock.tick(60)

        self.menu = DisplayMenu()

    def loop(self):
        while True:
            if self.menu.exit:
                return
            self.menu.show()
