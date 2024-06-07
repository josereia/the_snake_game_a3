import pygame
import pygame_gui

import consts
from food import Food
from ranking import add_ranking, rankings  # Importa a função e o array de rankings
from snake import Snake


def restart_game(manager):
    """Reseta o jogo para o estado inicial"""
    global snake, food, game_over, running, ranking_window
    food = Food(screen)
    snake = Snake(
        food=food,
        screen=screen,
        position=(consts.screen[0] / 2, consts.screen[1] / 2),
        velocity=(0, 0),
        pixels=[],
        size=1,
    )
    game_over = False

    # Fecha a janela do ranking, se existir
    if ranking_window is not None:
        ranking_window.kill()
        ranking_window = None


def main():
    global screen, snake, food, game_over, running, ranking_window
    pygame.init()

    screen = pygame.display.set_mode(consts.screen)
    clock = pygame.time.Clock()
    running = True
    game_over = False  # Variável para controlar o estado do jogo
    ranking_window = None  # Inicializa a janela do ranking como None

    manager = pygame_gui.UIManager(consts.screen)

    window_width = 200
    window_height = 50  # Ajusta a altura para acomodar a pontuação
    window_rect = pygame.Rect(consts.screen[0] - window_width - 10, 10, window_width, window_height)

    side_panel = pygame_gui.elements.UIPanel(
        relative_rect=window_rect,
        starting_height=1,
        manager=manager
    )

    info_label = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect(10, 10, window_width - 20, 30),
        text="Pontuação: 0",
        manager=manager,
        container=side_panel
    )

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
        time_delta = clock.tick(consts.fps) / 1000.0  # Calcula o delta de tempo para a atualização do manager

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                snake.dir(event.key)

            manager.process_events(event)  # Processa eventos do pygame_gui

            if event.type == pygame.USEREVENT:
                if event.ui_element == new_game_button:
                    restart_game(manager)
                elif event.ui_element == quit_button:
                    running = False

        screen.fill(consts.bg_color)

        # Atualiza e desenha o pygame_gui
        manager.update(time_delta)
        info_label.set_text(f"Pontuação: {snake.size - 1}")

        # Desenha e movimenta a cobra e comida apenas se o jogo não terminou
        if not game_over:
            food.paint()
            snake.move()
            snake.gen()
            snake.paint()
            snake.eat()

            # Verifica se o jogo terminou
            if snake.game_over_condition():
                game_over = True
                add_ranking("Jogador", snake.size - 1)  # Atualiza o ranking com a pontuação final

                # Cria uma nova janela modal para mostrar o ranking e opções
                ranking_window_rect = pygame.Rect((consts.screen[0] - 300) // 2, (consts.screen[1] - 400) // 2, 300,
                                                  400)
                ranking_window = pygame_gui.elements.UIWindow(
                    rect=ranking_window_rect,
                    window_display_title='Game Over',
                    manager=manager,
                    object_id='#game_over_window'
                )

                # Adiciona os botões de nova partida e sair
                new_game_button = pygame_gui.elements.UIButton(
                    relative_rect=pygame.Rect(50, 320, 200, 50),
                    text='Novo Jogo',
                    manager=manager,
                    container=ranking_window
                )

                quit_button = pygame_gui.elements.UIButton(
                    relative_rect=pygame.Rect(50, 380, 200, 50),
                    text='Sair',
                    manager=manager,
                    container=ranking_window
                )

                # Adiciona os rankings na janela modal
                for i, rank in enumerate(rankings[:10]):
                    pygame_gui.elements.UILabel(
                        relative_rect=pygame.Rect(10, 10 + i * 30,
                                                  280, 30),
                        text=f"{i + 1}. {rank['name']}: {rank['score']}",
                        manager=manager,
                        container=ranking_window
                    )

        manager.draw_ui(screen)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
