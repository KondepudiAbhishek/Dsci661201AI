import pygame
from engine.game import SnakeGame

# Initialize and run the game
def main():
    pygame.init()
    screen_size = 600  # fits nicely on all screens
    screen = pygame.display.set_mode((screen_size, screen_size))
    pygame.display.set_caption("Serpent Sprint")
    clock = pygame.time.Clock()
    game = SnakeGame(screen)

    while not game.quit:
        game.handle_input()
        game.update()
        game.draw()
        pygame.display.flip()
        clock.tick(game.fps)

    pygame.quit()

if __name__ == "__main__":
    main()


