import pygame
from engine.board import GameBoard
from engine.score import ScoreDisplay
from engine.sound import SoundPlayer

class SnakeGame:
    def __init__(self, screen):
        self.screen = screen
        self.board = GameBoard()
        self.score = ScoreDisplay(24)
        self.sounds = SoundPlayer()
        self.dead = False
        self.quit = False
        self.fps = 7
        self.started = False

        self.title_font = pygame.font.SysFont("impact", 60, bold=True)
        self.menu_font = pygame.font.SysFont("comicsansms", 28)

        self.sounds.play_background()  # Play background music before starting

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.quit = True
                if event.key == pygame.K_r and self.dead:
                    self.board.reset()
                    self.dead = False
                    self.started = False
                    self.sounds.play_background()
                if not self.started:
                    self.started = True
                    self.sounds.stop_background()  # Stop background music once game starts

                if event.key == pygame.K_UP:
                    self.board.set_direction("UP")
                elif event.key == pygame.K_DOWN:
                    self.board.set_direction("DOWN")
                elif event.key == pygame.K_LEFT:
                    self.board.set_direction("LEFT")
                elif event.key == pygame.K_RIGHT:
                    self.board.set_direction("RIGHT")

    def update(self):
        if self.dead or not self.started:
            return

        ate = self.board.move_snake()

        if self.board.dead:
            self.dead = True
            self.sounds.play_death()
            self.sounds.play_background()  # Restart background music after death
        elif ate:
            self.sounds.play_chew()


    def draw(self):
        self.screen.fill((0, 0, 0))
        self.board.draw(self.screen)
        self.score.draw(self.screen, self.board.get_score())

        if self.dead:
            self.show_game_over()

    def show_game_over(self):
        title_font = pygame.font.SysFont("arial", 60, bold=True)
        text = title_font.render("GAME OVER!", True, (255, 0, 0))
        rect = text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2 - 30))
        self.screen.blit(text, rect)

        option_font = pygame.font.SysFont("verdana", 20)
        option = option_font.render("Press R to Restart or Q to Quit", True, (0, 0, 0))
        opt_rect = option.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2 + 20))
        self.screen.blit(option, opt_rect)
