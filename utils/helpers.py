import matplotlib.pyplot as plt
from IPython import display

plt.ion()


def plot(scores, mean_scores):
    """
    Plot in real time the performances of the Agent.
    :param scores: An array containing the score of each episode.
    :param mean_scores: An array containing the mean scores."""
    display.clear_output(wait=True)
    display.display(plt.gcf())
    plt.clf()
    plt.title('Training...')
    plt.xlabel('Number of Games')
    plt.ylabel('Score')
    plt.plot(scores, label="Score")
    plt.plot(mean_scores, label="Mean Score", linestyle="dashed")
    plt.ylim(ymin=0)

    plt.text(len(scores)-1, scores[-1], str(scores[-1]))
    plt.text(len(mean_scores)-1, mean_scores[-1], str(mean_scores[-1]))

    plt.legend()
    plt.pause(0.01)
