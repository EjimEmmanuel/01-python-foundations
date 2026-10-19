"""Application tests without prompts or writing personal statistics."""

from stone_lines import app
from stone_lines.game import Game
from stone_lines.player import Player
from stone_lines.ui import QuitMatch


class FakeUI:
    def __init__(self, actions=()):
        self.actions = iter(actions)
        self.messages = []
        self.boards = 0

    def info(self, text):
        self.messages.append(text)

    def error(self, text):
        self.messages.append(text)

    def board(self, game, stats=None):
        self.boards += 1

    def finished(self, game):
        self.messages.append(f"finished: {game.result}")

    def ask_human_action(self, game):
        return next(self.actions)


def test_select_action_human_uses_ui():
    game = Game(Player("Emma", "X"), Player("Chioma", "O"))
    ui = FakeUI([("place", 4)])
    assert app.select_action(game, "human", ui) == ("place", 4)


def test_select_action_computer_mode_starts_with_human():
    game = Game(Player("Emma", "X"), Player("Computer Rules", "O"))
    ui = FakeUI([("place", 4)])
    assert app.select_action(game, "rules", ui) == ("place", 4)


def test_unimplemented_mode_returns_gracefully(monkeypatch):
    game = Game(Player("Emma", "X"), Player("Computer Rules", "O"))
    game.apply_action(("place", 4))
    ui = FakeUI()

    def unfinished(_game):
        raise NotImplementedError

    monkeypatch.setattr(app, "choose_rule_based_action", unfinished)
    try:
        app.select_action(game, "rules", ui)
    except NotImplementedError:
        pass
    else:
        raise AssertionError("The simulated unfinished mode should be reported")


def test_cancel_match_never_records_statistics(monkeypatch):
    class QuitUI(FakeUI):
        def ask_human_action(self, game):
            raise QuitMatch()

    monkeypatch.setattr(app, "save_statistics", lambda *_: (_ for _ in ()).throw(AssertionError("should not save")))
    ui = QuitUI()
    stats = {}
    result = app.play_match("human", ui, stats, Player("Emma", "X"), Player("Chioma", "O"))
    assert result == "quit"
    assert stats == {}
