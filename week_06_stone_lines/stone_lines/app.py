"""Application coordinator — game rules stay in game.py; input in ui.py."""

from .computer import choose_random_action, choose_rule_based_action
from .game import Game
from .player import Player
from .storage import load_statistics, record_result, save_statistics
from .ui import QuitMatch, TerminalUI

MODES = {"1": "human", "2": "random", "3": "rules"}


def players_for_mode(mode, ui):
    name_x = ui.ask_name("X")
    if mode == "human":
        name_o = ui.ask_name("O", other_name=name_x)
    else:
        name_o = "Computer Random" if mode == "random" else "Computer Rules"
        if name_x.casefold() == name_o.casefold():
            ui.error("Choose a different human name from the computer player.")
            name_x = ui.ask_name("X", other_name=name_o)
    return Player(name_x, "X"), Player(name_o, "O")


def select_action(game, mode, ui):
    """Only select actions. The Game class validates and executes them."""
    if game.current_player == "X" or mode == "human":
        return ui.ask_human_action(game)
    if mode == "random":
        return choose_random_action(game)   # deliberately unfinished Week 6 task
    if mode == "rules":
        return choose_rule_based_action(game)  # deliberately unfinished Week 6 task
    raise ValueError("Unknown game mode")


def play_match(mode, ui, statistics, player_x, player_o):
    """Run exactly one match. Return 'finished', 'quit', or 'not_ready'."""
    game = Game(player_x, player_o)
    ui.info(f"Starting {player_x.name} (X) vs {player_o.name} (O).")
    while not game.finished:
        ui.board(game, statistics)
        try:
            action = select_action(game, mode, ui)
        except QuitMatch:
            ui.info("Match cancelled. No result recorded.")
            return "quit"
        except NotImplementedError:
            ui.info("Computer strategy not implemented yet. Complete the Week 6 task to unlock this mode.")
            return "not_ready"
        if action is None:
            ui.error("No action was returned. Check the computer strategy contract.")
            return "not_ready"
        try:
            game.apply_action(action)
        except ValueError as exc:
            ui.error(f"Invalid action from player/strategy: {exc}")
            if mode != "human" and game.current_player == "O":
                return "not_ready"
    ui.board(game, statistics)
    ui.finished(game)
    record_result(statistics, player_x.name, player_o.name, game.result)
    save_statistics(statistics)
    ui.info("Match statistics saved.")
    return "finished"


def run(ui=None):
    ui = ui or TerminalUI()
    ui.welcome()
    try:
        statistics = load_statistics()
    except ValueError as exc:
        ui.error(str(exc))
        ui.info("Please repair or back up the statistics file before starting a match.")
        return
    while True:
        selection = ui.menu()
        if selection in MODES:
            mode = MODES[selection]
            player_x, player_o = players_for_mode(mode, ui)
            while True:
                status = play_match(mode, ui, statistics, player_x, player_o)
                if status != "finished" or not ui.ask_replay():
                    break
        elif selection.lower() in ("4", "help", "rules"):
            ui.rules()
        elif selection.lower() in ("5", "q", "quit", "exit"):
            ui.info("Thanks for playing Stone Lines!")
            return
        else:
            ui.error("Choose 1, 2, 3, 4, or 5.")
