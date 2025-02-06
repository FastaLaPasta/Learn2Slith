import random


class Agent:
    def __init__(self, episodes=1000):
        """
        Initialize the Agent class.
        :param episodes: number of episodes of training.
        """
        self.alpha = 0.9
        self.gamma = 0.95
        self.epsilon = 1
        self.epsilon_mini = 0.001
        self.epsilon_decay = 0.975
        self.episodes = episodes
        self.reward = 0

    def choose_action(self):
        """
        Choose the following moove.
        """

    def movement(self, snake):
        """
        Choose a random movement that cannot kill itself.
        :param snake: The snake object.
        :return: The random direction choosen."""
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        move = snake.get_direction()
        for dir in range(len(dirs)):
            if move == dirs[dir]:
                return dir

    def get_state(self, snake, board):
        """
        Get the state of the object pass in parameter.
        :param snake: The snake object.
        :param board: The game board.
        :return: return the state of the object pass as a parameter.
        """
        head = snake.body[0]
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
            if (not board.is_valid_position((next_x, next_y))) or\
                    ((next_x, next_y) in snake.body):
                immediate_danger = True
            else:
                immediate_danger = False

            green_apple = False
            red_apple = False

            temp_x, temp_y = x, y
            while True:
                temp_x += dx
                temp_y += dy
                if not board.is_valid_position((temp_x, temp_y)):
                    break
                cell_value = board.grid[temp_x, temp_y]
                if cell_value == 2:
                    green_apple = True
                    break
                elif cell_value == 3:
                    red_apple = True
                    break

            state.extend([immediate_danger, green_apple, red_apple])
        return tuple(state)
