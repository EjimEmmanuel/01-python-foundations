import pytest
import constant as c
import main 
from player import Player
from game import Game
import storage as s

FILE_PATH = "data/statistics.json"

player_X = Player("Emmanuel", "X")
player_O = Player("Chioma", "O")

def test_new_game_has_expected_initial_state():
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    gametest = Game(
        board,
        player_X.symbol,
        player_X.name,
        "placement",
        player_X,
        player_O,
        0
    )
    assert gametest.board == board
    assert gametest.current_player == "X"
    assert gametest.current_phase == "placement"

def test_valid_placement_updates_board(monkeypatch):
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    storage = s.initialize_statistics(file_path=FILE_PATH)

    gametest = Game(
    board,
    player_X.symbol,
    player_X.name,
    "placement",
    player_X,
    player_O,
    0
    )
    monkeypatch.setattr("builtins.input", lambda: "5")
    monkeypatch.setattr(main, "create_game", lambda: gametest)
    main.Placement_loop(gametest, storage)
    assert gametest.board[4] == "X"




def test_invalid_placement_rejects_input(monkeypatch):
    board = ["X", "2", "3", "4", "5", "6", "7", "8", "9"]

    gametest = Game(
    board,
    player_X.symbol,
    player_X.name,
    "placement",
    player_X,
    player_O,
    0
    )
 
    inputs = iter(["1", "5"])

    monkeypatch.setattr(
        "builtins.input",
        lambda: next(inputs)
    )

    placement_index = gametest.get_placement_position("O", player_X.name)

    assert placement_index == 4


def test_horizontal_win_is_detected():
    board = ["X", "X", "X", "4", "5", "6", "7", "8", "9"]

    gametest = Game(
    board,
    player_X.symbol,
    player_X.name,
    "placement",
    player_X,
    player_O,
    0
    )

    assert gametest.check_winner(board, "X") is True

def test_six_non_winning_placements_enter_movement(monkeypatch):
    board = ["X", "2", "3", "X", "O", "6", "7", "O", "O"]

    gametest = Game(
        board,
        player_X.symbol,
        player_X.name,
        "placement",
        player_X,
        player_O,
        5
    )

    # Select "Start Game" from the main menu.
    monkeypatch.setattr("builtins.input", lambda *args: "1")

    # Select position 2 during placement.
    monkeypatch.setattr("game.console.input", lambda *args: "2")

    # Make create_game() return our prepared game object.
    monkeypatch.setattr(main, "create_game", lambda: gametest)

    def fake_movement_loop(*args, **kwargs):
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
    player_X.symbol,
    player_X.name,
    "placement",
    player_X,
    player_O,
    0
    )
    inputs = iter(["5", "4", "7"])
    monkeypatch.setattr("game.console.input", lambda _: next(inputs))

    monkeypatch.setattr(main, "create_game", lambda: gametest)
    s, d = gametest.get_movement_position(player_X.symbol, player_X.name,  c.connections)
    output = capsys.readouterr().out
    
    assert "You can only move your own stone: Please select your valid stone position." in output
    assert s == 3
    
    

def test_unconnected_destination_is_rejected(monkeypatch, capsys):
    board = ["X", "2", "X", "X", "O", "6", "7", "O", "O"]   
    gametest = Game(
    board,
    player_X.symbol,
    player_X.name,
    "placement",
    player_X,
    player_O,
    0
    )
    inputs = iter(["9", "7", "6"])
    monkeypatch.setattr("game.console.input", lambda _: next(inputs))
    monkeypatch.setattr(main, "create_game", lambda: gametest)
    gametest.get_movement_position(player_O.symbol, player_O.name,  c.connections)
    
    output = capsys.readouterr().out

    assert "Invalid input. Please enter a valid connected destination." in output






def test_statistics_use_temporary_path(tmp_path):
    # Create a temporary statistics file
    test_file = tmp_path / "statistics.json"

    # Sample player records
    statistics = {
        "Emmanuel": {
            "games": 1,
            "wins": 1,
            "losses": 0
        },
        "Boss": {
            "games": 1,
            "wins": 0,
            "losses": 1
        }
    }

    # Save the records to the temporary file
    s.dump_statistics(statistics, test_file)

    # Load the records from the temporary file
    loaded_statistics = s.initialize_statistics(test_file)

    # Verify that the records were saved and loaded correctly
    assert loaded_statistics == statistics





    




def test_occupied_destination_is_rejected(monkeypatch, capsys):
    board = ["X", "2", "X", "X", "O", "6", "7", "O", "O"]   
    gametest = Game(
    board,
    player_X.symbol,
    player_X.name,
    "placement",
    player_X,
    player_O,
    0
    )
    inputs = iter(["5", "4", "6"])
    monkeypatch.setattr("game.console.input", lambda _: next(inputs))
    monkeypatch.setattr(main, "create_game", lambda: gametest)
    gametest.get_movement_position(player_O.symbol, player_O.name,  c.connections)
    
    output = capsys.readouterr().out
    assert  "Invalid input. Please enter a valid empty destination." in output

def test_legal_move_clears_source_and_fills_destination(monkeypatch):
    board = ["X", "O", "X", "X", "5", "O", "7", "O", "9"]
    storage = s.initialize_statistics(file_path=FILE_PATH)

    gametest = Game(
    board,
    player_X.symbol,
    player_X.name,
    "placement",
    player_X,
    player_O,
    0
    )
    inputs = iter([
        "4",  # X chooses position 4 as the source
        "5"   # X chooses position 5 as the destination
    ])

    monkeypatch.setattr("game.console.input", lambda _: next(inputs))

    # Make the global gameClass in main.py use our test game
    monkeypatch.setattr(main, "create_game", lambda: gametest)
    main.Movement_loop(gametest, storage)

    assert gametest.board[3] == "4"
    assert gametest.board[4] == "X"

def test_movement_win_is_detected(monkeypatch, capsys):
    board = ["O", "2", "X", "4", "X", "O", "7", "X", "O"]
    storage = s.initialize_statistics(file_path=FILE_PATH)

    gametest = Game(
    board,
    player_X.symbol,
    player_X.name,
    "placement",
    player_X,
    player_O,
    0
    )
    inputs = iter([
        "8",  
        "7"   ])

    monkeypatch.setattr("game.console.input", lambda _: next(inputs))

    monkeypatch.setattr(main, "create_game", lambda: gametest)
    main.Movement_loop(gametest, storage)
    output = capsys.readouterr().out
    assert f"Player {gametest.current_player} wins on board positions: " in output