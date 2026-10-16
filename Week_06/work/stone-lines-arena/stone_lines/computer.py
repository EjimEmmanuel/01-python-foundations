"""WEEK 6 STUDENT WORK — decision strategies.

This is intentionally unfinished. Game mechanics, UI, legal actions, and safe
simulation are already provided. Do not implement the tasks in the starter.

Fixed action contracts:
    ("place", position_index)
    ("move", source_index, destination_index)
Indexes are 0..8. Strategies must NEVER change `game` or print prompts.
Each function returns a legal action tuple, or None if no action exists.

Task requirements and tests are in the Week 6 student package (03_PROJECT/).
"""


def choose_random_action(game):
    """Week 6 task: select any legal action using random.choice()."""
    raise NotImplementedError("Complete the Week 6 random strategy task.")


def find_winning_action(game):
    """Week 6 task: find a legal action that wins immediately, else None."""
    raise NotImplementedError("Complete the Week 6 immediate-win task.")


def find_blocking_action(game):
    """Week 6 task: prevent an immediate opponent win when possible, else None."""
    raise NotImplementedError("Complete the Week 6 blocking task.")


def score_action(game, action):
    """Week 6 task: return a numeric heuristic score for a legal action."""
    raise NotImplementedError("Complete the Week 6 heuristic-scoring task.")


def choose_rule_based_action(game):
    """Week 6 task: combine win, block, heuristic, and random fallback."""
    raise NotImplementedError("Complete the Week 6 strategy-priority task.")
