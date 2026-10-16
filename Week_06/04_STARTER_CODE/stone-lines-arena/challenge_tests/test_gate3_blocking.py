from challenge_tests.helpers import state
from stone_lines.computer import find_blocking_action


def test_prevent_opponents_top_row():
    g = state(['X','X','.','O','X','.','.','.','O'], turn='O')
    before = (g.board.copy(),g.current_player,g.stones_placed)
    assert find_blocking_action(g) == ('place',2)
    assert (g.board,g.current_player,g.stones_placed) == before


def test_no_existing_threat_returns_none():
    g = state(['.']*9, turn='X')
    assert find_blocking_action(g) is None


def test_finished_match_returns_none():
    g = state(['X','X','X','O','.','.','.','.','.'])
    g.finished = True
    assert find_blocking_action(g) is None
