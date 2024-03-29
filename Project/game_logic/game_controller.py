from .state import State
from .constants import *
from ai_algorithms.minimax import MiniMax
import pygame
from . import utils


class Game:
    """Class that represents a game

    Attributes:
        state : State
            The current state of the game
        window : pygame.Surface
            The game window

    Methods:
        play_game(mode):
            Main method to play the game, allowing interaction with the AI or a friend.

        print_end_message(end_message):
            Displays the end message on the screen

    """
    def __init__(self):
        """Initializes the game class
        """
        self.state = State()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Trap the mouse')
        pygame.font.init()

    def play_game(self, mode):
        """Main method that contains the game loop and handles input from the user
        :param mode: str
            the game mode ('easy', 'normal', 'hard')
        """

        my_ai = None
        if mode != 'friend':
            play_with_ai = True
            my_ai = MiniMax(mode)
        else:
            play_with_ai = False

        run = True
        clock = pygame.time.Clock()
        end_message = ''
        game_ended = False
        while run:
            clock.tick(FPS)
            if self.state.winning_state():
                self.state.game_matrix[self.state.mouse_pos[0]][self.state.mouse_pos[1]] = 0
                end_message = 'Mouse wins'
                game_ended = True
            elif self.state.losing_state():
                end_message = 'Mouse loses'
                game_ended = True

            if not game_ended and play_with_ai and self.state.turn == WHO_IS_AI:
                ai_row, ai_col = my_ai.get_best_move(self.state)
                self.state.move(ai_row, ai_col)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN and not game_ended:
                    x, y = pygame.mouse.get_pos()
                    row, col = utils.get_matrix_position(x, y)
                    self.state.move(row, col)

            self.state.draw_state(self.window)

            if game_ended:
                self.print_end_message(end_message)

            pygame.display.update()

        pygame.quit()

    def print_end_message(self, end_message):
        """Prints the final message on the screen: if the mouse loses or not
        :param end_message: str
            The end message that must be printed on the screen
        """
        font = pygame.font.Font(None, 36)
        text = font.render(end_message, True, WHITE)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

        text_surface = pygame.Surface((text_rect.width + 20, text_rect.height + 10))
        text_surface.fill(BLACK)

        text_rect = text.get_rect(center=(text_surface.get_width() // 2, text_surface.get_height() // 2))
        text_surface.blit(text, text_rect)

        window_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.window.blit(text_surface, window_rect)

        mouse_image = pygame.image.load("assets/img.png")

        mouse_rect = mouse_image.get_rect(center=(WIDTH // 2, HEIGHT // 2 + text_rect.height + 100))
        self.window.blit(mouse_image, mouse_rect)
