from challenge_tests.helpers import state
from stone_lines.computer import choose_random_action


def test_random_returns_legal_placement_without_mutation():
    g = state(['X','.','.','.','O','.','.','.','.'], turn='X')
    before = (g.board.copy(), g.current_player, g.phase, g.turns_taken)
    for _ in range(25):
        assert choose_random_action(g) in g.get_legal_actions()
    assert (g.board,g.current_player,g.phase,g.turns_taken) == before


def test_random_returns_legal_movement():
    g = state(['X','O','X','O','X','.','.','O','.'], turn='X', phase='movement', stones=6)
    assert choose_random_action(g) in g.get_legal_actions()


def test_random_returns_none_on_finished_game():
    g = state(['X','X','X','.','O','.','.','O','.'])
    g.finished = True
    g.winner = 'X'
    assert choose_random_action(g) is None
