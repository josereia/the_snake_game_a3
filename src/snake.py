import pygame
import consts


class Snake:
    position: tuple[float, float]
    velocity: tuple[float, float]
    pixels: list
    size: int

    def __init__(
        self,
        position: tuple[float, float],
        velocity: tuple[float, float],
        pixels: list,
        size: int,
    ) -> None:
        self.position = position
        self.velocity = velocity
        self.pixels = pixels
        self.size = size

    def dir(self, key: int) -> None:
        if key == pygame.K_DOWN:
            self.velocity = (0, consts.pixel)
        elif key == pygame.K_UP:
            self.velocity = (0, -consts.pixel)
        elif key == pygame.K_RIGHT:
            self.velocity = (consts.pixel, 0)
        elif key == pygame.K_LEFT:
            self.velocity = (-consts.pixel, 0)

    def move(self) -> None:
        self.position = (
            self.position[0] + self.velocity[0],
            self.position[1] + self.velocity[1],
        )

    def gen(self) -> None:
        self.pixels.append(self.position)
        if len(self.pixels) > self.size:
            del self.pixels[0]

    def paint(self, screen: pygame.Surface) -> None:
        for pixel in self.pixels:
            pygame.draw.rect(
                screen,
                consts.fg_color,
                [
                    pixel[0],
                    pixel[1],
                    consts.pixel,
                    consts.pixel,
                ],
            )
