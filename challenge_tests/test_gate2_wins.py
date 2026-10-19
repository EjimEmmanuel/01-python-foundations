from challenge_tests.helpers import state
from stone_lines.computer import find_winning_action


def test_first_immediate_win_selected():
    g = state(['X','X','.','O','O','.','.','.','.'], turn='X')
    before = g.board.copy()
    assert find_winning_action(g) == ('place',2)
    assert g.board == before


def test_opponent_can_win_but_current_player_cannot():
    g = state(['X','X','.','O','X','.','.','.','O'], turn='O')
    assert find_winning_action(g) is None


def test_computer_has_winning_placement_at_screen_seven():
    g = state(['O','X','.','O','X','.','.','.','X'], turn='O')
    assert find_winning_action(g) == ('place',6)
