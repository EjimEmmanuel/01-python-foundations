"""Prepared-game tests; intentionally no solutions to Week 6 strategy tasks."""

import pytest

from stone_lines.constants import CONNECTIONS, WINNING_LINES
from stone_lines.game import Game
from stone_lines.player import Player


def place(game, *positions):
    for position in positions:
        game.apply_action(("place", position - 1))
    return game


def movement_game():
    # Legal six-placement board, no winner: X on 1, 3, 4; O on 2, 8, 9.
    game = Game(Player("Emma", "X"), Player("Chioma", "O"))
    place(game, 1, 2, 3, 8, 4, 9)
    assert game.phase == "movement"
    return game


def test_new_game_has_expected_start(game):
    assert game.board == [str(n) for n in range(1, 10)]
    assert game.current_player == "X"
    assert game.phase == "placement"
    assert game.stones_placed == 0
    assert game.result is None
    assert game.finished is False


def test_player_validation():
    with pytest.raises(ValueError):
        Player("A", "X")
    with pytest.raises(ValueError):
        Player("Emma", "Z")
    with pytest.raises(ValueError):
        Game(Player("Emma", "X"), Player("emma", "O"))


def test_placement_lists_all_nine_actions(game):
    assert game.get_legal_actions() == [("place", n) for n in range(9)]


def test_placement_updates_state(game):
    game.apply_action(("place", 4))
    assert game.board[4] == "X"
    assert game.stones_placed == 1
    assert game.current_player == "O"
    assert game.turns_taken == 1


def test_illegal_placement_does_not_change_state(game):
    game.apply_action(("place", 0))
    prior = game.copy()
    with pytest.raises(ValueError):
        game.apply_action(("place", 0))
    assert game.board == prior.board
    assert game.current_player == prior.current_player
    assert game.stones_placed == prior.stones_placed


@pytest.mark.parametrize("action", [None, ["place", 0], ("place", -1),
                                    ("place", 9), ("move", 0, 1), ("place", True)])
def test_malformed_or_illegal_action_rejected_without_mutation(game, action):
    prior = game.copy()
    with pytest.raises(ValueError):
        game.apply_action(action)
    assert game.board == prior.board
    assert game.current_player == prior.current_player
    assert game.turns_taken == prior.turns_taken


@pytest.mark.parametrize("line", WINNING_LINES)
def test_all_eight_winning_lines_are_recognized(game, line):
    for i in line:
        game.board[i] = "X"
    assert game.check_winner("X")
    assert not game.check_winner("O")


def test_no_false_winner_for_empty_row(game):
    assert not game.check_winner("X")
    assert not game.check_winner("O")


def test_game_ends_when_fifth_placement_wins(game):
    place(game, 1, 4, 2, 5, 3)
    assert game.winner == "X"
    assert game.finished is True
    assert game.result == "X"
    assert game.stones_placed == 5
    assert game.get_legal_actions() == []
    with pytest.raises(ValueError):
        game.apply_action(("place", 5))


def test_six_nonwinning_placements_enter_movement():
    game = movement_game()
    assert game.stones_placed == 6
    assert game.current_player == "X"
    assert game.finished is False
    assert all(action[0] == "move" for action in game.get_legal_actions())


def test_movement_uses_real_board_connections():
    game = movement_game()
    expected = [("move", source, target)
                for source, value in enumerate(game.board)
                if value == "X"
                for target in CONNECTIONS[source]
                if game.board[target] not in ("X", "O")]
    assert game.get_legal_actions() == expected


def test_opponent_stone_cannot_be_moved():
    game = movement_game()
    with pytest.raises(ValueError):
        game.apply_action(("move", 1, 4))  # source 2 holds O


def test_unconnected_movement_rejected():
    game = movement_game()
    with pytest.raises(ValueError):
        game.apply_action(("move", 0, 7))


def test_destination_occupied_rejected():
    game = movement_game()
    with pytest.raises(ValueError):
        game.apply_action(("move", 0, 1))


def test_legal_movement_clears_source_and_switches_player():
    game = movement_game()
    game.apply_action(("move", 3, 4))  # X: 4 -> 5
    assert game.board[3] == "4"
    assert game.board[4] == "X"
    assert game.current_player == "O"


def test_movement_win_detected(game):
    # Directly prepare a valid movement-phase state for targeted test.
    game.board = ["X", "X", "3", "4", "O", "6", "O", "X", "O"]
    game.phase = "movement"
    game.stones_placed = 6
    game.current_player = "X"
    assert ("move", 7, 2) not in game.get_legal_actions()
    # X at 8 can go to 5 only if empty; instead X at 1 can go to 3 only by two moves.
    # Here, test win after a connected move using a different board.
    game.board = ["X", "X", "3", "4", "O", "X", "O", "8", "O"]
    game.current_player = "X"
    # X at 6 -> 3 is connected, yielding X on 1,2,3.
    assert ("move", 5, 2) in game.get_legal_actions()
    game.apply_action(("move", 5, 2))
    assert game.finished
    assert game.result == "X"
    assert game.winning_positions("X") == [(0, 1, 2)]


def test_copy_is_independent(game):
    other = game.copy()
    other.apply_action(("place", 0))
    assert game.board[0] == "1"
    assert game.current_player == "X"
    assert other.board[0] == "X"
    assert other.current_player == "O"
    assert game.player_x is not other.player_x


def test_preview_does_not_mutate_game(game):
    future = game.preview_action(("place", 4))
    assert future.board[4] == "X"
    assert game.board[4] == "5"
    assert game.stones_placed == 0


def test_preview_rejects_bad_action_and_keeps_original(game):
    with pytest.raises(ValueError):
        game.preview_action(("move", 0, 4))
    assert game.board[0] == "1"


def test_turn_is_preserved_after_invalid_movement():
    game = movement_game()
    before = game.copy()
    with pytest.raises(ValueError):
        game.apply_action(("move", 0, 8))
    assert game.current_player == before.current_player
    assert game.board == before.board


def test_legal_action_query_does_not_mutate_game():
    game = movement_game()
    before = game.copy()
    _ = game.get_legal_actions()
    assert game.board == before.board
    assert game.current_player == before.current_player
    assert game.turns_taken == before.turns_taken


def test_o_can_win_on_sixth_placement(game):
    # O takes 1, 4, 7; X places at 2, 5, 9 without forming a line.
    place(game, 2, 1, 5, 4, 9, 7)
    assert game.finished
    assert game.result == "O"
    assert game.stones_placed == 6
    assert game.phase == "placement"  # game ended before movement


def test_each_board_connection_is_reciprocal():
    for source, destinations in CONNECTIONS.items():
        for destination in destinations:
            assert source in CONNECTIONS[destination]
