"""Gate 6: integration with the prepared app (run after Tasks 1-5)."""
from stone_lines import app
from stone_lines.game import Game
from stone_lines.player import Player


class PromptUI:
    def ask_human_action(self, game):
        return game.get_legal_actions()[0]


def test_existing_human_mode_preserved():
    game=Game(Player('Emma','X'), Player('Chioma','O'))
    assert app.select_action(game,'human',PromptUI())==('place',0)


def test_random_mode_computer_turn_returns_legal_action():
    game=Game(Player('Emma','X'), Player('Computer Random','O'))
    game.apply_action(('place',0))
    previous=(game.board.copy(),game.current_player)
    result=app.select_action(game,'random',PromptUI())
    assert result in game.get_legal_actions()
    assert (game.board,game.current_player)==previous


def test_rules_mode_computer_turn_returns_legal_action():
    game=Game(Player('Emma','X'), Player('Computer Rules','O'))
    game.apply_action(('place',0))
    previous=(game.board.copy(),game.current_player)
    result=app.select_action(game,'rules',PromptUI())
    assert result in game.get_legal_actions()
    assert (game.board,game.current_player)==previous
