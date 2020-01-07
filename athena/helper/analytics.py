# here are the main analytics functions
import random


def score_ideas(ideas):
    """
    This is a function that assigns scores to the ideas.
    Inputs:
        ideas (list): a list of ideas to be scored.
    Output:
        ranked_ideas (list): a list of idea and score tuple ranked descending.
    """

    ranked_ideas = []

    # get score for each idea
    for idea in ideas:
        score = run_score(idea)
        ranked_ideas.append([idea, score])

    # rank
    ranked_ideas = sorted(ranked_ideas, key=get_key, reverse=True)

    return ranked_ideas


def run_score(idea):
    """
    This function runs analysis and assigns a score to an idea.
    Inputs:
        idea (str): an idea to be score
    Output:
        score (int): a score between 0 and 100.
    """
    # TODO: develop the scoring function
    score = random.randint(0, 100)

    return score


def get_key(item):
    return item[1]
