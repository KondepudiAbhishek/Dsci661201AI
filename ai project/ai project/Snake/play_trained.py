import pygame
import torch
from dqn.dqn import DQN
from env import SnakeEnv

def play_trained(model_path="dqn_snake_model.pth"):
    pygame.init()
    screen_size = 600
    screen = pygame.display.set_mode((screen_size, screen_size))
    pygame.display.set_caption("Snake AI - Trained Agent")
    clock = pygame.time.Clock()

    env = SnakeEnv()
    model = DQN()
    model.load_state_dict(torch.load(model_path))
    model.eval()

    cell_size = screen_size // env.board.rows
    state = env.reset()
    running = True

    while running and not env.done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Agent selects action
        with torch.no_grad():
            state_tensor = torch.tensor(state, dtype=torch.float32).unsqueeze(0)
            q_values = model(state_tensor)
            action = torch.argmax(q_values).item()

        next_state, _, done, _ = env.step(action)
        state = next_state

        # Draw board
        screen.fill((0, 0, 0))
        if env.board.apple:
            r, c = env.board.apple
            pygame.draw.rect(screen, (255, 0, 0), (c * cell_size, r * cell_size, cell_size, cell_size))

        for r, c in env.board.snake:
            pygame.draw.rect(screen, (0, 255, 0), (c * cell_size, r * cell_size, cell_size, cell_size))

        pygame.display.flip()
        clock.tick(10)

    pygame.quit()

if __name__ == "__main__":
    play_trained()
