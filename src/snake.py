import pygame

import consts
from food import Food


class Snake:
    screen: pygame.Surface
    food: Food
    position: tuple[float, float]
    velocity: tuple[float, float]
    pixels: list
    size: int
    gameOver: bool

    def __init__(
            self,
            screen: pygame.Surface,
            food: Food,
            position: tuple[float, float],
            velocity: tuple[float, float],
            pixels: list,
            size: int,
    ) -> None:
        self.screen = screen
        self.food = food
        self.position = position
        self.velocity = velocity
        self.pixels = pixels
        self.size = size
        self.gameOver = False

    def dir(self, key: int) -> None:
        """Sets the snake's direction"""
        if key == pygame.K_DOWN:
            self.velocity = (0, consts.pixel)
        elif key == pygame.K_UP:
            self.velocity = (0, -consts.pixel)
        elif key == pygame.K_RIGHT:
            self.velocity = (consts.pixel, 0)
        elif key == pygame.K_LEFT:
            self.velocity = (-consts.pixel, 0)

    def move(self) -> None:
        new_position = (
            self.position[0] + self.velocity[0],
            self.position[1] + self.velocity[1],
        )

        if new_position[0] < 0 or new_position[0] >= self.screen.get_width() or new_position[1] < 0 or new_position[
            1] >= self.screen.get_height():
            self.gameOver = True
        else:
            self.position = new_position

    def gen(self) -> None:
        """Generate a new position for snake"""
        self.pixels.append(self.position)
        if len(self.pixels) > self.size:
            del self.pixels[0]

        # Verifica colisão consigo mesma
        if self.pixels.count(self.position) > 1:
            self.gameOver = True

    def eat(self) -> None:
        """Increase the size of the snake if it has eaten"""
        if self.position == self.food.position:
            self.size += 1
            self.food.gen()

    def paint(self) -> None:
        """Draw snake in the current position"""
        for pixel in self.pixels:
            pygame.draw.rect(
                self.screen,
                consts.fg_color,
                [
                    pixel[0],
                    pixel[1],
                    consts.pixel,
                    consts.pixel,
                ],
            )

    def game_over_condition(self) -> bool:
        """Check if the game is over"""
        return self.gameOver
