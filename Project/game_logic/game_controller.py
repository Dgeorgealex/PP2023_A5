from .state import State
from .constants import *
from ai_algorithms.minimax import MiniMax
import pygame
from . import utils


class Game:
    def __init__(self):
        self.state = State()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Trap the mouse')
        pygame.font.init()

    def play(self, mode):
        if mode == 'friend':
            self.play_with_friend()

        else:
            minimax = MiniMax(mode)
            self.play_with_ai(minimax)

    def play_with_friend(self):
        run = True
        clock = pygame.time.Clock()

        end_message = ''
        game_ended = False
        while run:
            clock.tick(FPS)
            if self.state.winning_state():
                end_message = 'Mouse wins'
                game_ended = True
            elif self.state.losing_state():
                end_message = 'Mouse loses'
                game_ended = True

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN and not game_ended:
                    x, y = pygame.mouse.get_pos()
                    row, col = utils.get_matrix_position(x, y)
                    self.state.move(row, col)

            self.state.draw_state(self.window)

            if game_ended:
                font = pygame.font.Font(None, 36)
                text = font.render(end_message, True, (255, 255, 255))
                text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

                text_surface = pygame.Surface((text_rect.width + 20, text_rect.height + 10))
                text_surface.fill((0, 0, 0))  # Background color (black)

                text_rect = text.get_rect(center=(text_surface.get_width() // 2, text_surface.get_height() // 2))
                text_surface.blit(text, text_rect)

                window_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
                self.window.blit(text_surface, window_rect)

            pygame.display.update()

        pygame.quit()

    def play_with_ai(self, ai):
        pass
