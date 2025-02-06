from game.game import Game
from agent.snake_agent import Agent

FPS = 8

if __name__ == '__main__':
    game = Game()
    agent = Agent()
    while game.running:
        print(game.board.grid)
        game.handle_input(agent.movement(game.snake))
        agent.reward = game.update()
        print(agent.reward)
        game.draw()
        game.clock.tick(FPS)
    print(agent.get_state(game.snake, game.board))
