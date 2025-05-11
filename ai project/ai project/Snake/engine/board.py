import pygame
import random

class GameBoard:
    def __init__(self, render_mode=True):
        self.rows = 20
        self.cols = 20
        self.cell_size = 30
        self.render_mode = render_mode
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
            (r, c) for r in range(self.rows)
                   for c in range(self.cols)
                   if (r, c) not in self.snake
        ]
        return random.choice(free_cells) if free_cells else None

    def move_snake(self):
        self.direction = self.next_direction
        head = self.snake[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])

        if (
            new_head in self.snake
            or new_head[0] < 0 or new_head[0] >= self.rows
            or new_head[1] < 0 or new_head[1] >= self.cols
        ):
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

    """def draw(self, screen):
        if not self.render_mode:
            return  # 🚫 Skip everything below if in training mode"""
    ...

    def draw(self, screen):
        from engine.tilemap import TileMap
        tilemap = TileMap(self.cell_size)
        tilemap.draw_background(screen, self.rows, self.cols)

        apple_img = pygame.image.load("assets/images/apple.png")
        apple_img = pygame.transform.scale(apple_img, (int(self.cell_size * 0.85), int(self.cell_size * 0.85)))
        offset = int((self.cell_size - self.cell_size * 0.85) / 2)
        if self.apple:
            screen.blit(apple_img, (self.apple[1] * self.cell_size + offset, self.apple[0] * self.cell_size + offset))

        for i, (row, col) in enumerate(self.snake):
            x, y = col * self.cell_size, row * self.cell_size

            if i == 0:
                dx, dy = self.direction
                head_map = {(-1, 0): "up", (1, 0): "down", (0, -1): "left", (0, 1): "right"}
                head_img = pygame.image.load(f"assets/images/head_{head_map[(dx, dy)]}.png")
                head_img = pygame.transform.scale(head_img, (int(self.cell_size * 0.85), int(self.cell_size * 0.85)))
                screen.blit(head_img, (x + offset, y + offset))

            elif i == len(self.snake) - 1:
                tx, ty = self.snake[i - 1][0] - row, self.snake[i - 1][1] - col
                tail_map = {(-1, 0): "down", (1, 0): "up", (0, -1): "right", (0, 1): "left"}
                tail_img = pygame.image.load(f"assets/images/tail_{tail_map[(tx, ty)]}.png")
                tail_img = pygame.transform.scale(tail_img, (int(self.cell_size * 0.85), int(self.cell_size * 0.85)))
                screen.blit(tail_img, (x + offset, y + offset))

            else:
                prev = self.snake[i - 1]
                next_ = self.snake[i + 1]
                prev_offset = (row - prev[0], col - prev[1])
                next_offset = (row - next_[0], col - next_[1])

                turn_key = (prev_offset, next_offset)

                turn_patterns = {
                    ((-1, 0), (0, -1)): "body_topleft",
                    ((0, -1), (-1, 0)): "body_topleft",
                    ((-1, 0), (0, 1)): "body_topright",
                    ((0, 1), (-1, 0)): "body_topright",
                    ((1, 0), (0, -1)): "body_bottomleft",
                    ((0, -1), (1, 0)): "body_bottomleft",
                    ((1, 0), (0, 1)): "body_bottomright",
                    ((0, 1), (1, 0)): "body_bottomright",
                }

                if prev[0] == next_[0]:
                    body_img = pygame.image.load("assets/images/body_horizontal.png")
                elif prev[1] == next_[1]:
                    body_img = pygame.image.load("assets/images/body_vertical.png")
                else:
                    filename = turn_patterns.get(turn_key, "body_vertical")
                    body_img = pygame.image.load(f"assets/images/{filename}.png")

                body_img = pygame.transform.scale(body_img, (int(self.cell_size * 0.85), int(self.cell_size * 0.85)))
                screen.blit(body_img, (x + offset, y + offset))