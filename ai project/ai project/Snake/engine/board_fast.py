import random

class GameBoard:
    def __init__(self, rows=20, cols=20):
        self.rows = rows
        self.cols = cols
        self.reset()

    def reset(self):
        self.snake = [(10, 10), (10, 11), (10, 12)]
        self.direction = (0, -1)
        self.next_direction = (0, -1)
        self.dead = False
        self.apple = self.place_apple()

    def set_direction(self, direction):
        dir_map = {
            "UP": (-1, 0),
            "DOWN": (1, 0),
            "LEFT": (0, -1),
            "RIGHT": (0, 1)
        }
        new_dir = dir_map[direction]
        if (new_dir[0] * -1, new_dir[1] * -1) != self.direction:
            self.next_direction = new_dir

    def place_apple(self):
        free_cells = [
            (r, c)
            for r in range(self.rows)
            for c in range(self.cols)
            if (r, c) not in self.snake
        ]
        return random.choice(free_cells) if free_cells else None

    def move_snake(self):
        self.direction = self.next_direction
        head = self.snake[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])

        if (new_head in self.snake or
            new_head[0] < 0 or new_head[0] >= self.rows or
            new_head[1] < 0 or new_head[1] >= self.cols):
            self.dead = True
            return False

        self.snake.insert(0, new_head)

        if new_head == self.apple:
            self.apple = self.place_apple()
            return True
        else:
            self.snake.pop()
            return False

    def get_score(self):
        return len(self.snake) - 3
