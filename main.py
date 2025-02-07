from game.game import Game
from agent.snake_agent import Agent
from utils.helpers import plot


FPS = 1000

if __name__ == '__main__':
    agent = Agent()
    total_size = 0
    size = []
    mean_size = []
    for episode in range(1, agent.episodes):
        game = Game()
        while game.running:
            agent.state = game.get_state()
            game.handle_input(agent.choose_action(game))
            agent.reward = game.update()
            if game.snake.body:
                agent.new_state = game.get_state()
            # print(agent.state, agent.new_state)
            agent.update_q_table()
            # game.draw()
            # game.clock.tick(FPS)
        agent.update_epsilon()
        # size.append(len(game.snake.body))
        # total_size += len(game.snake.body)
        # mean_size.append(total_size / episode)
        # plot(size, mean_size)
    agent.save_q_table()


# TODO Step-bt-step Mode
# TODO state segfault quand meurt de pomme rouge
# TODO Vision matrix
# TODO Flags
# TODO Use the q-table from a file/ Non random move then

# TODO Bonus: modifiable board Size, Accurcy of the bot, Neural network Agent
# TODO Norme FLAKE8
