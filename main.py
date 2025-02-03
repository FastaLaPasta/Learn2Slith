from game.board import Board
from game.snake import Snake
from game.apple import Apple

# Test the Snake class
board = Board()
snake = Snake((5, 5))

# Test movement
print("Initial snake body:", snake.body)
snake.move()
print("After moving right:", snake.body)

# Test direction change
snake.change_direction((-1, 0))  # Up
snake.move()
print("After moving up:", snake.body)

# Test collision
print("Collision at (4, 6):", snake.check_collision(board))  # Should be False
print("Collision at (-1, 5):", snake.check_collision(board))  # Should be True (out of bounds)

# Test vision
board.place_snake(snake)

# Place some apples for testing
green_apple = Apple('green', (3, 6))
red_apple = Apple('red', (5, 4))
board.place_apple(green_apple)
board.place_apple(red_apple)

vision = snake.get_vision(board)
print("\nSnake vision:")
for line in vision:
    print(line)