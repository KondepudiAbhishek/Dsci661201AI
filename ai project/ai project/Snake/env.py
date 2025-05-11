import numpy as np
from engine.board import GameBoard

class SnakeEnv:
    def __init__(self):
        self.board = GameBoard()
        self.done = False

    def reset(self):
        self.board.reset()
        self.done = False
        return self.get_state()

    def step(self, action):
        if self.done:
            return self.get_state(), 0, True, {}

        old_head = self.board.snake[0]
        apple = self.board.apple
        dist_before = abs(old_head[0] - apple[0]) + abs(old_head[1] - apple[1])

        self.set_direction(action)
        ate = self.board.move_snake()

        new_head = self.board.snake[0]
        dist_after = abs(new_head[0] - apple[0]) + abs(new_head[1] - apple[1])

        if self.board.dead:
            reward = -10
            self.done = True
        elif ate:
            reward = 10
        elif dist_after < dist_before:
            reward = 1  # moved closer to apple
        else:
            reward = -1  # moved away

        return self.get_state(), reward, self.done, {}

    def get_state(self):
        head = self.board.snake[0]
        direction = self.board.direction

        def danger(point):
            return (
                point in self.board.snake
                or point[0] < 0 or point[0] >= self.board.rows
                or point[1] < 0 or point[1] >= self.board.cols
            )

        danger_left = danger((head[0], head[1] - 1))
        danger_right = danger((head[0], head[1] + 1))
        danger_up = danger((head[0] - 1, head[1]))
        danger_down = danger((head[0] + 1, head[1]))

        apple = self.board.apple
        state = [
            # Dangers
            direction == (-1, 0) and danger_up or
            direction == (1, 0) and danger_down or
            direction == (0, -1) and danger_left or
            direction == (0, 1) and danger_right,

            direction == (-1, 0) and danger_right or
            direction == (1, 0) and danger_left or
            direction == (0, -1) and danger_up or
            direction == (0, 1) and danger_down,

            direction == (-1, 0) and danger_left or
            direction == (1, 0) and danger_right or
            direction == (0, -1) and danger_down or
            direction == (0, 1) and danger_up,

            # Apple location relative to head
            apple[0] < head[0],  # apple is up
            apple[0] > head[0],  # down
            apple[1] < head[1],  # left
            apple[1] > head[1],  # right

            # Current direction
            direction == (-1, 0),  # up
            direction == (1, 0),   # down
            direction == (0, -1),  # left
            direction == (0, 1),   # right
        ]

        return np.array(state, dtype=int)

    def set_direction(self, action):
        mapping = {
            0: "UP",
            1: "DOWN",
            2: "LEFT",
            3: "RIGHT"
        }
        self.board.set_direction(mapping[action])
