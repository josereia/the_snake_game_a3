import pygame
import consts
from snake import Snake
from food import Food


pygame.init()

screen = pygame.display.set_mode(consts.screen)
clock = pygame.time.Clock()
running = True

food = Food(screen)
snake = Snake(
    food=food,
    screen=screen,
    position=(consts.screen[0] / 2, consts.screen[1] / 2),
    velocity=(0, 0),
    pixels=[],
    size=1,
)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            snake.dir(event.key)

    screen.fill(consts.bg_color)

    food.paint()

    snake.move()
    snake.gen()
    snake.paint()

    pygame.display.update()

    snake.eat()

    clock.tick(consts.fps)

pygame.quit()
