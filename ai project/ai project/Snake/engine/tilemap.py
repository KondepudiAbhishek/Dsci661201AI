import pygame

class TileMap:
    def __init__(self, cell_size):
        self.cell_size = cell_size
        self.color1 = (173, 219, 109)   # lighter green
        self.color2 = (167, 215, 95)    # darker green

    def draw_background(self, screen, rows, cols):
        for row in range(rows):
            for col in range(cols):
                tile_rect = pygame.Rect(
                    col * self.cell_size,
                    row * self.cell_size,
                    self.cell_size,
                    self.cell_size
                )
                color = self.color1 if (row + col) % 2 == 0 else self.color2
                pygame.draw.rect(screen, color, tile_rect)
