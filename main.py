from game.game import Game
from agent.snake_agent import Agent
from utils.helpers import plot, open_file
import argparse as ap


FPS = 10


def print_plot(game, total_size):
    size.append(len(game.snake.body))
    total_size += len(game.snake.body)
    mean_size.append(total_size / episode)
    plot(size, mean_size)
    return total_size


if __name__ == '__main__':
    parser = ap.ArgumentParser()
    parser.add_argument("-s", "--size", help="size", type=int, default=10)
    parser.add_argument("-n", "--training_session", help="Training_session(s)",
                        type=int, default=1000)
    parser.add_argument("-e", "--epsilon", help="No learning",
                        action='store_false')
    parser.add_argument("-L", "--learning", help='Update agent',
                        action='store_false')
    parser.add_argument("-D", "--display", help="Display off",
                        action="store_false")
    parser.add_argument("-load_f", "--path",
                        help="Load a file with training informations",
                        type=str, default=None)
    parser.add_argument("-v", "--vision", help="Print snake vision",
                        action="store_true")
    args = parser.parse_args()

    try:
        if (args.path):
            file = open_file(args.path)
            agent = Agent(args.training_session, args.epsilon, args.learning, file)
        else:
            agent = Agent(args.training_session, args.epsilon, args.learning)
    except Exception as e:
        print(e)
    total_size = 0
    size = []
    mean_size = []
    game = Game(args.size, args.display)
    for episode in range(1, agent.episodes + 1):
        game.restart()
        if args.vision:
            print(game.snake.get_vision(game.board))
        while game.running:
            agent.state = game.get_state()
            game.handle_input(agent.choose_action(game))
            agent.reward = game.update()
            if game.snake.body:
                agent.new_state = game.get_state()
            agent.update_q_table()
            if args.display:
                game.draw()
                game.clock.tick(FPS)
        agent.update_epsilon()
        total_size = print_plot(game, total_size)
    agent.save_q_table()


# TODO Step-bt-step Mode 🚧
# TODO main() function need to be create and called🚧
# TODO Bonus: modifiable board Size ✅ Implement draw function 🚧
# TODO Accurcy of the bot 🚧
# TODO Neural network Agent 🚧
# TODO Norme FLAKE8 🚧

# TODO state segfault quand meurt de pomme rouge / Maybe Done with if in main ✅
# TODO Vision matrix // DONE ✅
# TODO Flags ✅
# TODO Use the q-table from a file/ Non random move then ✅
# TODO Flags Number of training session ✅/ don't learn ✅/ Visual display ✅
# load file ✅/ epsilon 0 ✅
# TODO one Game object for the loop ✅
