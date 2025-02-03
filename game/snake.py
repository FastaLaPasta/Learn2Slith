class Snake:
    def __init__(self, initial_position):
        """
        Initialize the snake.
        :param initial_position: Tuple (x, y) representing the starting \
        position of the snake's head.
        """
        self.body = [initial_position]
        self.direction = (0, 1)
        self.grow = False

    def move(self):
        """
        Move the snake in the current direction.
        """
        head = self.body[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])
        self.body.insert(0, new_head)
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

    def change_direction(self, new_direction):
        """
        Change the snake's direction.
        param: new_direction: Tuple(dx, dy) representing the new direction.
        """
        self.direction = new_direction

    def check_collision(self, board):
        """
        Check if the sneak collide with the board boundaries or itself.
        :param board: The game board.
        :return: True if collision occurs, False otherwise
        """
        head = self.body[0]
        return board.is_collision(head)

    def eat_apple(self, apple):
        """
        Handle the snake eating an apple.
        :param apple: The apple object.
        """
        if apple.color == 'green':
            self.grow = True
        elif apple.color == 'red':
            if len(self.body) > 1:
                self.body.pop()

    def get_vision(self, board):
        """
        Generate the snake's cross-shaped vision matrix.
        :param board: The game board.
        :return: A list of lists representing the vision matrix.
        """
        head = self.body[0]
        vision = []

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dx, dy in directions:
            vision_line = []
            x, y = head
            while True:
                x += dx
                y += dy
                if not board.is_valid_position((x, y)):
                    vision_line.append('W')
                    break
                elif (x, y) in self.body:
                    vision_line.append('S')
                elif board.grid[x, y] == 2:
                    vision_line.append('G')
                elif board.grid[x, y] == 3:
                    vision_line.append('R')
                else:
                    vision_line.append('0')
            vision.append(vision_line)
        return vision
