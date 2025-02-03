import random


class Apple:
    def __init__(self, color, position=None):
        """
        Initialize the apple.
        :param color: Color of the apple ('green' or 'red').
        :param position: Tuple (x, y) representing the apple's position.
        """
        self.color = color
        self.position = position

    def place_randomly(self, board):
        """
        Place the apple randomly on the board.
        :param board: The game board.
        """
        while True:
            x = random.randint(0, board.size - 1)
            y = random.randint(0, board.size - 1)
            if board.grid[x, y] == 0:
                self.position = (x, y)
                break
