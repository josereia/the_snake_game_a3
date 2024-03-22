import random
import pygame
import consts


class Food:
    screen: pygame.Surface
    position: tuple[int, int]

    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen
        self.gen()

    def gen(self) -> None:
        """Generate a new position for food"""
        randX = random.randrange(0, consts.screen[0] - consts.pixel)
        randY = random.randrange(0, consts.screen[1] - consts.pixel)
        x = round(randX / consts.pixel) * consts.pixel
        y = round(randY / consts.pixel) * consts.pixel

        self.position = (x, y)

    def paint(self) -> None:
        """Draw food in the current position"""
        pygame.draw.rect(
            self.screen,
            consts.fg_color,
            [
                self.position[0],
                self.position[1],
                consts.pixel,
                consts.pixel,
            ],
        )
