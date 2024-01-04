from .state import State
from .constants import *
from ai_algorithms.minimax import MiniMax
import pygame


class Game:
    def __init__(self):
        self.state = State()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Trap the mouse')

    def play(self, mode):
        if mode == 'friend':
            self.play_with_friend()

        else:
            minimax = MiniMax(mode)
            self.play_with_ai(minimax)

    def play_with_friend(self):
        run = True
        clock = pygame.time.Clock()

        while run:
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            self.state.draw_state(self.window)
            pygame.display.update()

        pygame.quit()

    def play_with_ai(self, ai):
        pass

