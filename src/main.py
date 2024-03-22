import pygame
from snake import Snake
import consts

snake = Snake(
    position=(consts.screen[0] / 2, consts.screen[1] / 2),
    velocity=(0, 0),
    pixels=[],
    size=1,
)

pygame.init()

screen = pygame.display.set_mode(consts.screen)
clock = pygame.time.Clock()
running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            snake.dir(event.key)

    screen.fill(consts.bg_color)

    snake.move()
    snake.gen()
    snake.paint(screen)

    pygame.display.update()
    clock.tick(consts.fps)

pygame.quit()
