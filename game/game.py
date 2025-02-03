import pygame
from board import Board
from snake import Snake
from apple import Apple

WINDOW_SIZE = 500
GRID_SIZE = 10
CELL_SIZE = WINDOW_SIZE // GRID_SIZE
FPS = 5

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
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
        pygame.display.set_caption("Snake Game")

        self.clock = pygame.time.Clock()
        self.running = True

        self.board = Board()
        self.snake = Snake((5, 5))
        self.apples = [Apple('green'), Apple('green'), Apple('red')]

        for apple in self.apples:
            apple.place_randomly(self.board)

    def handle_input(self):
        """
        Handle keyboard input for snake movement.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.snake.direction != (1, 0):
                    self.snake.change_direction((-1, 0))
                elif event.key == pygame.K_DOWN and self.snake.direction != (-1, 0):
                    self.snake.change_direction((1, 0))
                elif event.key == pygame.K_LEFT and self.snake.direction != (0, 1):
                    self.snake.change_direction((0, -1))
                elif event.key == pygame.K_RIGHT and self.snake.direction != (0, -1):
                    self.snake.change_direction((0, 1))

    def update(self):
        """
        Update game logic.
        """
        self.snake.move()

        if self.snake.check_collision(self.board):
            print("Game Over! Snake collided.")
            self.running = False
            return

        for apple in self.apples:
            if self.snake.body[0] == apple.position:
                self.snake.eat_apple(apple)
                self.board.remove_apple(apple)
                apple.place_randomly(self.board)
                break

        if len(self.snake.body) == 0:
            print("Game Over! Snake has no length.")
            self.running = False

    def draw(self):
        """
        Draw the game objects on the screen.
        """
        self.screen.fill(WHITE)

        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):
                rect = pygame.Rect(y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(self.screen, BLACK, rect, 1)

        for segment in self.snake.body:
            rect = pygame.Rect(segment[1] * CELL_SIZE, segment[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(self.screen, BLUE, rect)

        for apple in self.apples:
            color = GREEN if apple.color == 'green' else RED
            rect = pygame.Rect(apple.position[1] * CELL_SIZE, apple.position[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(self.screen, color, rect)

        pygame.display.flip()

    def run(self):
        """
        Run the game loop.
        """
        while self.running:
            self.handle_input()
            self.update()
            self.draw()
            self.clock.tick(FPS)

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
