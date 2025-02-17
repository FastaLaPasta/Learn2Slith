import random


class Snake:
    def __init__(self, board_size):
        """
        Initialize the snake.
        :param initial_position: Tuple (x, y) representing the starting \
        position of the snake's head.
        """
        self.body = self.create_snake(board_size)
        self.direction = self.get_direction()
        self.grow = False

    def get_direction(self):
        """
        Determine a valid initial movement direction.
        :return: Tuple (dx, dy) representing the direction.
        """
        head = self.body[0]
        possible_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for segment in self.body[1:]:
            dx = segment[0] - head[0]
            dy = segment[1] - head[1]
            if (dx, dy) in possible_dirs:
                possible_dirs.remove((dx, dy))

        return random.choice(possible_dirs) if possible_dirs else (0, 1)

    def create_snake(self, board_size):
        """
        Create a snake with an L-shaped initial position.
        :param board_size: Size of the board.
        :return: A list representing the snake's body.
        """
        head_x = random.randint(2, board_size - 2)
        head_y = random.randint(2, board_size - 2)
        body = [(head_x, head_y)]

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        dx1, dy1 = random.choice(directions)
        second_x, second_y = head_x + dx1, head_y + dy1
        body.append((second_x, second_y))

        possible_bend_directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1)
        ]
        possible_bend_directions.remove((-dx1, -dy1))

        while True:
            dx2, dy2 = random.choice(possible_bend_directions)
            third_x, third_y = second_x + dx2, second_y + dy2
            if 0 <= third_x < board_size and 0 <= third_y < board_size:
                body.append((third_x, third_y))
                break

        return body

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
            return 10
        elif apple.color == 'red':
            self.body.pop()
            return -5

    def respawn(self, board_size):
        self.body = []
        self.body = self.create_snake(board_size)

    def eat_itself(self):
        """
        Check if the sneak eat his own body.
        :return True if eating itself, False otherwise.
        """
        head = self.body[0]
        for segment in range(len(self.body)):
            if head == self.body[segment] and segment != 0:
                return True
        return False

    def get_vision(self, board):
        """
        Generate the snake's cross-shaped vision matrix.
        :param board: The game board.
        :return: A list of lists representing the vision matrix.
        """
        dirs = ["UP", "DOWN", "LEFT", "RIGHT"]
        mtx_size = board.size + 2
        vision_matrix = [[" " for _ in range(mtx_size)]
                         for _ in range(mtx_size)]

        head_x, head_y = int(self.body[0][0]) + 1, int(self.body[0][1]) + 1
        vision_matrix[head_y][head_x] = 'H'

        vision_matrix[0][head_x] = 'W'
        vision_matrix[-1][head_x] = 'W'
        vision_matrix[head_y][0] = 'W'
        vision_matrix[head_y][-1] = 'W'

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dx, dy in directions:
            x, y = head_x, head_y
            while True:
                x += dx
                y += dy

                if not (0 <= x < mtx_size and 0 <= y < mtx_size):
                    break
                board_x, board_y = x - 1, y - 1

                vision_matrix[y][x] = '0'
                if not board.is_valid_position((board_x, board_y)):
                    vision_matrix[y][x] = 'W'
                    break
                elif (board_x, board_y) in self.body:
                    vision_matrix[y][x] = 'S'
                elif board.grid[board_x, board_y] == 2:
                    vision_matrix[y][x] = 'G'
                elif board.grid[board_x, board_y] == 3:
                    vision_matrix[y][x] = 'R'
        for row in vision_matrix:
            print("".join(row))
        for dir in range(len(directions)):
            if directions[dir] == self.direction:
                print(dirs[dir])
