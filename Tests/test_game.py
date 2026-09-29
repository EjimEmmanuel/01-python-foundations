import main 
from game import Game
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
    


def test_valid_placement_updates_board(monkeypatch):
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    gametest = Game(
        board,
        "X",
        "placement",
        None
    )
    monkeypatch.setattr("builtins.input", lambda _: "5")

    placement_index = gametest.placement("X")
    gametest.board[placement_index] = gametest.current_player


    assert gametest.board[4] == "X"

def test_invalid_placement_rejects_input(monkeypatch):
    board = ["X", "2", "3", "4", "5", "6", "7", "8", "9"]

    gametest = Game(
        board,
        "X",
        "placement",
        None
    )


    inputs = iter(["1", "5"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    position = gametest.placement("O")

    assert position == 4
    assert gametest.board[0] == "X"

def test_horizontal_win_is_detected():
    board = ["X", "X", "X", "4", "5", "6", "7", "8", "9"]

    gametest = Game(
        board,
        "X",
        "placement",
        None
    )

    assert gametest.check_winner(board, "X") is True




"""
def test_six_non_winning_placements_enter_movement(monkeypatch):
    board = ["X", "2", "3", "X", "O", "6", "7", "O", "O"]

    gametest = Game(
        board,
        "X",
        "placement",
        None
    )
    monkeypatch.setattr("builtins.input", lambda _: "3")
    print("Before:", gametest.board)

    assert gametest.current_phase == "movement"""""
"""    
def test_opponent_source_is_rejected(monkeypatch):
    board = ["X", "2", "3", "X", "O", "6", "7", "O", "O"]   
    gametest = Game(
        board,
        "X",
        "movement",
        None
    )
    monkeypatch.setattr("builtins.input", lambda _: "3")
    if gametest.current_phase == "movement":
        get_source, get_destination = gametest.get_movement_position("O", gametest.connections)
        print("current player:", gametest.current_player)
        print(gametest.board)
        if gametest.board[get_source[0]] != "O":
            assert True"""

def test_unconnected_destination_is_rejected(monkeypatch, capsys):
    board = ["X", "2", "X", "X", "O", "6", "7", "O", "O"]   
    gametest = Game(
        board,
        "X",
        "movement",
        None
    )
    inputs = iter(["9", "7", "4", "1", "3", "6"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs) )
    gametest.get_movement_position("O", gametest.connections)
    
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
    monkeypatch.setattr("builtins.input", lambda _: next(inputs) )
    gametest.get_movement_position("O", gametest.connections)
    
    output = capsys.readouterr().out
    assert  "Invalid input. Please enter a valid empty destination." in output

def test_legal_move_clears_source_and_fills_destination(monkeypatch):
    board = ["X", "O", "X", "X", "5", "O", "7", "O", "9"]
    gametest = Game(board, "X", "movement", None)

    inputs = iter([
        "4",  # X chooses position 4 as the source
        "5"   # X chooses position 5 as the destination
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # Make the global gameClass in main.py use our test game
    monkeypatch.setattr(main, "gameClass", gametest)

    main.Movement_loop()

    assert gametest.board[3] == "4"
    assert gametest.board[4] == "X"

def test_movement_win_is_detected(monkeypatch):
    board = ["O", "2", "X", "4", "X", "O", "7", "X", "O"]
    gametest = Game(board, "X", "movement", None)

    inputs = iter([
        "3",  # X chooses position 4 as the source
        "2"   # X chooses position 5 as the destination
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    monkeypatch.setattr(main, "gameClass", gametest)
    main.Movement_loop()

    assert gametest.check_winner(gametest.board, "X") == True
