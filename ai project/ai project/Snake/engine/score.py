# engine/score.py
import pygame

class ScoreDisplay:
    def __init__(self, size=24):
        self.font = pygame.font.SysFont("comicsansms", size, bold=True)
        self.color = (0, 0, 0)

    def draw(self, screen, score):
        text = self.font.render(f"Score: {score}", True, self.color)
        screen.blit(text, (20, 20))

