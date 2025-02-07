import pygame
from game.board import Board
from game.snake import Snake
from game.apple import Apple

WINDOW_SIZE = 500
GRID_SIZE = 10
CELL_SIZE = WINDOW_SIZE // GRID_SIZE
FPS = 8

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


class Game:
    def __init__(self):
        """
        Initialize the game components and pygame window.
        """
        # pygame.init()
        # self.screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
        # pygame.display.set_caption("Snake Game")

        self.clock = pygame.time.Clock()
        self.running = True

        self.board = Board()
        self.snake = Snake(self.board.size)
        self.apples = [Apple('green'), Apple('green'), Apple('red')]

        self.board.place_snake(self.snake)
        for apple in self.apples:
            apple.place_randomly(self.board)
            self.board.place_apple(apple)

    def handle_input(self, move):
        """
        Handle keyboard input for snake movement.
        :param moove: The movement asked to proceed.
        """
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         self.running = False
        #         pygame.quit()
        if move == 0:
            self.snake.change_direction((-1, 0))
        elif move == 1:
            self.snake.change_direction((1, 0))
        elif move == 2:
            self.snake.change_direction((0, -1))
        elif move == 3:
            self.snake.change_direction((0, 1))

    def update(self):
        """
        Update game logic.
        """
        reward = -0.1
        self.snake.move()

        if not self.snake.check_collision(self.board):
            print("Game Over! Snake collided.")
            self.running = False
            reward = -10
            return reward

        self.board.place_snake(self.snake)
        if self.snake.eat_itself():
            print("Game Over! Snake eating itself.")
            self.running = False
            reward = -10
            return reward

        for apple in self.apples:
            if self.snake.body[0] == apple.position:
                reward = self.snake.eat_apple(apple)
                self.board.remove_apple(apple)
                self.board.place_snake(self.snake)
                apple.place_randomly(self.board)
                self.board.place_apple(apple)
                break

        if len(self.snake.body) == 0:
            print("Game Over! Snake has no length.")
            self.running = False
        return reward

    def draw(self):
        """
        Draw the game objects on the screen.
        """
        self.screen.fill(WHITE)

        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):
                rect = pygame.Rect(y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(self.screen, BLACK, rect, 1)

        for index, segment in enumerate(self.snake.body):
            rect = pygame.Rect(segment[1] * CELL_SIZE, segment[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if index != 0:
                pygame.draw.rect(self.screen, BLUE, rect)
            else:
                pygame.draw.rect(self.screen, 'darkblue', rect)

        for apple in self.apples:
            color = GREEN if apple.color == 'green' else RED
            rect = pygame.Rect(apple.position[1] * CELL_SIZE, apple.position[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(self.screen, color, rect)

        pygame.display.flip()

    def get_state(self):
        """
        Get the state of the object pass in parameter.
        :param snake: The snake object.
        :param board: The game board.
        :return: return the state of the object pass as a parameter.
        """
        head = self.snake.body[0]
        state = []
        x, y = head
        directions = {
            'up': (-1, 0),
            'down': (1, 0),
            'right': (0, 1),
            'left': (0, -1)
        }

        for dir in ['up', 'down', 'left', 'right']:
            dx, dy = directions[dir]

            next_x, next_y = x + dx, y + dy
            if (not self.board.is_valid_position((next_x, next_y))) or\
                    ((next_x, next_y) in self.snake.body):
                immediate_danger = 1
            else:
                immediate_danger = 0

            green_apple = 0
            red_apple = 0

            temp_x, temp_y = x, y
            while True:
                temp_x += dx
                temp_y += dy
                if not self.board.is_valid_position((temp_x, temp_y)):
                    break
                cell_value = self.board.grid[temp_x, temp_y]
                if cell_value == 2:
                    green_apple = 1
                    break
                elif cell_value == 3:
                    red_apple = 1
                    break

            state.extend([immediate_danger, green_apple, red_apple])
        return state
