import random
import numpy as np


class Agent:
    def __init__(self, episodes=10, epsilon=True, alpha=True, file=None):
        """
        Initialize the Agent class.
        :param episodes: number of episodes of training.
        """
        # How fast do we replace old knowledge, 0 = never/ 1 = completely
        self.alpha = 0.2 if alpha is True else 0
        # How much consideration given to future rewards
        self.gamma = 0.975
        self.epsilon = 1 if epsilon is True else 0
        self.epsilon_min = 0.001
        self.epsilon_decay = 0.98
        self.episodes = episodes
        self.reward = 0

        self.state = None
        self.new_state = None
        self.action = None
        self.q_table = np.zeros((4096, 4)) if file is None else file

    def update_q_table(self):
        """
        Update the Q-table using the Q-learning update rule.
        """
        current_q = self.q_table[self.encode_state(self.state), self.action]
        max_future_q = np.max(self.q_table[self.encode_state(self.new_state)])
        new_q = (1 - self.alpha) * current_q + self.alpha *\
            (self.reward + self.gamma * max_future_q)

        self.q_table[self.encode_state(self.state), self.action] = new_q

    def choose_action(self, game):
        """
        Choose the following moove.
        :param snake: The snake object.
        :param board: The board object.
        """
        if random.random() < self.epsilon:
            self.movement(game.snake)
            return self.action
        else:
            self.action = np.argmax(
                self.q_table[self.encode_state(self.state)])
            return self.action

    def movement(self, snake):
        """
        Choose a random movement that cannot kill itself.
        :param snake: The snake object.
        :return: The random direction choosen.
        """
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        move = snake.get_direction()
        for dir in range(len(dirs)):
            if move == dirs[dir]:
                self.action = dir
                return dir

    def encode_state(self, state):
        """
        Convert a list of 12 boolean values into a unique integer index.
        :param state_list: List of 12 boolean values (0s and 1s).
        :return: Integer representation of the state.
        """
        return int("".join(map(str, state)), 2)

    def update_epsilon(self):
        self.epsilon = max(self.epsilon * self.epsilon_decay, self.epsilon_min)

    def save_q_table(self):
        """
        Save the Q table in a file.
        """
        np.save(f'models/model_{self.episodes}_session.npy', self.q_table)

    def load_q_table(self, path):
        """
        Load a file and set the q-table with the one in it.
        :param path: Path to the file containing the Q-table.
        """
        self.q_table = np.load(path)
