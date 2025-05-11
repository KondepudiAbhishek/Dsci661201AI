import pygame
import sys
import torch
from engine.game import SnakeGame
from env import SnakeEnv
from dqn.dqn import DQN

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Serpent Sprint - Trained Agent")

# Load environment and trained model
env = SnakeEnv()
model = DQN()
model.load_state_dict(torch.load("dqn_snake_model.pth"))
model.eval()

# Setup game
game = SnakeGame(screen)
clock = pygame.time.Clock()

# Mapping index to direction
direction_map = {0: "UP", 1: "DOWN", 2: "LEFT", 3: "RIGHT"}

def main():
    while not game.quit:
        game.handle_input()  # for quitting or restarting

        # Only let the AI play if game is started and not dead
        if game.started and not game.dead:
            state = env.get_state()
            state_tensor = torch.tensor(state, dtype=torch.float32).unsqueeze(0)

            with torch.no_grad():
                q_values = model(state_tensor)
            action = torch.argmax(q_values).item()
            game.board.set_direction(direction_map[action])

            env.set_direction(action)
            env.board = game.board  # sync board to keep consistent

            game.update()

        game.draw()
        pygame.display.flip()
        clock.tick(game.fps)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
