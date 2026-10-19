from challenge_tests.helpers import state
from stone_lines.computer import choose_rule_based_action


def test_immediate_win_outranks_block():
    g = state(['X','X','.','O','O','.','.','.','.'], turn='X')
    assert choose_rule_based_action(g) == ('place',2)


def test_block_precedes_heuristic():
    g = state(['X','X','.','O','X','.','.','.','O'], turn='O')
    assert choose_rule_based_action(g) == ('place',2)


def test_first_highest_scoring_action_selected():
    g = state(['.']*9, turn='X')
    assert choose_rule_based_action(g) == ('place',4)


def test_finished_game_has_no_action():
    g = state(['X','X','X','.','.','.','.','.','.'])
    g.finished = True
    assert choose_rule_based_action(g) is None
