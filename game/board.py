import numpy as np


class Board:
    """
    Initialize the game board.
    :param size: Size of the board (default 10x10)
    """
    def __init__(self, size=10):
        self.size = size
        self.grid = np.zeros((size, size), dtype=int)

    def reset(self):
        """
        Reset Board to its initial state.
        """
        self.grid = np.zeros((self.size, self.size), dtype=int)

    def is_valid_position(self, position):
        """
        Check if a position within the bounds of the board.
        :param position: Tuple(x, y) representing the position.
        :return:True if he position is valid False otherwise"""
        x, y = position
        return 0 <= x < self.size and 0 <= y < self.size

    def place_snake(self, snake):
        """
        Place the snake body on the board.
        :param snake: The snake object.
        """
        for segment in snake.body:
            self.grid[segment] = 1

    def place_apple(self, apple):
        """
        Place an apple on the board.
        :param apple: The apple object.
        """
        self.grid[apple.position] = 2 if apple.color == 'green' else 3

    def remove_apple(self, apple):
        """
        Remove an apple from the board.
        :param apple: The apple object
        """
        self.grid[apple.position] = 0

    def is_collision(self, position):
        """
        Check if a position is a collision (Wall or snake body).
        :param position: Tuple(x, y) representing the position.
        :return: True if the position is a collision, False otherwise.
        """
        return not self.is_valid_position(position) or self.grid[position] == 1
