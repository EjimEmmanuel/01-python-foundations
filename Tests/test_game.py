import pytest
import constant as c
import main 
from game import Game
import game
""" Test cases for game class"""
def test_new_game_has_expected_initial_state():
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    gametest = Game(
        board,
        "X",
        "placement",
        None
    )
    assert gametest.board == board
    assert gametest.current_player == "X"
    assert gametest.current_phase == "placement"
    assert gametest.winner_state is None
    8
def test_valid_placement_updates_board(monkeypatch):
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    gametest = Game(
        board,
        "X",
        "placement",
        None
    )
    monkeypatch.setattr("builtins.input", lambda: "5")

    monkeypatch.setattr(main, "gameClass", gametest)
    main.Placement_loop()
    assert gametest.board[4] == "X"




def test_invalid_placement_rejects_input(monkeypatch):
    board = ["X", "2", "3", "4", "5", "6", "7", "8", "9"]

    game = Game(
        board,
        "X",
        "placement",
        None
    )

    inputs = iter(["1", "5"])

    monkeypatch.setattr(
        "builtins.input",
        lambda: next(inputs)
    )

    placement_index = game.get_placement_position("O")

    assert placement_index == 4


def test_horizontal_win_is_detected():
    board = ["X", "X", "X", "4", "5", "6", "7", "8", "9"]

    gametest = Game(
        board,
        "X",
        "placement",
        None
    )

    assert gametest.check_winner(board, "X") is True

def test_six_non_winning_placements_enter_movement(monkeypatch):
    board = ["X", "2", "3", "X", "O", "6", "7", "O", "O"]

    gametest = Game(
        board,
        "X",
        "placement",
        None
    )

    # The board already contains 5 stones.
    monkeypatch.setattr(main, "stone_placed", 5)

    monkeypatch.setattr("game.console.input", lambda _: "2")
    monkeypatch.setattr(main, "gameClass", gametest)

    def fake_movement_loop():
        print("Movement phase ongoing...")
        gametest.current_phase = "movement"
        raise RuntimeError("Movement phase reached")

    monkeypatch.setattr(main, "Movement_loop", fake_movement_loop)

    with pytest.raises(RuntimeError, match="Movement phase reached"):
        main.main()

    assert gametest.board[1] == "X"
    assert gametest.current_phase == "movement"




def test_opponent_source_is_rejected(monkeypatch, capsys):
    board = ["X", "2", "X", "X", "O", "O", "7", "8", "O"]   
    gametest = Game(
        board,
        "X",
        "movement",
        None
    )
    inputs = iter(["5", "4", "7"])
    monkeypatch.setattr("game.console.input", lambda _: next(inputs))

    monkeypatch.setattr(main, "gameClass", gametest)
    s, d = gametest.get_movement_position("X", c.connections)
    output = capsys.readouterr().out
    
    assert "You can only move your own stone: Please select your valid stone position." in output
    assert s == 3
    
    

def test_unconnected_destination_is_rejected(monkeypatch, capsys):
    board = ["X", "2", "X", "X", "O", "6", "7", "O", "O"]   
    gametest = Game(
        board,
        "X",
        "movement",
        None    )
    inputs = iter(["9", "7", "6"])
    monkeypatch.setattr("game.console.input", lambda _: next(inputs))
    monkeypatch.setattr(main, "gameClass", gametest)
    gametest.get_movement_position("O", c.connections)
    
    output = capsys.readouterr().out

    assert "Invalid input. Please enter a valid connected destination." in output









    




def test_occupied_destination_is_rejected(monkeypatch, capsys):
    board = ["X", "2", "X", "X", "O", "6", "7", "O", "O"]   
    gametest = Game(
        board,
        "X",
        "movement",
        None
    )
    inputs = iter(["5", "4", "6"])
    monkeypatch.setattr("game.console.input", lambda _: next(inputs))
    monkeypatch.setattr(main, "gameClass", gametest)
    gametest.get_movement_position("O", c.connections)
    
    output = capsys.readouterr().out
    assert  "Invalid input. Please enter a valid empty destination." in output

def test_legal_move_clears_source_and_fills_destination(monkeypatch):
    board = ["X", "O", "X", "X", "5", "O", "7", "O", "9"]
    gametest = Game(board, "X", "movement", None)

    inputs = iter([
        "4",  # X chooses position 4 as the source
        "5"   # X chooses position 5 as the destination
    ])

    monkeypatch.setattr("game.console.input", lambda _: next(inputs))

    # Make the global gameClass in main.py use our test game
    monkeypatch.setattr(main, "gameClass", gametest)

    main.Movement_loop()

    assert gametest.board[3] == "4"
    assert gametest.board[4] == "X"

def test_movement_win_is_detected(monkeypatch, capsys):
    board = ["O", "2", "X", "4", "X", "O", "7", "X", "O"]
    gametest = Game(board, "X", "movement", None)

    inputs = iter([
        "8",  
        "7"   ])

    monkeypatch.setattr("game.console.input", lambda _: next(inputs))

    monkeypatch.setattr(main, "gameClass", gametest)
    main.Movement_loop()
    output = capsys.readouterr().out
    assert f"Player {gametest.current_player} wins on board positions: " in output