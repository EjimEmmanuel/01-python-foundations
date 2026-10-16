import pytest
from challenge_tests.helpers import state
from stone_lines.computer import score_action


def test_centre_scores_six_on_empty_board():
    g = state(['.']*9, turn='X')
    assert score_action(g, ('place',4)) == 6


def test_corner_scores_three_on_empty_board():
    g = state(['.']*9, turn='X')
    assert score_action(g, ('place',0)) == 3


def test_direct_win_always_scores_one_hundred():
    g = state(['X','X','.','O','O','.','.','.','.'], turn='X')
    assert score_action(g, ('place',2)) == 100


def test_illegal_action_raises_and_does_not_mutate():
    g = state(['X','.','.','.','.','.','.','.','.'], turn='O')
    before = g.board.copy()
    with pytest.raises(ValueError):
        score_action(g, ('place',0))
    assert g.board == before
